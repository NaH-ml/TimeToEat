import os
import tkinter as tk
import random
from matplotlib import image

def roll():
    f = random.randint(-1, 1)
    if f > -1:
        f += 1
    lb_A.config(text="去 " + str(f) + " 号码头！")

win = tk.Tk()

win.title("Go!")
win.geometry("220x200")
win.resizable(0,0)
win.config(bg="#ffffff")
win.attributes("-alpha", 0.98)

win.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"//bitmap//logo.ico")

img = tk.PhotoImage(file=os.path.dirname(os.path.abspath(__file__))+"//bitmap//dice.png")

lb_Q = tk.Label(text="今天去哪个码头整点薯条？")
lb_Q.config(bg="#ffffff")
lb_Q.place(x=75, y=55, width=145, height=20)

lb_A = tk.Label(text="投个骰子看看")
lb_A.config(bg="#ffffff")
lb_A.place(x=90, y=85, width=100, height=20)

lb_num = tk.Label()
lb_num.config(bg="#ffffff")
lb_num.place(x=90, y=105, width=100, height=20)

btn = tk.Button()
btn.config(image=img)
btn.config(bg="#ffffff")
btn.config(command=roll)
btn.place(x=15, y=60, width = 52, height=52)


win.mainloop()

