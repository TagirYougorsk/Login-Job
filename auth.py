#from jose import jwt # type: ignore
#from datetime import datetime, timedelta, timezone
#
#def get_key():
#    return "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt"
#
#def get_algorithm():
#    return "HS256"
#
##Проблемы с форматами данных, невозможно грамотно поработать с временем жизни
#def create_token(data: dict) -> str:
#    expire : datetime = datetime.now(timezone.utc) + timedelta(minutes=15)
#    data.update({"exp": expire.strftime('%s')})
#    encode_jwt : str = jwt.encode(data, get_key(), get_algorithm())
#    return encode_jwt

from datetime import datetime, timedelta, timezone
from jose import jwt
from uuid import UUID
import secrets

SECRET_KEY = "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEty"  # Заменить на настоящий ключ
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# Хранилище refresh-токенов (можно заменить на БД)
refresh_tokens_store = {}

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(user_id: UUID) -> str:
    token = secrets.token_hex(32)
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_tokens_store[token] = {"user_id": str(user_id), "exp": expire}
    return token

def verify_refresh_token(token: str) -> str:
    data = refresh_tokens_store.get(token)
    if not data:
        raise Exception("Refresh-токен не действителен")
    if data["exp"] < datetime.now(timezone.utc):
        del refresh_tokens_store[token]
        raise Exception("Refresh-токен истёк")
    return data["user_id"]

def revoke_refresh_token(token: str) -> None:
    refresh_tokens_store.pop(token, None)

def get_algorithm() -> str:
    return ALGORITHM

def get_key() -> str:
    return SECRET_KEY
