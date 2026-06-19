from pathlib import Path

import pandas as pd


def to_csv(data: dict, file_path):
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    new_row = pd.DataFrame([data])
    if not file_path.exists():
        new_row.to_csv(file_path, index=False)
        return

    existing = pd.read_csv(file_path)
    df = pd.concat([existing, new_row], ignore_index=True)
    df.to_csv(file_path, index=False)