#This code is going to be updated
#everytime i realize a new version
#any feedback is welcome :)

import pyautogui
from tkinter import *
import keyboard 
import time

win = Tk()
win.geometry("300x60")
win.resizable(False,False)
win.title("Cursor Automation")

def moving_cursor():
	time.sleep(5)
	x, y = pyautogui.position()
	while True:
		pyautogui.moveTo(x + 700,y, duration = 2)
		time.sleep(3)
		if keyboard.is_pressed('p'): #press and hold p to stop
			break
		pyautogui.moveTo(x,y, duration = 2)
		time.sleep(3)
		if keyboard.is_pressed('p'):
			break
		
		
size_font = dict(size = 30)

message = Label(win, text = "Press 'p' to stop", font = size_font)
message.pack()

btn = Button(win, text = "Start", command = moving_cursor, font = size_font)
btn.pack()

win.mainloop()
