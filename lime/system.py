from firewall import Firewall
from users import Users
class System:
    def __init__(self): # self = this
        pass
    
    def analyze_system(self):
        users = Users()
        firewall = Firewall()
        print(users.check_status())
        return {
            "firewall_status": firewall.check_status(),
            "users_list": users.check_status()
        }
