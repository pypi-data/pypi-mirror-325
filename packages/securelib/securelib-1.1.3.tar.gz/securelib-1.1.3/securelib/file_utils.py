from Crypto.Cipher import AES

def pad(data: bytes) -> bytes:
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(file_path: str, key: str) -> None:
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = cipher.encrypt(pad(data))
    with open(file_path + '.enc', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path: str, key: str) -> None:
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data).rstrip(b' ')
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
