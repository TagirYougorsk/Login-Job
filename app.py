from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime

from UserRepository import UserRepository
from UserModels import RegisterUserModel, LoginUserModel

app = FastAPI()

# Указываем папку с HTML-шаблонами
templates = Jinja2Templates(directory="templates")

# Если есть папка со static-файлами (CSS, JS, изображения) — подключаем
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Инициализация репозитория пользователей
user_repo = UserRepository()

# Главная страница — форма входа
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Страница регистрации
@app.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# Обработка формы регистрации
@app.post("/register")
def register_user(
    email: str = Form(...),
    password: str = Form(...),
    name: str = Form(...),
    surname: str = Form(...),
    birthdate: str = Form(...),  # формат: YYYY-MM-DD
    gender: str = Form(...)
):
    try:
        birthdate_dt = datetime.strptime(birthdate, "%Y-%m-%d")
        reg_model = RegisterUserModel(
            email=email,
            password=password,
            name=name,
            surname=surname,
            birthdate=birthdate_dt,
            gender=gender
        )
        user_repo.register(reg_model)
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        return {"error": str(e)}

# Обработка формы входа
@app.post("/login")
def login_user(
    email: str = Form(...),
    password: str = Form(...)
):
    try:
        login_model = LoginUserModel(email=email, password=password)
        token = user_repo.login(login_model)
        return {"access_token": token}
    except Exception as e:
        return {"error": str(e)}
