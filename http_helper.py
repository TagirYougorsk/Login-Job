from uuid import UUID
from fastapi import Request, HTTPException, status
from jose import jwt
from datetime import datetime, timezone

from auth import get_algorithm, get_key

def get_token(request: Request) -> str:
    token = request.headers.get("authorization")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found')
    return token

def token_validation(request : Request) -> None:
    get_user_id(request)

def get_user_id(request : Request) -> UUID:
    token : str = get_token(request)
    payload = jwt.decode(token, get_key(), get_algorithm())

    expire = payload.get('exp')
    if not expire: 
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен не валидный!')
    
    expire_time = datetime.strptime(expire, '%y/%m/%d %H:%M:%S')
    if expire_time < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Токен истек')

    user_id = payload.get('id')
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Не найден ID пользователя')

    return UUID(user_id)