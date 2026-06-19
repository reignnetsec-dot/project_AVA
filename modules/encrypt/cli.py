from __future__ import annotations

from pathlib import Path

from .core import DEFAULT_STORAGE_DIR, decrypt_credentials, encrypt_credentials

from ..utils.validators import normalize_filename, prompt_non_empty


# def _normalize_filename(filename: str, extension: str) -> str:
#     filename = filename.strip()
#     if not filename:
#         raise ValueError("Filename cannot be empty.")
#     return filename if filename.lower().endswith(extension) else f"{filename}{extension}"


# def _prompt_non_empty(prompt: str) -> str:
#     value = input(prompt).strip()
#     if not value:
#         raise ValueError("Input cannot be empty.")
#     return value


def run_encryptor_cli(storage_dir: Path = DEFAULT_STORAGE_DIR) -> None:
    storage_dir = Path(storage_dir)
    storage_dir.mkdir(parents=True, exist_ok=True)

    action = input("Type 'x10' to encrypt, 'd10' to decrypt| ").strip().lower()
    print()

    try:
        if action == "x10":
            _encrypt_flow(storage_dir)
        elif action == "d10":
            _decrypt_flow(storage_dir)
        else:
            print("Invalid option.")
    except Exception as error:
        print(f"Operation failed: {error}")


def _encrypt_flow(storage_dir: Path) -> None:
    username = input("username: ").strip()
    password = input("password: ").strip()

    if not username and not password:
        print("At least username or password is required.")
        return

    user_token_file = normalize_filename(prompt_non_empty("username-file| "), ".npy")
    pass_token_file = normalize_filename(prompt_non_empty("password-file| "), ".npy")
    key_file = normalize_filename(prompt_non_empty("key-name: "), ".enc")

    print("----------------------------------")
    print("KEEP KEY SAFE. DO NOT SHARE ⚠️")
    print("----------------------------------\n")

    master_password = prompt_non_empty("Set master password. KEEP SAFE ⚠️ | ")
    if len(master_password) < 10:
        print("Master password must be at least 10 characters.")
        return

    confirm_password = input("Confirm master password: ").strip()
    if master_password != confirm_password:
        print("Passwords do not match. Exiting.")
        return

    encrypt_credentials(
        master_password=master_password,
        username=username,
        password=password,
        user_token_path=storage_dir / user_token_file,
        pass_token_path=storage_dir / pass_token_file,
        mapping_path=storage_dir / key_file,
    )

    print()
    print(
        f"Encryption Complete ✅ -> {user_token_file}, {pass_token_file}, {key_file}"
    )


def _decrypt_flow(storage_dir: Path) -> None:
    user_token_file = normalize_filename(prompt_non_empty("Encrypted File-1: "), ".npy")
    pass_token_file = normalize_filename(prompt_non_empty("Encrypted File-2: "), ".npy")
    key_file = normalize_filename(prompt_non_empty("key: "), ".enc")
    master_password = prompt_non_empty("Master Password: ")

    username, password = decrypt_credentials(
        master_password=master_password,
        user_token_path=storage_dir / user_token_file,
        pass_token_path=storage_dir / pass_token_file,
        mapping_path=storage_dir / key_file,
    )

    print("Decryption Complete ✅")
    print(f"Decrypted username: {username}")
    print(f"Decrypted password: {password}")
