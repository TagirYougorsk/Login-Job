from typing import Optional
from uuid import UUID
from fastapi import HTTPException, Request, Body
from fastapi_controllers import Controller
from fastapi_controllers.routing import delete, get, post, put
from InitData import init_data
from UserModels import LoginUserModel, RegisterUserModel, UpdateUserModel
from UserRepository import UserRepository
from auth import create_access_token, create_refresh_token, verify_refresh_token, revoke_refresh_token
from http_helper import token_validation


class UserController(Controller):
    user_repo = UserRepository()
    init_data(user_repo)

    @get("/users/{id}")
    def get_user(self, id: UUID):
        try:
            return self.user_repo.read_by_id(id)
        except Exception as e:
            return str(e)

    @post("/users/register")
    def register_user(self, reg_model: RegisterUserModel):
        try:
            self.user_repo.register(reg_model)
            return "Пользователь успешно создан"
        except Exception as e:
            return str(e)

    @post("/users/login")
    def login_user(self, login_model: LoginUserModel):
        try:
            # Выполнение логина и создание токенов
            tokens = self.user_repo.login(login_model)
            return tokens  # Возвращаем оба токена
        except Exception as e:
            return str(e)

    @post("/users/refresh")
    def refresh_token(self, token: str = Body(...)):
        try:
            # Обновление токена через refresh
            user_id = verify_refresh_token(token)
            new_access_token = create_access_token({"id": user_id})
            return {"access_token": new_access_token}
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))

    @post("/users/logout")
    def logout_user(self, token: str = Body(...)):
        try:
            # Отзыв refresh-токена
            revoke_refresh_token(token)
            return {"message": "Вы успешно вышли"}
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))

    @put("/users/{id}")
    def update_user(self, id: UUID, update_model: UpdateUserModel):
        try:
            self.user_repo.update(id, update_model)
            return "Пользователь успешно обновлен"
        except Exception as e:
            return e

    @delete("/users/{id}")
    def delete_user(self, id: UUID):
        try:
            self.user_repo.delete(id)
            return "Пользователь успешно удален"
        except Exception as e:
            return str(e)

    @get("/users")
    def get_users(self, request: Request, search_value: Optional[str] = None,
                  filter_value: Optional[str] = None, sort_field: Optional[str] = None,
                  sort_type: Optional[int] = None, page_size: Optional[int] = None,
                  page_num: Optional[int] = None):
        try:
            token_validation(request)  # Проверка токена в запросе
            return self.user_repo.read(search_value, filter_value, sort_field, sort_type, page_size, page_num)
        except HTTPException as e:
            return e

    @get("/get_gender_tags")
    def get_gender_tags(self):
        return self.user_repo.get_gender_tags()
