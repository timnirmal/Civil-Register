from tkinter import *

if __name__ == '__main__':
    # Create Object and setup window
    root = Tk()
    root.title('Login Form')

    # Create Frames
    top = Frame(root, width=600, height=100, bg='white')
    top.pack(side=TOP)
    bottom = Frame(root, width=600, height=500, bg='#fcc324')
    bottom.pack(side=BOTTOM)

    # Create Widgets
    label = Label(top, text='Login Form', font=('arial', 30), fg='steelblue', bg='white')
    label.place(x=200, y=30)

    username = Label(bottom, text='Username', font=('arial', 15), fg='white', bg='#fcc324')
    username.place(x=40, y=70)

    password = Label(bottom, text='Password', font=('arial', 15), fg='white', bg='#fcc324')
    password.place(x=40, y=130)

    username_entry = Entry(bottom, bd=5, font=('arial', 15))
    username_entry.place(x=150, y=70)

    password_entry = Entry(bottom, bd=5, font=('arial', 15), show='*')
    password_entry.place(x=150, y=130)

    btn_login = Button(bottom, text='Login', font=('arial', 15))
    btn_login.place(x=150, y=190)

    btn_login = Button(bottom, text='Create Account', font=('arial', 15))
    btn_login.place(x=270, y=190)

    root.mainloop()
