import hashlib
import hmac

def generate_signature(data: str, key: str) -> str:
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

def verify_signature(data: str, key: str, signature: str) -> bool:
    return generate_signature(data, key) == signature
