# from modules.pass_manager import PassMan
import pandas as pd
import random



class Train:
    

    def __init__(self, prompt: str):
        self.prompt = prompt.lower().strip()
        self.LEARNING_RATE = 0.05

    def train(self):
        
        df_memory = pd.read_csv('data/memory.csv')

        while True:
            ava_answer = ['hie', 'no', 'what', 'hello', 'how are you', 'who are you']
            answer = random.choice(ava_answer)

            print(f"Prompt: {self.prompt}\nAnswer: {answer}")
            print()

            # intent = input("Intent: ")
            score: int = int(input("Eval: "))
            
            if score == 1:
                if 'confidence' not in df_memory.columns:
                    df_memory['confidence'] = 0.0
                elif 'confidence' in df_memory.columns:
                    df_memory['confidence'] = 0.0
                df_memory.loc[:, 'confidence']  += self.LEARNING_RATE
                df_memory.to_csv('data/memory.csv', index=False)

            # else:
            #     w[answer] -= 0.1

            print()
            print(f"Prompt -> {self.prompt}\nAnswer -> {answer}\nConfidence -> {df_memory['confidence']}")
            print()


ava = Train("hello")
ava.train()
