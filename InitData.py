from datetime import datetime
from UserModels import RegisterUserModel
from UserRepository import UserRepository



def init_data(user_repo : UserRepository):
    #region init_data
    user_repo.register(RegisterUserModel( 
        email="1@mail.ru", 
        password="123aaaAAA", 
        name="АААААА", 
        surname="Первый",
        birthdate=datetime(1999,3,4),
        gender="Мужской"))

    user_repo.register(RegisterUserModel( 
        email="2@mail.ru", 
        password="123aaaAAA", 
        name="ЯЯЯЯЯЯЯ", 
        surname="Первый",
        birthdate=datetime(1899,3,4),
        gender="Мужской"))

    user_repo.register(RegisterUserModel( 
        email="3@mail.ru", 
        password="123aaaAAA", 
        name="ГГГГГГГ", 
        surname="Первый",
        birthdate=datetime(1989,3,4),
        gender="Мужской"))

    user_repo.register(RegisterUserModel( 
        email="4@mail.ru", 
        password="123aaaAAA", 
        name="ЖЖЖЖЖЖЖ", 
        surname="Первый",
        birthdate=datetime(1779,3,4),
        gender="Мужской"))

    user_repo.register(RegisterUserModel( 
        email="5@mail.ru", 
        password="123aaaAAA", 
        name="ВВВВВВВВ", 
        surname="Первый",
        birthdate=datetime(1777,3,4),
        gender="Женский"))

    user_repo.register(RegisterUserModel( 
        email="6@mail.ru", 
        password="123aaaAAA", 
        name="ЛЛЛЛЛЛЛЛЛ", 
        surname="Первый",
        birthdate=datetime(2005,3,4),
        gender="Женский"))

    user_repo.register(RegisterUserModel( 
        email="7@mail.ru", 
        password="123aaaAAA", 
        name="МММММММММ", 
        surname="Первый",
        birthdate=datetime(2001,3,4),
        gender="Женский"))

    user_repo.register(RegisterUserModel( 
        email="8@mail.ru", 
        password="123aaaAAA", 
        name="НННННННННН", 
        surname="Первый",
        birthdate=datetime(2002,3,4),
        gender="Женский"))

    user_repo.register(RegisterUserModel( 
        email="9@mail.ru", 
        password="123aaaAAA", 
        name="КККККККК", 
        surname="Первый",
        birthdate=datetime(2003,3,4),
        gender="Женский"))

    user_repo.register(RegisterUserModel( 
        email="10@mail.ru", 
        password="123aaaAAA", 
        name="ААААААААА", 
        surname="Первый",
        birthdate=datetime(2003,3,4),
        gender="Женский"))
    #endregion`