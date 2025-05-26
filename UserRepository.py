from uuid import UUID
from auth import create_access_token, create_refresh_token, verify_refresh_token, revoke_refresh_token
from User import User
from UserModels import LoginUserModel, RegisterUserModel, UpdateUserModel, ReadUserModel
from hash import get_password_hash, verify_password
from typing import Optional

class UserRepository:
    __users: list[User]
    
    def __init__(self):
        self.__users = []
    
    def register(self, reg_model: RegisterUserModel) -> None:
        """Регистрирует нового пользователя"""
        if self.__identification(reg_model.email):
            raise Exception("Такой пользователь уже существует")
        
        self.__add(reg_model)
    
    def login(self, login_model: LoginUserModel) -> dict:
        """Процесс авторизации пользователя. Возвращает access и refresh токены"""
        user = self.__authetification(login_model.email, login_model.password)
        access_token = create_access_token({"id": str(user.id)})
        refresh_token = create_refresh_token(user.id)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

    def __authetification(self, identificatior: str, password: str) -> User:
        """Проверяет правильность данных для авторизации"""
        user = self.__identification(identificatior)
        if not user:
            raise Exception("Такой пользователь не существует") 
        
        if not verify_password(password, user.hashed_password):
            raise Exception("Пароли не совпадают")  
        return user
        
    def __identification(self, identificator: str) -> User | None:
        """Ищет пользователя по идентификатору"""
        for user in self.__users:
            if user.email == identificator:
                return user
        return None

    def __add(self, reg_model: RegisterUserModel) -> None:
        """Добавляет нового пользователя"""
        hashed_password = get_password_hash(reg_model.password)
        user = User(
            email=reg_model.email, 
            hashed_password=hashed_password, 
            name=reg_model.name,
            surname=reg_model.surname,
            birthdate=reg_model.birthdate,
            gender=reg_model.gender
        )
        self.__users.append(user)
    
    def read(self, search_value: Optional[str], filter_value: Optional[str], sort_field: Optional[str],
             sort_type: Optional[int], page_size: Optional[int], page_num: Optional[int]) -> list[ReadUserModel]:
        """Метод для получения списка пользователей с возможностью фильтрации и сортировки"""
        users_list = [
            ReadUserModel(
                id=user.id,
                email=user.email,
                name=user.name,
                surname=user.surname,
                birthdate=user.birthdate,
                age=user.age,
                gender=user.gender
            )
            for user in self.__users
        ]
        # Здесь можно добавить логику фильтрации, сортировки и пагинации
        return users_list
    
    def read_by_id(self, id: UUID) -> ReadUserModel | None:
        """Получение пользователя по ID"""
        for user in self.__users:
            if user.id == id:
                return ReadUserModel(
                    id=user.id,
                    email=user.email,
                    name=user.name,
                    surname=user.surname,
                    birthdate=user.birthdate,
                    age=user.age,
                    gender=user.gender
                )
        raise Exception("Пользователь не найден")
    
    def update(self, id: UUID, update_model: UpdateUserModel) -> None:
        """Обновление данных пользователя"""
        for user in self.__users:
            if user.id == id:
                if update_model.email:
                    user.email = update_model.email 
                if update_model.name:
                    user.name = update_model.name 
                if update_model.surname:
                    user.surname = update_model.surname 
                if update_model.birthdate:
                    user.birthdate = update_model.birthdate 
                if update_model.password:
                    user.hashed_password = get_password_hash(update_model.password)
                if update_model.gender:
                    user.gender = update_model.gender
                return
        raise Exception("Пользователь не найден")

    def delete(self, id: UUID) -> None:
        """Удаление пользователя"""
        for user in self.__users:
            if user.id == id:
                self.__users.remove(user)
                return
        raise Exception("Пользователь не найден")
    
    def get_gender_tags(self) -> list[str]:
        """Получение всех уникальных тегов гендера среди пользователей"""
        return list(set(user.gender for user in self.__users))
