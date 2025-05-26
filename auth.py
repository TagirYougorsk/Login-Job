from jose import jwt # type: ignore
from datetime import datetime, timedelta, timezone

def get_key():
    return "gV64m9aIzFG4qpgVphvQbPQrtAO0nM-7YwwOvu0XPt5KJOjAy4AfgLkqJXYEt"

def get_algorithm():
    return "HS256"

#Проблемы с форматами данных, невозможно грамотно поработать с временем жизни
def create_token(data: dict) -> str:
    expire : datetime = datetime.now(timezone.utc) + timedelta(minutes=15)
    data.update({"exp": expire.strftime('%s')})
    encode_jwt : str = jwt.encode(data, get_key(), get_algorithm())
    return encode_jwt