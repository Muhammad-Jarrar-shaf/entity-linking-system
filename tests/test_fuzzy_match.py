from app.linker import find_best_match


def test_find_best_match():
    kb = [
        "Apple Inc",
        "Microsoft",
        "Google"
    ]

    result = find_best_match(
        "Apple",
        kb
    )

    assert result[0] == "Apple Inc"