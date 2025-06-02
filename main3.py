from tkinter import *
from tkinter.ttk import *
import time

root = Tk()
root.geometry("500x500")
root.title("Progress bar")

progress = Progressbar(root,orient = HORIZONTAL,length = 250, mode = "determinate")
progress.pack(pady = 10)

def bar():
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(2)

    progress['value'] = 100
    root.update()
    time.sleep(3)

bn1 = Button(root,text = "Start",command = bar)
bn1.pack(pady = 20)



root.mainloop()