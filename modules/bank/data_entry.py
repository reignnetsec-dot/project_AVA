import datetime


def get_date() -> str:
    date = input("Date (DD-MM-YYYY): ")
    if date == "":
        date = datetime.datetime.today().strftime("%d-%m-%Y")
    return date


def get_amount() -> float:
    amount = input("Amount: ")
    if amount == "":
        amount = 0.0
    else:
        amount = float(amount)
    return amount


def get_tag() -> str:
    tag = input("Tag: ")
    if tag == "":
        tag = "None"
    return tag


def get_description() -> str:
    description = input("Description: ")
    if description == "":
        description = "None"
    return description


def get_deposit_amount() -> float:
    while True:
        val = input("Deposit amount: ").strip()
        if val == "":
            return 0.0
        try:
            return float(val)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def get_withdraw_amount() -> float:
    withdraw_amount = input("Withdraw amount: ")
    if withdraw_amount == "":
        withdraw_amount = 0.0
    return float(withdraw_amount)

