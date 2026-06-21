from rapidfuzz import process

from app.kb import load_kb


def find_best_match(entity, kb_entities):
    return process.extractOne(entity, kb_entities)


def link_entity(entity):
    kb = load_kb()

    kb_entities = [
        row["entity"]
        for row in kb
    ]

    match = find_best_match(
        entity,
        kb_entities
    )

    matched_name = match[0]
    score = match[1]

    matched_record = next(
        row
        for row in kb
        if row["entity"] == matched_name
    )

    return {
        "entity": entity,
        "matched_entity": matched_name,
        "score": score,
        "url": matched_record["url"]
    }