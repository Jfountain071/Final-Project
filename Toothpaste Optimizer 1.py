
from os import system
from tkinter import *
import time

WIDTH = 400
HEIGHT = 400

def update_clock():
    timer_label.config(text = time.strftime("%I:%M:%S", time.localtime()))
    window.after(1000, update_clock)

GUI_data = [
{"row": 0, "col": 0, "colspan": 3, "value": ""},
{"row": 0, "col": 3, "colspan": 3, "value": ""},
{"row": 1, "col": 0, "colspan": 2, "value": ""},
]

USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)
        self.setupGUI()

    def make_GUI_item(self, row, col, colspan, value):

        GUI_item = Label(self, text=value, anchor=CENTER, bg="white", fg="black", height=1)

        GUI_item.grid(row=row, column=col, columnspan=colspan, sticky=NSEW)

    def setupGUI(self):

        for row in range(2):
            Grid.rowconfigure(self, row, weight = 1)
        
        for col in range(6):
            Grid.columnconfigure(self, col, weight = 1)

        for GUI_item in GUI_data:
            self.make_GUI_item(GUI_item["row"], GUI_item["col"], GUI_item["colspan"], GUI_item["value"])

        self.pack(fill = BOTH, expand = 1)

window = Tk()
gui = MainGUI(window)
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Terrific Toothpaste Prototype")
timer_label = Label(window, text = '', anchor=SE, bg="white", fg="black", height = 1)
timer_label.pack(fill=BOTH, expand=1)
window.after(0, update_clock)
window.mainloop()