from base import Base

class Firewall(Base):
    def __init__(self):
        super().__init__()

    def check_status(self) -> str: # Same way to check on Server and on Windows -> Efficiency
        return ("ON" if super().cmd_output(["netsh", "advfirewall", "show", "allprofiles", "state"]).lower().count("on") == 3 else "OFF")
    
    def run_script(self): # Same way to check on Server and on Windows -> Efficiency
        if self.check_status() == "ON":
            return 0
        else:
            super().cmd_output(["netsh", "advfirewall", "set", "allprofiles", "state", "on"])
            