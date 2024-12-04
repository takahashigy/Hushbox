import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode


class EncryptionManager:
    def __init__(self, salt_file="salt.bin"):
        self.salt_file = salt_file
        self.salt = self.load_or_generate_salt()
        self.key = None

    def load_or_generate_salt(self):
        """Load or generate a cryptographic salt."""
        if os.path.exists(self.salt_file):
            # Check if the file size is correct (16 bytes)
            if os.path.getsize(self.salt_file) == 16:
                with open(self.salt_file, "rb") as f:
                    return f.read()
            else:
                print("Warning: salt.bin file is corrupted or invalid. Regenerating salt...")

        # Generate a new salt if the file is missing or invalid
        salt = os.urandom(16)
        with open(self.salt_file, "wb") as f:
            f.write(salt)
        return salt

    def derive_key(self, master_password):
        """Derive a strong encryption key from the master password."""
        if isinstance(master_password, str):
            master_password = master_password.encode('utf-8')  # Ensure consistent encoding
        kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(master_password)

    def set_master_password(self, master_password):
        """Set the master password and derive the encryption key."""
        self.key = self.derive_key(master_password)

    def encrypt(self, plaintext):
        """Encrypt plaintext using AES-256."""
        try:
            iv = os.urandom(16)  # Initialization vector
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()

            # PKCS7 padding
            padder = PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()

            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            # Combine IV and ciphertext, then encode them to a base64 string
            return urlsafe_b64encode(iv + ciphertext).decode('utf-8')
        except Exception as e:
            raise ValueError(f"Encryption failed: {e}")

    def decrypt(self, encrypted_data):
        """Decrypt encrypted data using AES-256."""
        try:
            # Decode base64 to retrieve IV and ciphertext
            encrypted_data = urlsafe_b64decode(encrypted_data)
            iv = encrypted_data[:16]  # First 16 bytes are the IV
            ciphertext = encrypted_data[16:]  # Remaining bytes are the ciphertext

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            # Decrypt and remove PKCS7 padding
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_data) + unpadder.finalize()

            return plaintext.decode('utf-8')  # Decode to a string
        except Exception as e:
            raise ValueError(f"Decryption failed: {e}")
