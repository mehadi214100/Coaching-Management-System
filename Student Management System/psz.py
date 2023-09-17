from tkinter import *
from tkinter import messagebox

import main
from main import RMS
# --------------------- Main Page Design -------------------------
root = Tk()
root.geometry("925x500+300+200")
root.title("PSZ")
root.configure(bg="#fff")
root.resizable(False, False)
img = PhotoImage(file="img_3.png")
Label(root, image=img, bg="white").place(x=80, y=120)
frame = Frame(root, height=350, width=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Private Study Zone", bg="white", fg="#57a1f8",
                font=("Arial", 23, 'bold'))
heading.place(x=50, y=5)


# -----------------------------------------sign in----------------------
def signin():
    username = user.get()
    password = code.get()
    if username == 'admin' and password == '1234':
        new_win = Toplevel(root)
        new_ob = RMS(new_win)
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "Invalid user name and password")
    elif username != 'admin':
        messagebox.showerror("Invalid", "Invalid user name")
    elif password != '1234':
        messagebox.showerror("Invalid", "Invalid password")


# ------------------------------------ Entry Form Reset for User -----------------------

def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'User Name')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, 'User Name')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=30, y=107)


# ------------------------------------ Entry Form Reset for password -----------------------

def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, 'Password')

code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=30, y=177)

# --------------------------------------------------------- Sign Up ----------------------

Button(frame, width=42, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signin).place(x=30, y=204)

label = Label(frame, text="Don't have an account ?", fg="black", bg="white", font="arial 9")
label.place(x=85, y=270)

sign_up = Button(frame, width=6, text="Sign Up", border=0, bg="white", cursor="hand2", fg="#57a1f8")
sign_up.place(x=225, y=270)

root.mainloop()
