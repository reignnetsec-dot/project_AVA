# from modules.pass_manager import PassMan
import pandas as pd
import random


learning_rate = 0.08


class Brain:
    def __init__(self, prompt: str):
        self.prompt = prompt


    def type(self):
        type = ["greet", "None", "Noon"]
        return random.choice(type)


    def ask_answer(self):
        print(f"Prompt: {self.prompt}")
        answer = input("Answer: ")

        df = pd.read_csv("data/memory.csv")
        df.loc[0, "prompt"] = self.prompt
        df.loc[0, "answer"] = answer

        
        while True:
            type = self.type()
            print(f"Type: {type}")
            val_type = input("Validate Type: ")
            if val_type == "y":
                df.loc[0, "type"] = type
                break
            elif val_type == "n":
                print("Lets try again.")
            else:
                print("Please validate type.")


        df.loc[0, "confidence"] = learning_rate + learning_rate
        
        df.to_csv("data/memory.csv", index=False)


brain = Brain("hello")
while True:
    brain.ask_answer()