import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str):
    """
    Extract named entities from text.

    Args:
        text (str): Input text

    Returns:
        list[str]
    """

    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append(ent.text)

    return entities