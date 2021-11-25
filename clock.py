from tkinter import Label,Tk

import time

App_window = Tk()
App_window.title("CLOCK")
App_window.geometry("420x150")
App_window.resizable(1,1)

text_front = ("Boulder",68,'bold')
background = "black"
foregrund = "white"
border_width = 17

label = Label(App_window,font=text_front,bg=background,fg=foregrund,bd=border_width)
label.grid(row=0,column=1)

def digtalclock(): 
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digtalclock)

digtalclock()
App_window.mainloop()
