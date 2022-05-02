
from dataclasses import dataclass
from os import system
from tkinter import *
import time
from random_word import RandomWords

window = Tk()

WIDTH = 800
HEIGHT = 480
window.geometry(f"{WIDTH}x{HEIGHT}")

r = RandomWords()
dayWord = r.word_of_the_day()

def update_clock():
    timer_label.config(text = time.strftime("%I:%M:%S", time.localtime()))
    window.after(1000, update_clock)

img = PhotoImage(file = "COES.gif")


GUI_data = [
{"row": 0, "col": 0, "colspan": 3, "value": f"Word of the Day: {dayWord['word']}"},
{"row": 0, "col": 3, "colspan": 3, "value": ""},
{"row": 1, "col": 0, "colspan": 3, "value": f"Definition: {dayWord['partOfSpeech']}, {dayWord['definitions']}"},
]

GUI_data2 = [
    {"row": 2, "col": 0, "rowspan": 3, "colspan": 3, "value": PhotoImage(file="COES.gif")},
]

USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)
        self.setupGUI()

    def make_GUI_item(self, row, col, colspan, value):

        GUI_item = Label(self, text=value, anchor=CENTER, bg="white", fg="black", height=1, font=("Times New Roman", 15))

        GUI_item.grid(row=row, column=col, columnspan=colspan, sticky=NSEW)

    def make_GUI_item2(self, row, rowspan, col, colspan, value):

        GUI_item2 = Label(self, image=value, anchor=CENTER, bg="white", fg="black", height=2)

        GUI_item2.grid(row=row, rowspan=rowspan, column=col, columnspan=colspan, sticky=NSEW)

    def setupGUI(self):

        for row in range(5):
            Grid.rowconfigure(self, row, weight = 1)
        
        for col in range(6):
            Grid.columnconfigure(self, col, weight = 1)

        for GUI_item in GUI_data:
            self.make_GUI_item(GUI_item["row"], GUI_item["col"], GUI_item["colspan"], GUI_item["value"])
        
        for GUI_item2 in GUI_data2:
            self.make_GUI_item2(GUI_item2["row"], GUI_item2["rowspan"], GUI_item2["col"], GUI_item2["colspan"], GUI_item2["value"])

        self.pack(fill = BOTH, expand = 1)

gui = MainGUI(window)
window.title("Terrific Toothpaste Prototype")
timer_label = Label(window, text = '', anchor=SE, bg="white", fg="black", height = 1, font=("Times New Roman", 20))
timer_label.pack(fill=BOTH, expand=1)
window.after(0, update_clock)
window.mainloop()