

class IUser:
    sessionID = ""


class User(IUser):
    id = -1
    name = ""
    hashedPassword = ""

    def __init__(self, sessionId: str, name: str, password: str):
        super().__init__()
        self.sessionID = sessionId
        self.name = name
        self.password = password
        

    def hash_user_password(self):
        
    