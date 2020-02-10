'''
May 2017
@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

# Adding a Label
ttk.Label(win, text="Моя перша програма").grid(column=0, row=0)


# Button Click Event Function
def click_me():
    win.destroy()

# Adding a Button
action = ttk.Button(win, text="Закрити!", command=click_me)   
action.grid(column=0, row=1)











#======================
# Start GUI
#======================
win.mainloop()
