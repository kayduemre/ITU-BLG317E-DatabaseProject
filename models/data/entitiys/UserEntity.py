
from flask_login import UserMixin
class UserEntity(UserMixin):
    def __init__(self, email, password, user_name="",user_last_name="",memberShip=""):
        self.id = 0
        self.account_id = 0
        self.user_name = user_name
        self.user_last_name = user_last_name
        self.email = email
        self.password = password
        self.memberShip= memberShip
    
    def is_authhenticated(self):
        pass
    @property
    def is_active(self):
        pass
    def get_id(self):
        pass

def getUser():
    pass

