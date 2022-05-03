import serial
import string
from cProfile import label
from itertools import count
from tkinter import *
import time
from random_word import RandomWords

window = Tk()

WIDTH = 800
HEIGHT = 480
window.geometry(f"{WIDTH}x{HEIGHT}")
ser=serial.Serial('/dev/ttyACM0', 250000)	# Reads the serial port on the raspi, and reads at a 250000 bit rate

r = RandomWords()
dayWord = r.word_of_the_day()

def update_clock():
    current_time_label.config(text = "Current Time: " + time.strftime("%I:%M:%S", time.localtime()))
    window.after(1000, update_clock)

def countdown(count=120):
    mins, secs = divmod(count, 60)
    time_format = "{:02d}:{:02d}".format(mins, secs)         
    text=f"Timer: {time_format}"
    timer_label.config(text=text)

    if count > 0:
        window.after(1000, countdown, count-1)

img = PhotoImage(file = "COES.gif")


GUI_data = [
{"row": 0, "col": 0, "colspan": 6, "value": f"Word of the Day: {dayWord['word']}"},
{"row": 1, "col": 0, "colspan": 6, "value": f"Definition: {dayWord['partOfSpeech']}, {dayWord['definitions']}"},
]

GUI_data2 = [
    {"row": 2, "col": 1, "rowspan": 7, "colspan": 6, "value": PhotoImage(file="COES.gif")},
    {"row": 2, "col": 0, "rowspan": 7, "colspan": 1, "value": None}
]

USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)
        self.setupGUI()

    def make_GUI_item(self, row, col, colspan, value):

        GUI_item = Label(self, text=value, anchor=W, bg="#5865F2", fg="white", height=1, font=("Times New Roman", 15))

        GUI_item.grid(row=row, column=col, columnspan=colspan, sticky=NSEW)

    def make_GUI_item2(self, row, rowspan, col, colspan, value):

        GUI_item2 = Label(self, image=value, anchor=W, bg="#5865F2", fg="white", height=1)

        GUI_item2.grid(row=row, rowspan=rowspan, column=col, columnspan=colspan, sticky=NSEW)

    def setupGUI(self):

        for row in range(9):
            Grid.rowconfigure(self, row, weight = 1)
        
        for col in range(6):
            Grid.columnconfigure(self, col, weight = 1)

        for GUI_item in GUI_data:
            self.make_GUI_item(GUI_item["row"], GUI_item["col"], GUI_item["colspan"], GUI_item["value"])
        
        for GUI_item2 in GUI_data2:
            self.make_GUI_item2(GUI_item2["row"], GUI_item2["rowspan"], GUI_item2["col"], GUI_item2["colspan"], GUI_item2["value"])

        self.pack(fill=BOTH, expand=1)

timer_label = Label(window, text = '', anchor=SE, bg ="#5865F2", fg="white", height=1, font=("Times New Roman", 20))
timer_label.pack(fill=BOTH, expand=0)
gui = MainGUI(window)
window.title("Terrific Toothpaste Prototype")
current_time_label = Label(window, text = '', anchor=SE, bg ="#5865F2", fg="white", height=1, font=("Times New Roman", 20))
current_time_label.pack(fill=BOTH, expand=0)
window.after(0, update_clock)
window.after(0, countdown)

window.mainloop()