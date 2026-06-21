from app.linker import link_entity


def test_link_entity():
    result = link_entity("Apple")

    assert result["matched_entity"] == "Apple Inc"

    assert "Apple_Inc" in result["url"]