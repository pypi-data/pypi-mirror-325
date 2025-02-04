import hashlib

def generate_sha256_hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()
