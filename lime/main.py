import lime, platform, os, subprocess, ctypes, sys, requests
import lime.widgets as widgets
from lime.util import *

@lime.register("tangerine", default=True)
def tangerine():
    return lime.create(
        "Tangerine",
        400,
        400,
        pos=Vector(1520, 0)
    )
    
@lime.register("analyze_system")
def analyze_system():
    return lime.create(
        "Analyze System",
        400,
        200,
        pos=Vector(1520, 425)
    )

def cmd_output(cmd):
    return str(subprocess.check_output(cmd, shell=True, text=True)).strip()

def analyze_system_function(widget):
    lime.open_window("analyze_system", "tangerine")

@lime.init("tangerine")
def init(win: lime.Window):
    title = widgets.Text("OS Info", 0, 18, bold=True, auto_width=True)
    os_version = widgets.Text(platform.platform(), 0, 14, auto_width=True)
    user = widgets.Text("Logged in as " + cmd_output("whoami").split("\\")[1], 0, 14, auto_width=True)
    
    
    analyze_system = widgets.Button("Analyze System", 300, bg_color=Color(255, 140, 0))
    analyze_system.on_click(analyze_system_function)
    install_tools = widgets.Button("Install Tools", 300, bg_color=Color(255, 140, 0))
    
    win.add_next([title, os_version, user], gap=10)
    #win.add_next([analyze_system], gap=20)
    win.add(50, win._real_height + 5, analyze_system)