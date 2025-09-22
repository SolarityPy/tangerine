import subprocess, platform, os
from datetime import datetime

class Base:
    def __init__(self) -> None:
        self.os_type = "server" if "server" in platform.release().lower() else "client"

    def cmd_output(self, cmd : list[str]): # Override only if needed for Active Directory Module
        try:
            return str(subprocess.check_output(cmd, shell=True, text=True)).strip()
        except Exception as E:
            self.log()
            
    def powershell_output(self, cmd : list[str]):
        cmd = ["powershell", "-Command"] + cmd
        return self.cmd_output(cmd)
        
    def check_status(self):
        if self.os_type == "server":
            return self.check_status_server()
        else:
            return self.check_status_client()
    
    def check_status_server(self):
        pass
    
    def check_status_client(self):
        pass
    
    def run_script(self):
        if self.os_type == "server":
            return self.run_script_server()
        else:
            return self.run_script_client()
    
    def run_script_server(self):
        pass
    
    def run_script_client(self):
        pass
    
    def log(self, type, message : str, exception : Exception = None):
        os.makedirs("C:/tangerine", exist_ok=True)
        with open("C:/tangerine/log.txt", "a") as fp:
            if exception or type == "error":
                fp.write(f"{datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")} {type.upper()}: {exception.__name__} - {message}")
            else:
                fp.write(f"{datetime.now().strftime("[%Y-%m-%d][%H:%M:%S]")} {type.upper()}: {message}")