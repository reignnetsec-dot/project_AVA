from __future__ import annotations
from pathlib import Path

from modules.password_generator.core import PasswordGenerator


def password_generator_flow():
    password_strength = int(input("Select password strength (1, 2, 3): "))
    print("Genarating new password.")
    new_password = PasswordGenerator().generate_password(password_strength)
    return new_password


def run_password_generator_cli():
    action = input("Type 'g' to generate password.\nType 's' to save existing credentials.\n: ").strip().lower()

    try:
        if action == "g":
            print(password_generator_flow())
    except Exception as error:
        print(f"Operation failed: {error}")

run_password_generator_cli()




# if __name__ == "__main__":
#     print("PasswordGenerator\n")
#     print("g = generate new password.\ns = save existing credentials.\nq = quit.\n")

#     while True:
#         prompt = input("What can I do for you.\n:\n")
#         if prompt == "g":
#             strength = int(input("Select Strength (1, 2, 3): "))
#             print("Generating new password.")
#             new_password = PasswordGenerator(strength, chars)._generate_password()
#             print(f"Generated Password: {new_password}")
#         elif prompt == "s":
#             username = input("Input new username: ")
#             password = input("Input new password: ")
#             description = input("Description: ")
#             PasswordGenerator(chars=chars)._to_csv(description, username, password)