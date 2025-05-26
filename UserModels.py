from datetime import datetime
# import re
from uuid import UUID
from pydantic import BaseModel, EmailStr

class RegisterUserModel(BaseModel):
    email : EmailStr
    password : str
    name : str
    surname : str
    birthdate : datetime
    gender : str
    
    # @property
    # def password(self):
    #     return self.__password
    # @password.setter
    # def password(self, value : str):
    #     if(not(8 < len(value) < 20)):
    #         raise Exception("Длина пароля должна быть от 8 до 20 символов")
    #     if(not bool(re.search(r'[A-Z]', value))):
    #         raise Exception("Пароль должен содержать хотя-бы одну заглавную букву")
    #     if(not bool(re.search(r'[a-z]', value))):
    #         raise Exception("Пароль должен содержать хотя-бы одну прописную букву")
    #     if(not bool(re.search(r'\d', value))):
    #         raise Exception("Пароль должен содержать хотя-бы одну цифру")
    #     self.__password = value
    
    
class LoginUserModel(BaseModel):
    email : EmailStr
    password : str
    
class ReadUserModel(BaseModel):
    id : UUID
    email : EmailStr 
    name : str
    surname : str
    birthdate : datetime
    age : int
    gender : str
    
class UpdateUserModel(BaseModel):
    email : EmailStr | None
    name : str | None
    surname : str | None
    birthdate : datetime | None
    password : str | None
    gender : str | None
