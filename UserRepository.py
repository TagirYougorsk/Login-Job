from uuid import UUID
from auth import create_token
from User import User
from UserDataManipulations import gender_filter, pagination, search, sort
from UserModels import LoginUserModel, ReadUserModel, RegisterUserModel, UpdateUserModel
from hash import get_password_hash, verify_password

class UserRepository:
    __users : list[User]
    
    def __init__(self):
        self.__users = []
    
    def register(self, reg_model : RegisterUserModel) -> None:
        if self.__identification(reg_model.email):
            raise Exception("Такой пользователь уже существует")
        
        self.__add(reg_model)
        
    def login(self, login_model : LoginUserModel) -> str:
        user : User = self.__authetification(login_model.email, login_model.password)
        token : str = create_token({"id" :  str(user.id)})
        return token
                  
    def __authetification(self, identificatior : str, password : str) -> User:
        user = self.__identification(identificatior)
        if not user:
            raise Exception("Такой пользователь не существует") 
        
        if not verify_password(password, user.hashed_password):
            raise Exception("Пароли не совпадают")  
        return user
        
    def __identification(self, identificator : str) -> User | None:
        for user in self.__users:
            if(user.email == identificator):
                return user
        return None
      
    def __add(self, reg_model : RegisterUserModel) -> None:
        hashed_password = get_password_hash(reg_model.password)
        print(hashed_password)
        user : User = User(reg_model.email, 
                        hashed_password, 
                        reg_model.name,
                        reg_model.surname,
                        reg_model.birthdate,
                        reg_model.gender)
        self.__users.append(user)
    
    def read(self, 
            search_value : str | None,
            filter_value : str | None,
            sort_field : str | None, 
            sort_type : int | None,
            page_size : int | None, 
            page_num : int | None) -> list[ReadUserModel]:
        """Этот метод мне нужен"""
        b0 = [ReadUserModel(
                id = user.id,
                email = user.email,
                name = user.name,
                surname = user.surname,
                birthdate = user.birthdate,
                age = user.age,
                gender = user.gender)
            for user in self.__users]
        b1 = search(b0, search_value)
        b2 = gender_filter(b1, filter_value)
        b3 = sort(b2, sort_field, sort_type)
        b4 = pagination(b3,page_size,page_num)
        return b4
    
    def read_by_id(self, id : UUID) -> ReadUserModel | None:
        for user in self.__users:
            if(user.id == id):
                return ReadUserModel(
                    id = user.id,
                    email = user.email,
                    name = user.name,
                    surname = user.surname,
                    birthdate = user.birthdate,
                    age = user.age,
                    gender = user.gender)
        raise Exception("Пользовтель не найден")
    
    def update(self, id : UUID, update_model : UpdateUserModel) -> None:
        for user in self.__users:
            if(user.id == id):
                if(update_model.email != None):
                    user.email = update_model.email 
                if(update_model.name != None):
                    user.name = update_model.name 
                if(update_model.surname != None):
                    user.surname = update_model.surname 
                if(update_model.birthdate != None):
                    user.birthdate = update_model.birthdate 
                if(update_model.password != None):
                    user.hashed_password = update_model.password
                if(update_model.gender != None):
                    user.gender = update_model.gender
        return None          
        
    def delete(self, id : UUID) -> None:
        for user in self.__users:
            if(user.id == id):
                self.__users.remove(user)
                return None
        raise Exception("Пользователь не найден")
    
    def get_gender_tags(self) -> list[str]:
        buffer : list[str] = []
        for user in self.__users:
            if(user.gender not in buffer):
                buffer.append(user.gender)
        return buffer

    
    
    
