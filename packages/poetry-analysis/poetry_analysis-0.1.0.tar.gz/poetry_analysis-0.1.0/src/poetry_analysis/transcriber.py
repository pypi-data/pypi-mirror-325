"""Module for downloading Norwegian G2P-models
and transcribe Bokmål text to phonemic transcription with the Nofabet notation.

Script for transcribing a textfile using a pre-trained g2p model.
"""

import json
import logging
import re
import string
from pathlib import Path
from typing import Generator

import phonetisaurus
from convert_pa import nofabet_to_ipa, convert_nofabet
from google.cloud import storage


PUNCTUATION_MARKS = str(
    string.punctuation + "‒.,!€«»’”—⁷⁶⁰–‒––!”-?‒"
)  # Note! The three long dashes look identical, but are different unicode characters


def is_punctuation(char: str) -> bool:
    """Check if a character is a punctuation mark."""
    return char in PUNCTUATION_MARKS


def strip_redundant_whitespace(text: str) -> str:
    """Strip redundant whitespace and reduce it to a single space."""
    return re.sub(r"\s+", " ", text).strip()


def strip_punctuation(string: str) -> str:
    """Remove punctuation from a string"""
    alphanumstr = ""
    for char in string:
        if not is_punctuation(char):
            alphanumstr += char
    return strip_redundant_whitespace(alphanumstr)


def download_public_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a public blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client.create_anonymous_client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)


def download_g2p_model(dialect="e", style="written"):
    """
    Download a pre-trained g2p model for a given language.
    """
    filename = f"nb_{dialect}_{style}.fst"
    download_dir = Path.home() / ".cache" / "g2p_models"
    download_dir.mkdir(parents=True, exist_ok=True)
    download_path = download_dir / filename
    bucket_name = "g2p-models"

    if not download_path.exists():
        try:
            download_public_file(bucket_name, filename, download_path)
            logging.debug("Download successful.")
        except Exception as e:
            logging.error(e)
            logging.info(f"No pre-trained g2p model available for {dialect} {style}.")

    logging.debug(f"Path to the G2P model: {download_path}.")
    return download_path


def format_transcription(pronunciation):
    return " ".join(pronunciation)


def syllabify(transcription: list[list]) -> list:
    """Flatten list of syllables from a list of transcribed words."""
    syllables = [
        syll  # if syll is not None else "NONE"
        for word, pron in transcription
        for syll in convert_to_syllables(pron, ipa=False)
    ]
    return syllables


def convert_to_syllables(phonemes: list, ipa=False) -> list:
    """Turn a sequence of phonemes into syllable groups."""
    transcription = phonemes if isinstance(phonemes, str) else " ".join(phonemes)
    if ipa:
        ipa = nofabet_to_ipa(transcription)
        syllables = ipa.split(".")
    else:
        syllables = convert_nofabet.nofabet_to_syllables(transcription)
    return syllables


def transcribe(text, dialect="e", style="written", full_annotation=False) -> Generator:
    """
    Transcribe a text of whitespace-separated words using a pre-trained g2p model.
    """
    text = strip_punctuation(text)
    words = text.split()
    transcriptions = transcribe_words(words, dialect=dialect, style=style)
    if full_annotation:
        return annotate_transcriptions(transcriptions)
    return ((word, format_transcription(pron)) for word, pron in transcriptions)


def annotate_transcriptions(transcription: list) -> Generator:
    for word, pronunciation in transcription:
        nofabet = format_transcription(pronunciation)
        yield dict(
            word=word,
            nofabet=nofabet,
            syllables=convert_nofabet.nofabet_to_syllables(nofabet),
            ipa=nofabet_to_ipa(nofabet),
        )


def transcribe_words(words, dialect="e", style="written"):
    """
    Transcribe a list of words using a pre-trained g2p model.
    """
    model_path = download_g2p_model(dialect=dialect, style=style)
    transcriptions = phonetisaurus.predict(words, model_path=model_path)
    return transcriptions


def split_paragraphs(text: str) -> list:
    """Split a text into paragraphs and paragraphs into lines."""
    return [
        [line.rstrip() for line in paragraph.rstrip().splitlines()]
        for paragraph in re.split("\n{2,}", text)
        if paragraph
    ]


def transcribe_file(file, dialect="e", style="written"):
    file = Path(file)
    text = file.read_text()

    text_id = file.stem
    # print(f"Text ID: {text_id}")

    annotations = {
        "text_id": text_id,
    }

    textlines = text.splitlines()

    for line_id, line in enumerate(textlines):
        if line == "":
            annotations[f"line_{line_id}"] = []
            continue
        transcriptions = transcribe(
            line, dialect=dialect, style=style, full_annotation=False
        )
        annotations[f"line_{line_id}"] = list(transcriptions)

    return annotations


if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG)

    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Transcribe a text using a pre-trained g2p model."
    )

    #    parser.add_argument("textfile", type=argparse.FileType("r"), help="Path to a text file.")
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Path to a text file."
    )
    parser.add_argument(
        "-d",
        "--dialect",
        type=str,
        default="e",
        help="Dialect area (e, sw, w, t, n) for transcriptions.",
    )
    parser.add_argument(
        "-s",
        "--style",
        type=str,
        default="written",
        help="Written or spoken pronunciation style for transcriptions.",
    )

    args = parser.parse_args()

    if args.file:        
        file_annotations = transcribe_file(
            args.file, dialect=args.dialect, style=args.style
        )
        file_annotations["dialect"] = args.dialect + "_" + args.style
        print(json.dumps(file_annotations))
    else: 
        text = """Kvass som kniv
i daudkjøt flengjande. 
Sanningstyrst 
mot ljoset trengjande. 
"""
        annotations = transcribe(text, dialect=args.dialect, style=args.style)
        print(json.dumps(list(annotations), ensure_ascii=False))

    ## TESTING CODE
    # download_g2p_model(dialect='t', style= "written")

    # text = "I Nasjonalbiblioteket har vi veldig mange gamle og sjeldne bøker"

    #
    # result = transcribe(args.textfile.read(), dialect='t', style= "written")
    # for word, pron in result:
    #   print(f"{word}: {pron}")
