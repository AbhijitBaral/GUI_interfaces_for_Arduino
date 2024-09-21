#---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino 
#---------------------------------------------

import tkinter;
from pyfirmata import Arduino;

# Functions
def LedON():
    board.digital[3].write(1);
def ledOFF():
    board.digital[3].write(0);

    # Arduino board connected to serial port 3
    board = Arduino("COM3");

    # Root widget to create window
    win = tkinter.Tk();

    # initialize window with title & minimum size
    win.title("L E D");
    win.minsize(200, 60);

    #Label widget
    label = tkinter.Label(win, text="click to turn ON/OFF");
    label.grid(column=1, row=1);

    # Button widget
    ONbtn = tkinter.Button(win, bd=4, text="LED ON", command=LedON);
    ONbtn.grid(cloumn=1, row=2);
    OFFbtn = tkinter.Button(win, bd=4, text="LED OFF", command=ledOFF);
    OFFbtn.grid(column=2, row=2);

    # start & open window continously
    win.mainloop();
