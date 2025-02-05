import re

def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak: Password too short"
    if not re.search(r'[A-Z]', password):
        return "Weak: Include at least one uppercase letter"
    if not re.search(r'[0-9]', password):
        return "Weak: Include at least one digit"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Include at least one special character"
    return "Strong password"
