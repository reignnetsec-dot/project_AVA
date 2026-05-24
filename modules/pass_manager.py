import pandas as pd
import random


class PassMan:
    def __init__(self):
        # self.username = username
        # self.password = password
        pass


    def _generate_password(self, strength: int, chars: dict):
        lower_case = chars['lower_case']
        upper_case = chars['upper_case']
        digits = chars['digits']
        punctuation = chars['punctuation']

        if strength == 1:
            # weak password: random lowercase + digits
            password = []
            for _ in range(5):
                lower_case_char = random.choice(lower_case)
                password.append(lower_case_char)
            for _ in range(5):
                digit = random.choice(digits)
                password.append(digit)
            return ''.join(password)
        
        elif strength == 2:
            # mid password: random lowercase + uppercase + digits
            ...
        elif strength == 3:
            # strong password: random lowercase + uppsercase + digits + symbols
            ...
        else:
            ...


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
    
    pass_man = PassMan()

    chars = {
            # Lowercase letters
            'lower_case': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

            # Uppercase letters
            'upper_case': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

            # Digits
            'digits': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

            # Punctuation & symbols (the 32 printable symbols on US QWERTY)
            'punctuation': ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':',
               "'", '"', ',', '<', '.', '>', '/', '?']
            }

    print(pass_man._generate_password(1, chars))