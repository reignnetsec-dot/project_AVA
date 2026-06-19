import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.encrypt import run_encryptor_cli


while True:
    print()
    prompt = input("::AVA:: What can I do for you?\n")

    if prompt == "encrypt":
        run_encryptor_cli()