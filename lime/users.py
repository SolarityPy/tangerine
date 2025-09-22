from base import Base
import wmi

class Users(Base):
    def __init__(self):
        super().__init__()
    
    def check_status_client(self):
        w = wmi.WMI()
        for user_object in w.Win32_UserAccount(["Name"]):
            print(user_object.name)
            
        return "67"

