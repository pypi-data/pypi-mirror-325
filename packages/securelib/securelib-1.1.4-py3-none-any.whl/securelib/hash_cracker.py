import hashlib

def crack_hash(target_hash: str, wordlist: list) -> str:
    for word in wordlist:
        if hashlib.sha256(word.encode()).hexdigest() == target_hash:
            return word
    return "Not found"
