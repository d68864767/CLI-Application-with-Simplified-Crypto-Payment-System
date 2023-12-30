```python
# security.py

import os
from cryptography.fernet import Fernet

class Security:
    def __init__(self):
        self.key = os.getenv('CRYPTO_KEY')
        self.cipher_suite = Fernet(self.key)

    def get_api_key(self):
        """
        Retrieve the encrypted API key from the environment variables, decrypt it and return.
        """
        encrypted_api_key = os.getenv('ENCRYPTED_API_KEY')
        decrypted_api_key = self.cipher_suite.decrypt(encrypted_api_key.encode()).decode()
        return decrypted_api_key

    def encrypt_data(self, data):
        """
        Encrypt the provided data using Fernet symmetric encryption.
        """
        encrypted_data = self.cipher_suite.encrypt(data.encode())
        return encrypted_data.decode()

    def decrypt_data(self, encrypted_data):
        """
        Decrypt the provided data using Fernet symmetric encryption.
        """
        decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
        return decrypted_data.decode()
```
