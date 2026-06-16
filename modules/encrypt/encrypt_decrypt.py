from .cli import run_encryptor_cli
from .core import DEFAULT_STORAGE_DIR, decrypt_credentials, encrypt_credentials

__all__ = [
    "DEFAULT_STORAGE_DIR",
    "encrypt_credentials",
    "decrypt_credentials",
    "encrypt_decrypt",
    "run_encryptor_cli",
]


def encrypt_decrypt() -> None:
    run_encryptor_cli()
