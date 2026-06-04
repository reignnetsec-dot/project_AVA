import pandas as pd
from data_entry import get_deposit_amount, get_withdraw_amount
from data_handler import load_data, save_data


TOTAL_BALANCE_PATH = "data/total_balance.csv"
FINANCE_LOGS_PATH = "data/finance_logs.csv"


class Account:
    def __init__(self):
        self.balance_path = TOTAL_BALANCE_PATH
        self._ensure_balance_file()


    def _ensure_balance_file(self):
        try:
            df = load_data(self.balance_path)
            if "balance" not in df.columns:
                raise ValueError
        except (FileNotFoundError, ValueError):
            pd.DataFrame({"balance": [0]}).to_csv(self.balance_path, index=False)


    def _get_balance(self) -> pd.DataFrame:
        return load_data(TOTAL_BALANCE_PATH)["balance"].iloc[0]
    

    def _set_balance(self, balance):
        # total_balance = self._get_balance() + balance
        df = load_data(TOTAL_BALANCE_PATH)
        df.loc[0, 'balance'] = balance
        # save_data({"balance": [balance]}, TOTAL_BALANCE_PATH)
        df.to_csv(TOTAL_BALANCE_PATH, index=False)


    def deposit(self, amount: float):
        # balance = self._get_balance()
        new_balance = self._get_balance() + amount
        self._set_balance(new_balance)
        print(f"Deposited R{amount}. New balance: R{new_balance} 🤑")


    def withdraw(self, amount):
        balance = self._get_balance()
        if amount > balance:
            print("Insufficient funds.")
            return
        new_balance = balance - amount
        self._set_balance(new_balance)
        print(f"Withdrew R{amount}. New balance: R{new_balance} 😰")


    def log(self, tag, amount):
        from time_master import get_current_datetime
        dt = get_current_datetime()
        new_log = {"date": dt["date"], "time": dt["time"], "tag": tag, "amount": amount}
        save_data(new_log, FINANCE_LOGS_PATH)


if __name__ == "__main__":
    print(f"Zacharia L. Gumbo\nBalance = R{Account()._get_balance():.2f}")
    print()
    
    prompt = input("What can I do for you?☺️\n1: Deposit, 2: Withdraw\n:").lower().strip()
    print()

    # 1: Deposit
    if prompt == "1":
        deposit_amount = get_deposit_amount()
        Account().deposit(deposit_amount)
        tag = "Deposit"
        Account().log(tag, deposit_amount)

    # 2: Withdraw
    elif prompt == "2":
        withdraw_amount = get_withdraw_amount()
        Account().withdraw(withdraw_amount)
        tag = "Withdraw"
        Account().log(tag, withdraw_amount)

    
