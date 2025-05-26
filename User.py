from datetime import datetime
from uuid import UUID
import uuid
from pydantic import EmailStr
from dateutil.relativedelta import relativedelta

class User:
    __id : UUID
    email : EmailStr 
    __hashed_password : str
    __name : str
    __surname : str
    __birthdate : datetime
    __gender : str
    
    def __init__(self, email: EmailStr, password: str, name: str, surname : str, birthdate : datetime, gender : str):
        self.__id = uuid.uuid4()
        self.email = email
        self.hashed_password = password
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    @property
    def id(self):
        return self.__id
    
    @property
    def age(self):
        return int((datetime.now() - self.birthdate).days / 365.2425)
    
    @property
    def hashed_password(self):
        return self.__hashed_password 
    @hashed_password.setter
    def hashed_password(self, value : str):
        self.__hashed_password = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value : str):
        self.__name = value
        
    @property
    def surname(self):
        return self.__surname
    @surname.setter
    def surname(self, value : str):
        self.__surname = value
   
    @property
    def birthdate(self):
        return self.__birthdate
    @birthdate.setter
    def birthdate(self, value : datetime):
        if(value > (datetime.now() - relativedelta(years = 18))):
            raise Exception("Вам должно быть больше 18 лет")
        self.__birthdate = value

    @property
    def gender(self): 
        return self.__gender
    @gender.setter
    def gender(self, value : str):
        if(value.lower() not in ["мужской", "женский"]):
            raise Exception("Пола всего два")
        self.__gender = value  