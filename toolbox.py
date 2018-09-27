#!/usr/bin/python
import sys
import os
from tkinter import *
from tkinter.ttk import *

class toolboxGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Quick Script Access")
        
        self.clean_button = Button(master, text="Clean Desktop", command=self.cleanDesktop)
        self.spoof_button = Button(master, text="Change BSSID", command=self.spoofMAC)
        self.clear_button = Button(master, text="Clear Terminal", command=self.clearTerminal)
        self.close_button = Button(master, text="Exit Toolbox", command=master.quit)
        
        self.clean_button.grid(row=2, column=1)
        self.spoof_button.grid(row=2, column=2)
        self.clear_button.grid(row=2, column=3)
        self.close_button.grid(row=2, column=4)
        
    def cleanDesktop(self):
        os.system('cd /Users/alexanderChudinov/Desktop/Tools; ./clean')
        print("Desktop cleaned.")
        
    def spoofMAC(self):
        os.system('while sleep 10; do sudo networksetup -setnetworkserviceenabled Wi-Fi off; ifconfig en0 | grep ether;openssl rand -hex 6 | sed \'s/\\(..\\)/\\1:/g; s/.$//\' | sudo xargs ifconfig en0 ether; ifconfig en0 | grep ether; sudo networksetup -setnetworkserviceenabled Wi-Fi on; sudo ifconfig en0 down; sudo ifconfig en0 up; done')
        
    def clearTerminal(self):
        os.system('clear')

root = Tk()
gui = toolboxGUI(root)
root.mainloop()