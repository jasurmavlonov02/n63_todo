# Hash pw 

from passlib.hash import pbkdf2_sha256

# password = 'admin123'

# hashed = pbkdf2_sha256.hash(password)

# print(hashed)

def hash_password(raw_password:str | None = None) -> str:
    assert raw_password, 'Raw Password Cannot be None'
    hashed_password = pbkdf2_sha256.hash(raw_password)
    return hashed_password

def match_password(raw_password : str,encoded_password : str):
    assert raw_password , 'Raw Password cannot be none'
    assert encoded_password , 'Encoded Password cannot be none'
    is_correct = pbkdf2_sha256.verify(raw_password,encoded_password)
    return is_correct



class Response:
    def __init__(self,message : str , status_code = 200):
        self.message = message
        self.status_code = status_code