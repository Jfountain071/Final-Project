####################################################################
# Project Name: Clean Caddy
# Staff: Lee Wycoff, Jeremy Fountain, Andrew Finch
####################################################################
from tkinter import *               # imports everything from tkinter 
import time                         # imports time
from random_word import RandomWords # imports the function from the API
import RPi.GPIO as GPIO             # enables the usage of the Pi's GPIO ports

window = Tk()                       # defines the window using the Tk module

WIDTH = 800
HEIGHT = 480
window.geometry(f"{WIDTH}x{HEIGHT}")

r = RandomWords()
dayWord = r.word_of_the_day()       # runs the function from the API and stores the dictionary in the dayWord value

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(5, GPIO.RISING, callback=countdown)  # the event detection allows for the pin 5 to be called to the top priority when it goes high

def update_clock():
    current_time_label.config(text = "Current Time: " + time.strftime("%I:%M:%S", time.localtime()))
    window.after(1000, update_clock) # when the function update_clock is called, it continuously updates the system time
    

def countdown_initialize(count=120):            # the first countdown statement to run
    mins, secs = divmod(count, 60)
    time_format = "{:02d}:{:02d}".format(mins, secs)      # the timer in min,sec will display 2:00 on startup  
    text=f"Timer: {time_format}"
    timer_label.config(text=text)

def countdown(_=None):              # denys input from the GPIO event detection call
    count=120
    while (count > 0):          # begins the timer ticking
        time.sleep(1)
        mins, secs = divmod(count, 60)
        time_format = "{:02d}:{:02d}".format(mins, secs)         
        text=f"Timer: {time_format}"
        timer_label.config(text=text)
        count -= 1
    if count == 0:      # when the timer is at 0, it will reset to 2 minutes and not loop
        count = 120
    countdown_initialize(count)     # feeds the current count (ticking time) into the prior countdown function to be displayed
0
img = PhotoImage(file = "COES.gif") # defines what the image to be used is


GUI_data = [                        # defines what is going to be called from the dayWord dictionary to put on the GUI
{"row": 0, "rowspan": 1, "col": 0, "colspan": 6, "value": f"Word of the Day: {dayWord['word']}"},
{"row": 1, "rowspan": 1, "col": 0, "colspan": 6, "value": f"Definition: {dayWord['partOfSpeech']}, {dayWord['definitions']}"},
]                                   

GUI_data2 = [                       # defines the image to be called by the GUI and also adds a blank space to move the image over
    {"row": 2, "col": 1, "rowspan": 7, "colspan": 6, "value": PhotoImage(file="COES.gif")},
    {"row": 2, "col": 0, "rowspan": 7, "colspan": 1, "value": None}
]

USING_RPI = False

class MainGUI(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        if USING_RPI:
            master.attributes("-fullscreen", True)      # sets the GUI to fullscreen if using the Raspberry Pi
        self.setupGUI()

    def make_GUI_item(self, row, rowspan, col, colspan, value): # makes GUI items with text

        GUI_item = Label(self, text=value, anchor=W, bg="#5865F2", fg="white", height=1, font=("Times New Roman", 15), wraplength = 775, justify="left")

        GUI_item.grid(row=row, rowspan=rowspan, column=col, columnspan=colspan, sticky=NSEW)

    def make_GUI_item2(self, row, rowspan, col, colspan, value): # makes GUI items with an image

        GUI_item2 = Label(self, image=value, anchor=W, bg="#5865F2", fg="white", height=1)

        GUI_item2.grid(row=row, rowspan=rowspan, column=col, columnspan=colspan, sticky=NSEW)

    def setupGUI(self): 

        for row in range(9):
            Grid.rowconfigure(self, row, weight = 1)    # defines the amount of rows
        
        for col in range(6):
            Grid.columnconfigure(self, col, weight = 1) # defines the amount of columns

        for GUI_item in GUI_data:                       # sets up the GUI items for the dayWord dictionary
            self.make_GUI_item(GUI_item["row"], GUI_item["rowspan"], GUI_item["col"], GUI_item["colspan"], GUI_item["value"])
        
        for GUI_item2 in GUI_data2:                     # sets up the GUI items for the image and blank space
            self.make_GUI_item2(GUI_item2["row"], GUI_item2["rowspan"], GUI_item2["col"], GUI_item2["colspan"], GUI_item2["value"])

        self.pack(fill=BOTH, expand=1)

timer_label = Label(window, text = '', anchor=SE, bg="#5865F2", fg="white", height=1, font=("Times New Roman", 20))
timer_label.pack(fill=BOTH, expand=0)   # creates the label for the timer and packs it
gui = MainGUI(window)   # calls the MainGUI class to setup the GUI
window.title("The Clean Caddy")     # title of the device
current_time_label = Label(window, text = '', anchor=SE, bg="#5865F2", fg="white", height=1, font=("Times New Roman", 20))
current_time_label.pack(fill=BOTH, expand=0)    # creates the label for the clock and packs it
window.after(0, setupGPIO)      # the following calls the three functions, with a wait time of 0
window.after(0, update_clock)   # updates the system time constantly
window.after(0, countdown_initialize)   # starts the countdown function to create the timer
window.mainloop()                       # main loop for the GUI
 