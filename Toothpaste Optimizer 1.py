
from tkinter import *
from time import *
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%I:%M")
print(current_time)

GUI_data = [
    {"row": 0, "col": 0, "colspan": 3, "value": ""},
    {"row": 0, "col": 3, "colspan": 3, "value": ""},
    {"row": 1, "col": 0, "colspan": 2, "value": ""},
    {"row": 1, "col": 5, "colspan": 1, "value": current_time}
]

USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)
        self.setupGUI()

    def setupGUI():
        pass

#window = Tk()
#window.title("Toothpaste Optimization Prototype")

#window.mainloop()