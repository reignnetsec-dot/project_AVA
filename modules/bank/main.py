import pandas as pd


class data_handler:
    DATA_PATH: str = 'finance.csv'
    COLUMNS = ['date', 'amount', 'tag', 'description']


    @classmethod
    def load_data(cls):
        try:
            df = pd.read_csv(cls.DATA_PATH)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.DATA_PATH, index=False)
        return df
    

    @classmethod
    def save_data(cls, data: dict):
        df = cls.load_data()
        new_row = pd.DataFrame([data], columns=cls.COLUMNS)
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(cls.DATA_PATH, index=False)


data = {
    "date": '2026/05/30',
    "amount": 100,
    "tag": "income",
    "description": 'construction-work'
}
data_handler.save_data(data)