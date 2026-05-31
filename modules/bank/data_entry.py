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
    deposit_amount = input("Deposit amount: ")
    if deposit_amount == "":
        deposit_amount = 0.0
    return float(deposit_amount)


def get_withdraw_amount() -> float:
    withdraw_amount = input("Withdraw amount: ")
    if withdraw_amount == "":
        withdraw_amount = 0.0
    return float(withdraw_amount)

