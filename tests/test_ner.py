from app.ner import extract_entities


def test_extract_entities():
    text = "Elon Musk visited Pakistan."

    entities = extract_entities(text)

    assert len(entities) > 0

    assert "Elon Musk" in entities

    assert "Pakistan" in entities