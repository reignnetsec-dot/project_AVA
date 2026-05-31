import pandas as pd
from data_entry import get_date, get_amount, get_tag, get_description, get_deposit_amount, get_withdraw_amount
from data_handler import load_data, save_data


TOTAL_BALANCE_PATH = "data/total_balance.csv"


class Account:
    def __init__(self):
        ...


    def deposit(self):
        deposit_amount = get_deposit_amount()
        df = load_data(TOTAL_BALANCE_PATH)
        new_balance = df.balance + deposit_amount
        balance_dict = {
            "balance": new_balance
        }
        new_balance_df = pd.DataFrame(balance_dict)
        new_balance_df.to_csv(TOTAL_BALANCE_PATH, index=False)


    def withdraw(self):
        withdraw_amount = get_withdraw_amount()
        df = load_data(TOTAL_BALANCE_PATH)
        new_balance = df.balance - withdraw_amount
        balance_dict = {
            "balance": new_balance
        }
        new_balance_df = pd.DataFrame(balance_dict)
        new_balance_df.to_csv(TOTAL_BALANCE_PATH, index=False)


if __name__ == "__main__":
    # prompt = input("What can I do for you?\nDeposit, Withdraw\n:").lower()
    Account().deposit()
    
