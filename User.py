from uuid import uuid4, UUID
from datetime import datetime

class User:
    def __init__(self, email: str, hashed_password: str, name: str, surname: str,
                 birthdate: datetime, gender: str, user_id: UUID = None):
        self.id = user_id or uuid4()
        self.email = email
        self.hashed_password = hashed_password
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @property
    def age(self) -> int:
        today = datetime.today()
        return today.year - self.birthdate.year - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "email": self.email,
            "hashed_password": self.hashed_password,
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate.isoformat(),  # 'YYYY-MM-DDTHH:MM:SS'
            "gender": self.gender
        }

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            email=data["email"],
            hashed_password=data["hashed_password"],
            name=data["name"],
            surname=data["surname"],
            birthdate=datetime.fromisoformat(data["birthdate"]),
            gender=data["gender"],
            user_id=UUID(data["id"])
        )
