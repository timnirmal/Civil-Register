import tkinter as tk

win = tk.Tk()
max_amount = 0
label1 = None


def fun():
    global max_amount, label1
    max_amount += 100
    label1.configure(text='Balance :$' + str(max_amount))


btn = tk.Button(win, text='Change', command=fun)
btn.grid()
t1 = str(max_amount)
label1 = tk.Label(win, text='Balance :$' + t1)
label1.grid()

win.mainloop()
