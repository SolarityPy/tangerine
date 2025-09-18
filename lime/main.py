import lime, platform, os, subprocess, ctypes, sys, requests
import lime.widgets as widgets
from typing import Callable
from pygame import freetype
from lime.util import *

class Checkbox(widgets.BaseWidget):
    """Draws a checkbox

    :param text: Checkbox text label
    :type text: str
    :param checked: If the checkbox is checked by default
    :type checked: bool, optional
    :param locked: If the checkbox is locked
    :type locked: bool, optional
    :param fontsize: Fontsize of label
    :type fontsize: int, optional
    :param fg_color: The color of the label
    :type fg_color: Color, optional
    :param border_color: The color of the border
    :type border_color: Color, optional
    :param check_color: The color of the check
    :type check_color: Color, optional
    """
    def __init__(self, text: str, checked: bool = False, locked: bool = False, fontsize: int = 14, fg_color = Color.foreground(), border_color: Color = None, check_color: Color = None, bold: bool = False, italic: bool = False, underline: bool = False):
        """Creates a new Checkbox
        """
        self.text = text
        self.fg_color = fg_color
        self.border_color = border_color if border_color else Color(63, 67, 71)
        self.check_color = check_color if check_color else Color.primary()
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.text_size = Vector(0, 0)
        self.padding = 7
        self.fontsize = fontsize
        self.checked = checked
        self.locked = locked
        self._hovered = False
        self._handlers = []

        super().__init__(Vector(0, 0))

    def get_freetype_style(self):
        return freetype.STYLE_NORMAL | (freetype.STYLE_STRONG if self.bold else 0) | (freetype.STYLE_OBLIQUE if self.italic else 0) | (freetype.STYLE_UNDERLINE if self.underline else 0)

    def render(self, draw):
        if self._hovered:
            draw.circle(Vector(self.size.h // 2, self.size.h // 2), self.size.h // 2, color=Color(255, 255, 255, 10))
        draw.circle_outline(Vector(self.size.h // 2, self.size.h // 2), self.size.h // 2, color=self.border_color)
        draw.text(Vector(self.size.h + self.padding, 3), self.text, self.fontsize, color=self.fg_color, bold=self.bold, underline=self.underline, italic=self.italic)
        
        if self.checked:      
            draw.line_strip([
                Vector(self.size.h // 20 * 3, self.size.h // 2),
                Vector(self.size.h // 5 * 2, self.size.h // 4 * 3),
                Vector(self.size.h // 5 * 4, self.size.h // 4)
            ], color=self.check_color, width=3)

    def calculate(self):
        rect = Font.get(self.fontsize).get_rect(self.text, style=self.get_freetype_style())
        self.text_size = Vector(rect.w, rect.h)
        self.size = Vector(
            self.fontsize + self.padding + rect.w + 6,
            self.fontsize + 6
        )

    def on_change(self, cb: Callable[[bool], ...]):
        self._handlers.append(cb)

    def remove_handler(self, cb: Callable[[bool], ...]):
        handlers = []
        for handler in self._handlers:
            if handler == cb:
                continue
            handlers.append(handlers)
        self._handlers = handlers

    def get_areas(self):
        area = widgets.InteractionArea(Vector(0, 0), Vector(16, 16))

        def click(_, _v):
            self.checked = not self.checked
            for handler in self._handlers:
                handler(self.checked)

        def enter(_, _v):
            if self.locked: return "NOT_ALLOWED"
            self._hovered = True
            return "POINTING_HAND"
        
        def exit(_):
            self._hovered = False

        if not self.locked: area.on_click(click)
        area.on_enter(enter, exit)
        return [(self, [area])]
    
    def hash(self):
        return f"{self.text},{self.fg_color},{self.border_color},{self.check_color},{self.locked},{self.fontsize}"


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
    
    checkbox = Checkbox("Something idk")
    
    analyze_system = widgets.Button("Analyze System", 300, bg_color=Color(255, 140, 0))
    analyze_system.on_click(analyze_system_function)
    install_tools = widgets.Button("Install Tools", 300, bg_color=Color(255, 140, 0))
    
    win.add_next([title, os_version, user, checkbox], gap=10)
    #win.add_next([analyze_system], gap=20)
    win.add(50, win._real_height + 5, analyze_system)