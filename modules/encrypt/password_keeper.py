"""
Password_Keeper:

1. Save passwords in categories:
   Red -> (HS) Heavy Security
   Blue -> (S-HS) Semi-Heavy Security
   Green -> (LS) Light Security

2. Encryption and Decryption using one‑time pad (per‑character random tokens).

3. Binary storage with NumPy (no CSV string conversions).
"""


import os
import numpy as np
import pickle
from typing import Tuple
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


# Helper: Encrypt mapping to file
def _save_encrypted_mapping(mapping_arr, master_password: str, filename: str) -> None:
    """
    Save a numpy structured array (mapping) encrypted with master password.
    """
    salt = os.urandom(16)
    iv = os.urandom(12)
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
        backend=default_backend()
    )
    key = kdf.derive(master_password.encode())
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    # Serialize the numpy array to bytes using pickle
    data = pickle.dumps(mapping_arr)
    ciphertext = encryptor.update(data) + encryptor.finalize()
    with open(filename, "wb") as f:
        f.write(salt + iv + encryptor.tag + ciphertext)
    return None


def _load_encrypted_mapping(filename: str, master_password: str):
    """Load and decrypt the mapping file"""
    with open(filename, "rb") as f:
        data = f.read()
    salt = data[:16]
    iv = data[16:28]
    tag = data[28:44]
    ciphertext = data[44:]
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=salt,
        iterations=600000,
        backend=default_backend()
    )
    key = kdf.derive(master_password.encode())
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return pickle.loads(plaintext)


# Encryption
def encrypt(master_password: str, file_names: list[str], credentials: list[str], max_length: int = 64) -> bool:

    """
    Encrypt username and password with perfect secrecy (one-time pad).
    Saves:
        user_token_file : fixed-length list of tokens for username (padded)
        pass_token_file : fixed-length list of tokens for password (padded)
        key_file        : encrypted mapping (character -> token) for all used tokens
    Returns True on success, raises exceptions on failure.
    """
    username, password = credentials[0], credentials[1]

    # Input Validation
    if not master_password:
        raise ValueError("Master password cannot be empty.")
    if not username and not password:
        raise ValueError("At least username or password must be provided.")
    
    # Pad strings to fixed length (hide true length, preserve perfect secrecy)
    username_padded = username.ljust(max_length, "\x00") # pad with null chars
    password_padded = password.ljust(max_length, "\x00")

    # Generate random tokens for each character
    user_tokens = [os.urandom(64) for _ in range(max_length)]
    pass_tokens = [os.urandom(64) for _ in range(max_length)]

    # save token sequences as npy files
    np.save(file_names[0], user_tokens, allow_pickle=True)
    np.save(file_names[1], pass_tokens, allow_pickle=True)

    # Build mapping (only for actual characters, not padding)
    # Include mapping for real username characters (ignore padding nulls)
    mapping = []
    for ch, tok in zip(username, user_tokens[:len(username)]):
        mapping.append((ch, tok))
    for ch, tok in zip(password, pass_tokens[:len(password)]):
        mapping.append((ch, tok))

    # Suggestion: Also add a special sentinel for padding (optional - ensures no token reuse)

    # Save mapping as a structured NumPy array
    dtype = [("char", object), ("token", object)]
    mapping_arr = np.array(mapping, dtype=dtype)

    _save_encrypted_mapping(mapping_arr, master_password, file_names[2])

    return True


# Decryption
def decrypt(master_password: str, user_token_file: str = "username_tokens.npy", pass_token_file: str = "password_tokens.npy", key_file: str = "key.enc") -> Tuple[str, str]:
    """
    Load the token files and the key file, then reconstruct the original username and password.
    Returns (username, password).
    """
    # Load token lists
    try:
        user_tokens = np.load(user_token_file, allow_pickle=True).tolist()
        pass_tokens = np.load(pass_token_file, allow_pickle=True).tolist()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Missing file: {e}")

    # Load mapping and build lookup dictionary: token -> character
    mapping_arr = _load_encrypted_mapping(key_file, master_password)
    lookup = {row["token"]: row["char"] for row in mapping_arr}

    # Decode username - stop at first token not in lookup (padding)
    username_chars = []
    for tok in user_tokens:
        ch = lookup.get(tok)
        if ch is None:
            break # padding token reached
        if ch == "\x00":
            break # safety: null characters also stops
        username_chars.append(ch)

    # Decode password - same logic
    password_chars = []
    for tok in pass_tokens:
        ch = lookup.get(tok)
        if ch is None:
            break
        if ch == "\x00":
            break
        password_chars.append(ch)

    return "".join(username_chars), "".join(password_chars)


# Main Interface
if __name__ == "__main__":
    # get file names to save encrypted data

    # file extensions
    npy_ext = ".npy"
    enc_ext = ".enc"

    # directory path -> save encoded files
    path = "/home/reign/projects/ml-projects/scripts/encoded_files/"

    print()
    print("---------------------------------------------")
    work = input("Type 'x10' to encrypt, 'd10' to decrypt| ").strip()
    print("---------------------------------------------")
    print()

    if work == "x10":
        # get details to be encrypted
        username = input("username: ")
        password = input("password: ")
        credentials = [username, password]

        # file names
        print()
        user_token_file = input("username-file| ") + npy_ext
        pass_token_file = input("password-file| ") + npy_ext
        print()
        key_file = input("key-name: ") + enc_ext
        print("----------------------------------")
        print("KEEP KEY SAFE. DO NOT SHARE ⚠️")
        print("----------------------------------")

        file_names = [path+user_token_file, path+pass_token_file,
        path+key_file]

        if "" in credentials:
            for n in range(1):
                print()
                print("Error -> {missing data}")
                print()
                if n == 0:
                    print()
                    print("Exiting for Security reasons")
                    exit()
        else:
            print()
            print("Data Accepted")

            # set master password
            print()




            # SET MASTER PASSWORD >= 10 chars
            master_pwd = input("Set master password. KEEP SAFE ⚠️ | ")
            print()

            if len(master_pwd) < 10:
                for _ in range(2):
                    master_pwd = input("Set longer master password: ")
                    if len(master_pwd) >= 10:
                        break
                print()
                print("Exiting for security reasons.")
                exit()
                
            confirm = input("Confirm master password: ")
            print()

            # Confirm Password Validation
            if master_pwd != confirm:
                print("Passwords do not match. Exiting.")
                exit()
            


            # ENCRYPT 
            """must correct the try statement"""
            try:
                encrypt(master_pwd, file_names, credentials)
            except:
                print("Something went wrong")



            print()
            print(f"Encryption Complete ✅ -> {user_token_file}, {pass_token_file}, {key_file}")

            # Reset Variables for extra security
            username = None
            password = None
            user_token_file = None
            pass_token_file = None
            key_file = None
            credentials = None

            print("Exiting...")
            exit()

    elif work == "d10":
        # get file names to decrypt
        user_token_file = input("Encrypted File-1: ")
        pass_token_file = input("Encrypted File-2: ")
        print()

        # get key for decryption
        key_file = input("key: ")
        print()

        # absolute path / file names
        file_names = [path+user_token_file, path+pass_token_file, path+key_file]

        # master password to decrypt
        master_pwd = input("Master Password: ")
        print()

        # Attempt to decrypt using the default filenames
        try:
            # Decrypt and print to console
            user, pwd = decrypt(master_pwd, file_names[0], file_names[1],
file_names[2])
            print("Decryption Complete ✅")
            print(f"Decrypted username: {user}")
            print(f"Decrypted password: {pwd}")
        except FileNotFoundError as e:
            print(f"Missing file: {e}. Run encryption first.")
        except KeyError:
            print("Decryption failed: (wrong password or corrupted file.)")
    else:
        print("Invalid option.")
