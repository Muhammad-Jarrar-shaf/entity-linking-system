# app/kb.py

import pandas as pd


def load_kb(filepath="data/knowledge_base.csv"):
    """
    Load the knowledge base from CSV.

    Returns:
        List[dict]
    """

    df = pd.read_csv(filepath)

    records = df.to_dict(orient="records")

    return records