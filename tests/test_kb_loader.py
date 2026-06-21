# tests/test_kb_loader.py

from app.kb import load_kb


def test_load_kb():
    kb = load_kb()

    assert len(kb) > 0

    assert "entity" in kb[0]

    assert "url" in kb[0]