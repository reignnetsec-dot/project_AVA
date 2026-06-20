import random
import pandas as pd


MEMORY = "/home/reign/projects/project_AVA/nlp_model/data/memory.csv"
TOOLS = [
    "password_generator",
    "like",
    "one",
    "None",
    "Liking",
    "No like"
]

class Train:
    def __init__(self, prompt: str, tools: list, file_path: str):
        self.prompt = prompt
        self.file_path = file_path


    """
    Taking guesses, evaluating and then update the memory 
    """
    def guess(self):
        return(random.choice(TOOLS))
    

    def evaluate_guess(self, guess):
        print(guess)

        evaluate: int = int(input("Eval: "))

        if evaluate == 1:
            print("|Added (0.05) confidence.|")
            print(f"Prompt -> |{self.prompt}|\nGuess -> |{guess}|")
            return 0.05
        elif evaluate == 0:
            print("Not validated.")
            return None


    def update_weight(self):
        df = pd.read_csv(self.file_path)
        # get the added weight from evaluation (may be None if not validated)
        delta = self.evaluate_guess(self.guess())
        if delta is None:
            print("No change to weights (not validated).")
            return
        # ensure existing weights are numeric
        df["weight"] = pd.to_numeric(df["weight"], errors="coerce").fillna(0)
        # increment the weight for matching prompt rows
        mask = df["prompt"] == self.prompt
        df.loc[mask, "weight"] = df.loc[mask, "weight"] + delta
        df.to_csv(self.file_path, index=False)

    
    def training_flow(self):
        self.update_weight()


answer = Train("generate new password", TOOLS, MEMORY).training_flow()
# print(f"Answer -> {answer}")
