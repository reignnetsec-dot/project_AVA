import pandas as pd


class PassMan:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


    def _to_csv(self, username, password):
        detail_dict = {
            'username': username,
            'password': password
        }
        new_row = pd.DataFrame([detail_dict])
        existing = pd.read_csv('credentials.csv')
        credentials_df = pd.concat([existing, new_row], ignore_index=True)
        credentials_df.to_csv('credentials.csv', index=False)


if __name__ == "__main__":
    username_input = input("USERNAME: ")
    password_input = input("PASSWORD: ")
    pass_man = PassMan(username_input, password_input)
    pass_man._to_csv(username_input, password_input)