from app.ner import extract_entities


def test_extract_entities():
    entities = extract_entities(
        "Elon Musk visited Pakistan."
    )

    assert len(entities) > 0

    assert entities[0]["text"] == "Elon Musk"
    assert entities[0]["label"] == "PERSON"