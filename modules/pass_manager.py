import pandas as pd
import random


class PassMan:
    def __init__(self):
        # self.username = username
        # self.password = password
        pass

    
    # generate password
    def _generate_password(self, strength: int, chars: dict):
        lower_case = chars['lower_case']
        upper_case = chars['upper_case']
        digits = chars['digits']
        punctuation = chars['punctuation']
        all_chars = lower_case + upper_case + digits + punctuation

        password = []
        if strength == 1:
            # weak password: random lowercase + digits
            for _ in range(5):
                lower_case_char = random.choice(lower_case)
                password.append(lower_case_char)
            for _ in range(5):
                digit = random.choice(digits)
                password.append(digit)
        
        elif strength == 2:
            # mid password: random lowercase + uppercase + digits

            sequence = [1, 2, 3, 4]
            for _ in range(3):
                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    lower_case_char = random.choice(lower_case)
                    password.append(lower_case_char)
            
                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    digit = random.choice(digits)
                    password.append(digit)

                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    upper_case_char = random.choice(upper_case)
                    password.append(upper_case_char)

        elif strength == 3:
            # strong password: random lowercase + uppsercase + digits + symbols

            sequence = [1, 2, 3, 4, 5, 1, 2]
            for _ in range(3):
                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    lower_case_char = random.choice(lower_case)
                    password.append(lower_case_char)
            
                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    digit = random.choice(digits)
                    password.append(digit)

                random_sequence = random.choice(sequence)
                for _ in range(random_sequence):
                    upper_case_char = random.choice(upper_case)
                    password.append(upper_case_char)

            sequence = sequence[0:1]
            random_sequence = random.choice(sequence)
            for _ in range(random_sequence):
                punctuation = random.choice(punctuation)
                password.append(punctuation)

        return ''.join(password)
        

    # save generated password
    # 
    def _to_csv(self, username, password):
        details_dict = {
            'username': username,
            'password': password
        }

        new_row = pd.DataFrame([details_dict])
        existing = pd.read_csv('credentials.csv')
        credentials_df = pd.concat([existing, new_row], ignore_index=True)
        credentials_df.to_csv('credentials.csv', index=False)


if __name__ == "__main__":
    username = input("username: ")
    password = input("password: ")
    
    
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

    if username is not None and password is not None:
        pass_man._to_csv(username, password)
    elif username != "" and not password:
        strength = input("Strength of password (1, 2, 3): ")
        if not strength:
            strength = 1
        generated_password = pass_man._generate_password(strength, chars)
        print(f"Strength {strength} password generated: {generated_password}")
    elif username == False and password == True:
        print(f"Please enter username.")