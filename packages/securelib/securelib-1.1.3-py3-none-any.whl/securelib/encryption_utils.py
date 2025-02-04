from Crypto.Cipher import AES
import base64

def pad(text: str) -> bytes:
    return text.encode() + b' ' * (16 - len(text) % 16)

def encrypt(text: str, key: str) -> str:
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(text))
    return base64.b64encode(encrypted_bytes).decode()

def decrypt(encrypted_text: str, key: str) -> str:
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_text))
    return decrypted_bytes.decode().strip()
