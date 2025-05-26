from uuid import UUID
from fastapi import Request, HTTPException, status
from jose import jwt
from datetime import datetime, timezone

from auth import get_key, get_algorithm

def get_token(request: Request) -> str:
    token = request.headers.get("Authorization")  # ← заглавная A
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found")
    return token

def token_validation(request: Request) -> None:
    get_user_id(request)  # ← если ошибка, то токен недействителен

def get_user_id(request: Request) -> UUID:
    token = get_token(request)

    try:
        payload = jwt.decode(token, get_key(), algorithms=[get_algorithm()])
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    expire_timestamp = payload.get("exp")
    if not expire_timestamp:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    expire_time = datetime.fromtimestamp(expire_timestamp, tz=timezone.utc)
    if expire_time < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")

    user_id = payload.get("id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User ID not found in token")

    return UUID(user_id)
