import pandas as pd
from typing import List, Dict

def load_medquad_data(csv_path: str) -> List[Dict]:
    """
    Loads medquad_cleaned.csv and returns a list of dicts, one per row.
    Each dict contains: source, filename, question, answer, url
    """
    df = pd.read_parquet(csv_path)
    passages = df.to_dict(orient="records")
    return passages

if __name__ == "__main__":
    csv_path = "hf://datasets/lavita/MedQuAD/data/train-00000-of-00001-e36383d177026d53.parquet"
    passages = load_medquad_data(csv_path)
    print(f"Loaded {len(passages)} passages.")
    print("Sample:", passages[0])
