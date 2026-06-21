import pandas as pd


def load_kb(filepath="data/knowledge_base.csv"):
    df = pd.read_csv(filepath)
    return df.to_dict(orient="records")


def get_entity_names():
    kb = load_kb()

    return [row["entity"] for row in kb]