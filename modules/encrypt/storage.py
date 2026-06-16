from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Iterable, List

from .cipher import AesGcmCipher

TOKEN_SIZE = 64

TokenMap = dict[bytes, str]


def save_token_stream(path: Path, tokens: Iterable[bytes], token_size: int = TOKEN_SIZE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    token_bytes = b"".join(_validate_token(token, token_size) for token in tokens)
    path.write_bytes(token_bytes)


def load_token_stream(path: Path, token_size: int = TOKEN_SIZE) -> List[bytes]:
    if not path.exists():
        raise FileNotFoundError(f"Token stream not found: {path}")

    raw_bytes = path.read_bytes()
    if len(raw_bytes) % token_size != 0:
        raise ValueError(f"Token stream has invalid length: {path}")

    return [raw_bytes[i : i + token_size] for i in range(0, len(raw_bytes), token_size)]


def save_encrypted_token_map(path: Path, mapping: TokenMap, master_password: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    records = [
        {"token": base64.b64encode(token).decode("ascii"), "character": character}
        for token, character in mapping.items()
    ]
    plaintext = json.dumps(records, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    path.write_bytes(AesGcmCipher.encrypt(plaintext, master_password))


def load_encrypted_token_map(path: Path, master_password: str) -> TokenMap:
    if not path.exists():
        raise FileNotFoundError(f"Encrypted mapping not found: {path}")

    encrypted_blob = path.read_bytes()
    plaintext = AesGcmCipher.decrypt(encrypted_blob, master_password)
    records = json.loads(plaintext)
    return {
        base64.b64decode(record["token"]): record["character"]
        for record in records
    }


def _validate_token(token: bytes, token_size: int) -> bytes:
    if not isinstance(token, (bytes, bytearray)):
        raise TypeError("Each token must be bytes.")
    if len(token) != token_size:
        raise ValueError(f"Each token must be exactly {token_size} bytes.")
    return bytes(token)
