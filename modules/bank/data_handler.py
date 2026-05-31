import pandas as pd


COLUMNS = ['date', 'amount', 'tag', 'description']


def load_data(data_path: str):
    try:
        df = pd.read_csv(data_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(FINANCE_LOGS_PATH, index=False)
    return df
    

def save_data(data: dict, data_path):
    df = load_data(data_path)
    new_row = pd.DataFrame([data], columns=COLUMNS)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FINANCE_LOGS_PATH, index=False)