from __future__ import annotations

import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AesGcmCipher:
    SALT_SIZE = 16
    IV_SIZE = 12
    KEY_SIZE = 32
    PBKDF2_ITERATIONS = 600_000

    @staticmethod
    def derive_key(master_password: str, salt: bytes) -> bytes:
        if not master_password:
            raise ValueError("Master password cannot be empty.")

        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=AesGcmCipher.KEY_SIZE,
            salt=salt,
            iterations=AesGcmCipher.PBKDF2_ITERATIONS,
            backend=default_backend(),
        )
        return kdf.derive(master_password.encode("utf-8"))

    @classmethod
    def encrypt(cls, plaintext: bytes, master_password: str) -> bytes:
        salt = os.urandom(cls.SALT_SIZE)
        iv = os.urandom(cls.IV_SIZE)
        key = cls.derive_key(master_password, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return salt + iv + encryptor.tag + ciphertext

    @classmethod
    def decrypt(cls, encrypted_blob: bytes, master_password: str) -> bytes:
        if len(encrypted_blob) < cls.SALT_SIZE + cls.IV_SIZE + 16:
            raise ValueError("Encrypted payload is too short.")

        salt_start = 0
        salt_end = cls.SALT_SIZE
        iv_end = salt_end + cls.IV_SIZE
        tag_end = iv_end + 16

        salt = encrypted_blob[salt_start:salt_end]
        iv = encrypted_blob[salt_end:iv_end]
        tag = encrypted_blob[iv_end:tag_end]
        ciphertext = encrypted_blob[tag_end:]

        key = cls.derive_key(master_password, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
