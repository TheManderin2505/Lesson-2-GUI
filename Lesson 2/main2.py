from tkinter import *
root = Tk()
root.geometry("500x500")
root.title('SpinBox')

w= Spinbox(root,from_=0,to=100)
w.pack()

root.mainloop()