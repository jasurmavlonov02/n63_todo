from enum import Enum
from datetime import datetime

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

class TodoType(Enum):
    PERSONAL = "personal"
    WORK = "work"
    SHOPPING = "shopping"
    OTHER = "other"



class User:
    def __init__(self,
                 username:str,
                 password:str,
                 email:str | None = None,
                 role : UserRole | None = None,
                 user_id : int | None = None,
                 login_try_count : int | None = None
                 ):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role or UserRole.USER.value
        self.email = email
        self.login_try_count = login_try_count or 0
    
    def __str__(self):
        return self.username
    
    @staticmethod
    def from_tuple(data:tuple):
        return User(
            user_id = data[0],
            username = data[1],
            password = data[2],
            email = data[3],
            role = data[4],
            login_try_count= data[5]
        
        )
    
    
class Todo:
    def __init__(self,
                 title : str,
                 description : str | None = None,
                 todo_type : TodoType | None = None,
                 created_at : datetime | None = None,
                 user_id : int | None  = None,
                 todo_id : int | None = None
                 ):
        self.id = todo_id
        self.title = title
        self.description = description
        self.todo_type = todo_type or TodoType.PERSONAL.value
        self.user_id = user_id
        self.created_at = created_at or datetime.now()