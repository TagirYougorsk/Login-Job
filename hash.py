import hashlib

def get_password_hash(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    hashed_plain_password = get_password_hash(plain_password)
    return hashed_password == hashed_plain_password
