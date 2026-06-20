from __future__ import annotations
from pathlib import Path

from modules.password_generator.core import PasswordGenerator
from modules.utils.file_handler import row_to_csv
from modules.time_master.time_master import get_datetime


CREDENTIALS = "/home/reign/projects/project_AVA/modules/password_generator/data/credentials.csv"


def password_generator_flow():
    password_strength = int(input("Select password strength (1, 2, 3): "))
    print("Genarating new password.")
    new_password = PasswordGenerator().generate_password(password_strength)
    return new_password


def save_credentials_flow(file_path, password="None"):
    username = input("Username: ")
    # password = ...
    description = input("Description: ")
    datetime = get_datetime()
    data_dict = {
        "date": datetime["date"],
        "time": datetime["time"],
        "description": description,
        "username": username,
        "password": password
    }
    row_to_csv(data_dict, file_path)


def run_password_generator_cli():
    action = input("Type 'g' to generate password.\nType 's' to save existing credentials.\n: ").strip().lower()

    try:
        if action == "g":
            new_password = password_generator_flow()
            print(new_password)
            action = input("Do you want to save the password ('Yes' or 'No')\n: ").lower().strip()
            if action == "yes":
                save_credentials_flow(CREDENTIALS, new_password)
        elif action == "s":
            save_credentials_flow(CREDENTIALS)
    except Exception as error:
        print(f"Operation failed: {error}")

run_password_generator_cli()


