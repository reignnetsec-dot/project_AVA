# from modules.pass_manager import PassMan
import pandas as pd



class AvaBrain:
    def __init__(self, prompt: str):
        self.prompt = prompt.lower().strip()


    def memory_handler(self):
        memory = pd.read_csv('data/memory.csv', index_col='prompt')
        return memory


    def tokens(self):
        return self.prompt.split()


    def intent(self):
        ...


ava_brain = AvaBrain("Generate a password with strength 3")
print(ava_brain.memory_handler())
# print(ava_brain.prompt)
print(ava_brain.tokens())
