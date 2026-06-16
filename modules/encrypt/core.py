from __future__ import annotations

import os
from pathlib import Path
from typing import List, Tuple

from .storage import TokenMap, load_encrypted_token_map, load_token_stream, save_encrypted_token_map, save_token_stream

DEFAULT_MAX_CREDENTIAL_LENGTH = 64
DEFAULT_STORAGE_DIR = Path(__file__).resolve().parent / "encoded_files"


def encrypt_credentials(
    master_password: str,
    username: str,
    password: str,
    user_token_path: Path,
    pass_token_path: Path,
    mapping_path: Path,
    max_length: int = DEFAULT_MAX_CREDENTIAL_LENGTH,
) -> None:
    if not master_password:
        raise ValueError("Master password cannot be empty.")

    if not username and not password:
        raise ValueError("At least username or password must be provided.")

    if max_length <= 0:
        raise ValueError("max_length must be a positive integer.")

    if len(username) > max_length:
        raise ValueError("username must not exceed max_length.")
    if len(password) > max_length:
        raise ValueError("password must not exceed max_length.")

    user_tokens = [os.urandom(64) for _ in range(max_length)]
    pass_tokens = [os.urandom(64) for _ in range(max_length)]

    save_token_stream(user_token_path, user_tokens)
    save_token_stream(pass_token_path, pass_tokens)

    token_map: TokenMap = {
        user_tokens[index]: character
        for index, character in enumerate(username)
    }
    token_map.update(
        {pass_tokens[index]: character for index, character in enumerate(password)}
    )

    save_encrypted_token_map(mapping_path, token_map, master_password)


def decrypt_credentials(
    master_password: str,
    user_token_path: Path,
    pass_token_path: Path,
    mapping_path: Path,
) -> Tuple[str, str]:
    token_map = load_encrypted_token_map(mapping_path, master_password)
    user_tokens = load_token_stream(user_token_path)
    pass_tokens = load_token_stream(pass_token_path)

    return (
        _decode_sequence(user_tokens, token_map),
        _decode_sequence(pass_tokens, token_map),
    )


def _decode_sequence(tokens: List[bytes], token_map: TokenMap) -> str:
    decoded_characters: List[str] = []
    for token in tokens:
        character = token_map.get(token)
        if character is None:
            break
        decoded_characters.append(character)
    return "".join(decoded_characters)
