from app.linker import process_text


def test_process_text():
    text = "Elon Musk visited Pakistan."

    results = process_text(text)

    assert len(results) > 0

    assert results[0]["entity"] == "Elon Musk"