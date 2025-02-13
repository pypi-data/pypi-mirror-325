from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64
from argon2 import low_level

class EnigmaBox:
    @staticmethod
    def _derive_key(password: str, salt: bytes) -> bytes:
        """Derive a 256-bit key from the password using Argon2id."""
        return low_level.hash_secret_raw(
            secret=password.encode(),
            salt=salt,
            time_cost=50,          # Iterations (adjust based on performance/security needs)
            memory_cost=65536,    # Memory usage (64MB)
            parallelism=4,        # Parallel threads
            hash_len=32,          # Output length (256 bits)
            type=low_level.Type.ID  # Argon2id (recommended variant)
        )

    @staticmethod
    def encrypt(password: str, message: str) -> str:
        """Encrypt the message using AES-256 with the given password."""
        if not password or not message:
            raise ValueError("Password and message cannot be empty.")

        # Generate random salt and IV
        salt = os.urandom(16)
        iv = os.urandom(16)

        # Derive the key
        key = EnigmaBox._derive_key(password, salt)

        # Encrypt the message
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message.encode()) + encryptor.finalize()

        # Combine salt, IV, and ciphertext into a single output
        encrypted_data = salt + iv + ciphertext
        return base64.urlsafe_b64encode(encrypted_data).decode()  # Simplified output

    @staticmethod
    def decrypt(password: str, encrypted_message: str) -> str:
        """Decrypt the message using AES-256 with the given password."""
        if not password or not encrypted_message:
            raise ValueError("Password and encrypted message cannot be empty.")

        try:
            # Decode the base64-encoded encrypted data
            encrypted_data = base64.urlsafe_b64decode(encrypted_message)
        except Exception:
            raise ValueError("Invalid encrypted message format.")

        # Extract salt, IV, and ciphertext
        if len(encrypted_data) < 16:  # Minimum length: 16 (salt) + 16 (IV) + 16 (ciphertext)
            raise ValueError("Encrypted message is too short.")
        salt = encrypted_data[:16]
        iv = encrypted_data[16:32]
        ciphertext = encrypted_data[32:]

        # Derive the key
        key = EnigmaBox._derive_key(password, salt)

        # Decrypt the message
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        try:
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        except Exception:
            raise ValueError("Decryption failed. Check the password or encrypted message.")

        # Ensure the plaintext is valid UTF-8
        try:
            return plaintext.decode('utf-8')
        except UnicodeDecodeError:
            raise ValueError("Decrypted data is not valid UTF-8. Check the password or encrypted message.")