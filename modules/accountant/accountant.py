from datetime import datetime

import pandas as pd

print('ACCOUNTANT')

# DATE AND TIME
now = datetime.now()
# Format date as dd/mm/yyyy
date_str = now.strftime("%d/%m/%Y")
# Format time as hh/mm (24-hour)
time_str = now.strftime("%H:%M")


"""I want to have a database/csv file with all possible things I could say in the prompt to get what I want from accountant."""
prompt = input("Prompt:\n")


if prompt.lower() == "w":

    """Create a loop that repeats when user not entered amount"""
    # amount
    while True:
        try:
            amount_float: float = round(float(input("R")), 2)
            amount_str = f"R{amount_float:.2f}"
            #print(amount_str)
        except ValueError as e:
            amount_float = 0.0


        # date and time

        """I want to do somethign if tag is approved or disapproved."""
        # tag (approved/disapproved)
        tag = input("Tag: ")
        if tag.lower() == "ap":
            tag = "approved"
        elif tag.lower() == "dp":
            tag = "disapproved"
        elif tag.lower() == None:
            tag = "pending"

        """Creating dict, DataFrame and save to CSV"""
        data = {"date": [date_str],
                "time": [time_str],
                "amount_float": [amount_float],
                "tag": [tag]}
        #print(data)

        df_data = pd.DataFrame(data=data, )
        #print(df_data)
        df_data.to_csv("reign_financials.csv", mode="a", header=False, index=False)

elif prompt.lower() == "r":
    df_financials = pd.read_csv("reign_financials.csv")
    #print(df)

    # Total amount
    amount_series = df_financials["amount_float"]

    total_list = []
    for total in amount_series:
        total_list.append(total)

    grand_total = sum(total_list)

    # Montly amount
    date_series = df_financials["date"]
    """I need to find a way to get the A.V.A to understand months, so that I can give a prompt like PROMPT:'Show the last month amount' """

else:
    ...
