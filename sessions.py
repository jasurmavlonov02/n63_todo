from models import User

class Session:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(Session,cls).__new__(cls)
        return cls._instance
    
    def __init__(self,session : User | None = None):
        if not hasattr(self, 'session'):
            self.session = session
        
    def check_session(self):
        return self.session
    
    def add_session(self,user:User):
        self.session = user
        
    def remove_session(self):
        self.session = None
        
        
