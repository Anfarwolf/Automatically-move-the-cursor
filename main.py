# This is the final version of the project
# maybe there are things that i can improve
# but Im very happy with the result :)


import pyautogui
from tkinter import *
import keyboard 

win = Tk()
win.geometry("300x60")
win.resizable(False,False)
win.title("Cursor Automation")

def moving_cursor():
	while True:
		pyautogui.moveTo(500,300, duration = 1.5)
		if keyboard.is_pressed('p'):
			break
		pyautogui.moveTo(1000,300, duration = 1.5)
		if keyboard.is_pressed('p'):
			break
		
size_font = dict(size = 30)

message = Label(win, text = "Press 'p' to stop", font = size_font)
message.pack()

btn = Button(win, text = "Start", command = moving_cursor, font = size_font)
btn.pack()

win.mainloop()
