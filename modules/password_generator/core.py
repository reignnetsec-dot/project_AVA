import random


CHARS = {
            'lower_case': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

            'upper_case': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],

            'digits': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],

            'punctuation': ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
               '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':',
               "'", '"', ',', '<', '.', '>', '/', '?']}


class PasswordGenerator:
    def __init__(self, chars: dict = CHARS):
        self.chars = chars

    # def ensure_credentials_file_exists(self):
    #     CREDENTIALS.parent.mkdir(parents=True, exist_ok=True)
    #     if not CREDENTIALS.exists():
    #         pd.DataFrame(columns=["date", "time", "description", "username", "password"]).to_csv(CREDENTIALS, index=False)

    def generate_password(self, strength: int = 1):
        lower_case = self.chars['lower_case']
        upper_case = self.chars['upper_case']
        digits = self.chars['digits']
        punctuation = self.chars['punctuation']

        password = []
        if strength == 1:
            for _ in range(5):
                lower_case_char = random.choice(lower_case)
                password.append(lower_case_char)
            for _ in range(5):
                digit = random.choice(digits)
                password.append(digit)

        elif strength == 2:
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
                punct_char = random.choice(punctuation)
                password.append(punct_char)
        return ''.join(password)




