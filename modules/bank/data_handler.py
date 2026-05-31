import pandas as pd
import os


"""UNIVERSAL DATA LOADER"""
"""STUDY THIS FUNCTION"""
def load_data(data_path: str, columns = None) -> pd.DataFrame:
    """
    Load a CSV file. If missing or empty, create it with the specified columns.
    Always returns a DataFrame with the given columns (in that order).
    """
    # infer columns if not provided
    if columns is None:
        if "balance" in data_path:
            columns = ["balance"]
        elif "log" in data_path or "finance" in data_path:
            columns = ["date", "time", "tag", "amount"]
        else:
            # generic: just load whatever exists, or return empty
            if os.path.exists(data_path):
                return pd.read_csv(data_path)
            return pd.DataFrame()
        
    # Ensure file exists with the right columns
    if not os.path.exists(data_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(data_path, index=False)
        return df
    
    # File exists - read and align columns
    df = pd.read_csv(data_path)
    # Add missing columns (at the end)
    for col in columns:
        if col not in df.columns:
            df[col] = None

    # Keep only the desired columns, in the order given
    df = df[columns]
    return df


def save_data(data: dict, data_path: str):
    df = load_data(data_path, columns=data.keys())
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(data_path, index=False)