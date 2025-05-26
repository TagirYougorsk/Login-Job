import tkinter as tk
from tkinter import messagebox

# создаём главное окно
root = tk.Tk()
root.title("Форма входа")
root.geometry("350x250")
root.resizable(False, False)  # запрещаем изменение размера

# Храним пользователей
users = {}

# Основной контейнер
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Заголовок
title_label = tk.Label(frame, text="Добро пожаловать!", font=("Arial", 14, "bold"))
title_label.pack(pady=(0, 10))

# Логин
login_label = tk.Label(frame, text="Логин:", font=("Arial", 10))
login_label.pack(anchor="w")
login_entry = tk.Entry(frame, font=("Arial", 10), width=30)
login_entry.pack(pady=(0, 10))

# Пароль
password_label = tk.Label(frame, text="Пароль:", font=("Arial", 10))
password_label.pack(anchor="w")
password_entry = tk.Entry(frame, font=("Arial", 10), show="*", width=30)
password_entry.pack(pady=(0, 10))

# Обработка входа
def handle_login():
    login = login_entry.get()
    password = password_entry.get()
    if login in users and users[login] == password:
        messagebox.showinfo("Успешный вход", "✅ Вход выполнен успешно!")
    else:
        messagebox.showerror("Ошибка входа", "❌ Неверный логин или пароль.")

# Обработка регистрации
def handle_register():
    login = login_entry.get()
    password = password_entry.get()
    if login in users:
        messagebox.showwarning("Регистрация", "⚠️ Такой пользователь уже существует.")
    else:
        users[login] = password
        messagebox.showinfo("Регистрация", "✅ Регистрация успешна!")

# Кнопки
button_frame = tk.Frame(frame)
button_frame.pack(pady=(10, 0))

login_button = tk.Button(button_frame, text="Войти", command=handle_login, width=15, font=("Arial", 10))
login_button.pack(side="left", padx=5)

register_button = tk.Button(button_frame, text="Зарегистрироваться", command=handle_register, width=15, font=("Arial", 10))
register_button.pack(side="left", padx=5)

# запускаем главный цикл
root.mainloop()
