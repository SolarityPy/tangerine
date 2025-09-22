import lime, platform, os, subprocess, ctypes, sys, requests
sys.path.append(os.path.dirname(__file__))
import lime.widgets as widgets
from firewall import Firewall
from lime.util import *
from system import System

@lime.register("tangerine", default=True)
def tangerine():
    return lime.create(
        "Tangerine",
        400,
        200,
        pos=Vector(1520, 0)
    )
    
@lime.register("analyze_system")
def analyze_system():
    return lime.create(
        "Analyze System",
        400,
        200,
        pos=Vector(1520, 225)
    )

def analyze_system_function(widget):
    @lime.init("analyze_system")
    def init_system(win: lime.Window):
        system = System()
        system_statuses = system.analyze_system()
        firewall_status = system_statuses["firewall_status"] # Firewall Status: ON
        
        firewall_text = widgets.Text(f"Firewall Status: {firewall_status}", 0, 15, bold=False, auto_width=True, centered=True)
        win.add_next([firewall_text], gap=10)
    lime.open_window("analyze_system")
    

@lime.init("tangerine")
def init(win: lime.Window):
    title = widgets.Text("Welcome to Tangerine!", 0, 20, bold=True, auto_width=True, centered=True)
    os_version = widgets.Text(platform.platform(), 0, 16, auto_width=True, centered=True)
    
    analyze_system = widgets.Button("Analyze System", 300, bg_color=Color(255, 140, 0))
    analyze_system.on_click(analyze_system_function)
    install_tools = widgets.Button("Install Tools", 300, bg_color=Color(255, 140, 0))
    
    win.add_next([title, os_version], gap=10)
    win.add(win._pane_size.w / 2 - 150, win._real_height + 10, analyze_system)