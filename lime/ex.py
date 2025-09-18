import lime
import lime.widgets as widgets
from lime.util import *

@lime.register("basic", default=True)
def window():
    return lime.create(
        "Basic Window",
        400,
        300,
        pos=Vector(500, 70)
    )

# TODO: find use case for this (in example)
# @lime.action
# def 

@lime.init("basic")
def init(win: lime.Window):
    button_header = widgets.Text("Buttons", 0, 18, bold=True, auto_width=True)
    button1 = widgets.Button("This button does nothing!", 300)
    button2 = widgets.Button("This button changes it's own color!", 300)
    button3 = widgets.Button("This button only works once!", 300)
    button4 = widgets.Button("This button is disabled.", 300, disabled=True)

    def button2_click(_):
        button2.bg_color += (9, 6, 3)
        button2.bg_color %= 256

        if sum(button2.bg_color) > 500 or (max(*button2.bg_color) > 200 and min(*button2.bg_color) < 100):
            button2.fg_color = Color(5, 5, 5)
        else:
            button2.fg_color = Color.foreground()

    button2.on_click(button2_click) 

    def button3_click(_):
        button3.disabled = True

        def button1_click(_):
            button_header.text = "I like buttons!"
            button1.text = "This button does nothing!"
            button1.remove_handler(button1_click)

        button1.on_click(button1_click)

        button1.text = "This button does something now!"

    button3.on_click(button3_click)

    win.add_next([button_header, button1, button2, button3, button4])

    check_header = widgets.Text("Checkboxes", 0, 18, bold=True, auto_width=True)
    check1 = widgets.Checkbox("Test checkbox!")
    check2 = widgets.Checkbox("Big checkbox!", fontsize=20)
    check3 = widgets.Checkbox("This one don't work", locked=True)
    check4 = widgets.Checkbox("This only works once.", italic=True)

    def check4_change(_):
        check4.locked = True

    check4.on_change(check4_change)

    win.add_next([check_header, check1, check2, check3, check4])

    input_header = widgets.Text("Inputs", 0, 18, bold=True, auto_width=True)
    input1 = widgets.Input("Text Input", 300, max_char=30, default="Placeholder")
    input2 = widgets.NumberInput("Number Input", 300)
    input3 = widgets.NumberInput("Number (75-100)", 300, min=75, max=100, floating=False)
    input4 = widgets.OptionInput("Favorite Color in Rainbow", 300, options=[
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Indigo",
        "Violet"
    ])
    input5 = widgets.Input("Disabled Input", 300, max_char=30, default="Changeme!", disabled=True)
    input6 = widgets.FileInput("Image Input", 300, dir="", extension=["png", "jpg", "jpeg", "svg"])

    def input6_change(_, valid):
        print("valid!!" if valid else "invalid", input6.value)

    input6.on_change(input6_change)

    win.add_next([input_header, input1, input2, input3, input4, input5, input6])

    misc_header = widgets.Text("Misc", 0, 18, bold=True, auto_width=True)
    popup = widgets.Button("Open a popup!", 300)

    def popup_click(_):
        lime.open_window("popup", "basic")

    popup.on_click(popup_click)

    win.add_next([misc_header, popup])

@lime.register("popup")
def window_popup():
    return lime.create(
        "Popup",
        100,
        300,
        pos = "center" # or you could specify Vector()
    )

@lime.init("popup")
def init_popup(win: lime.Window):
    win.add_next(widgets.Text("Was good!", 100, 14))