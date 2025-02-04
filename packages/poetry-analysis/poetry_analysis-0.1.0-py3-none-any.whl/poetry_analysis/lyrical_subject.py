
# Eksplisitt lyrisk jeg: 1.person entall i subjektsform
# Eksplisitt lyrisk jeg-o: 1.person entall i objektsform
# Implisitt lyrisk "jeg": Kontekst-basert 

#%%
import re 
import pandas as pd 

import spacy

#from dotenv import dotenv_values


lyric_i_map = dict(
    explicit_i_subject = [
        "jeg", 
        "eg", 
    ], 
    explicit_i_object = [
        "mig",
        "meg",
        "mine",
        "min", 
        "mitt",
        "mit",
        "mi",
    ],
    implicit_i = [
       
        "vi", 
        "oss",
        "våre",
        "vår",
        "du",
        "deg",
        "dig", 
        "din", 
        "dine", 
        "ditt",
        "dere", 
        "deres",       
    ],
    deixis = [
        "her", 
        "hit",
        "nå",
        "nu",
        "herfra",
        "i morgen", 
        "i går", 
        "i kveld",
        "i fjor",
    ]
)

category_names = dict(
    explicit_i_subject="Explicit I (subject)", 
    explicit_i_object="Explicit I (object)", 
    implicit_i="Implicit I", 
    deixis="Deixis"
    )

def detect_lyric_i(poem_text:str):
    """Map the presence of certain words denoting a lyric I in a poem to categorical labels."""
    lyric_i = {}
    for label, words in lyric_i_map.items(): 
        regx_pattern = "|".join(words)
        matches = re.findall(regx_pattern, poem_text.lower())
        is_present = True if any(matches) else False
        lyric_i[label] = is_present
    return lyric_i




def process_poems(poems, text_field = "textV3"):
    """Annotate whether or not lyric I is a feature in poems in the db"""

    for poem in poems:
        poem_text = poem.get(text_field)
        lyric_features = detect_lyric_i(poem_text)
        yield add_metadata(poem, lyric_features)


def add_metadata(poem, lyric_features):
    """Add metadata from the poem to the annotations."""
    lyric_features["ID"] = int(poem.get("ID"))
    lyric_features["URN"] = poem.get("URN")
    lyric_features["Tittel på dikt"] = poem.get("Tittel på dikt")
    return lyric_features

def connect(env_path: str = ".env"):
    """Connect to a mongoDB server"""
    db_uri = dotenv_values(env_path)["MONGODB_URI"]
    client = pymongo.MongoClient(db_uri)
    return client


def update_db(db, annotations):
    """Write annotations to the database in batches of size batch_size."""
    
    result = db.lyric_features.bulk_write(
        [pymongo.UpdateOne(
            {"ID": poem.get("ID")}, 
            {"$set": poem}, upsert=True)
         for poem in annotations]
    )
    print(result.bulk_api_result) 
        

# %%
if __name__ == "__main__":
   
   
    env_path = "/home/ingeridd/prosjekter/NORN/.env" 
    client = connect(env_path)
    db = client.norn
    
    text_field = "textV3"  #"ferdig_korrektur"  #"ferdig_linje"
    poems = list(db.poems.find(
        {
            text_field: {"$exists": 1},
         }, 
        {
            "_id": 0,  
            "ID": 1, 
            "URN": 1, 
            "Tittel på dikt": 1, 
            "ferdig_linje": 1, 
            "ferdig_korrektur": 1,
            "textV1": 1, 
            "textV2": 1, 
            "textV3": 1, 
        })
    )
    #%%    
    annotations  = [add_metadata(poem, detect_lyric_i(poem.get(text_field))) for poem in poems]
    
    #%% Visualize the annotations
    df = pd.DataFrame(annotations)
    df_sum = df[list(category_names.keys())].sum()
    df_sum.rename(index=category_names).sort_values(ascending=True).plot(kind="barh")
    
    #%% Update the database with the annotations
    update_db(db, annotations)

    #%% Extract pronouns from the poems
    #model_name = "nb_core_news_lg"
    model_name = "da_core_news_lg"
    #model_name = "da_core_news_trf"
    nlp = spacy.load(model_name)
    
    pronouns = []
    for poem in poems:
        doc = nlp(poem.get(text_field))
        pronouns += [token.text for token in doc if token.pos_ == "PRON"]
    
    pronouns = set(pronouns)
   
    #%%
    client.close()
# %%
