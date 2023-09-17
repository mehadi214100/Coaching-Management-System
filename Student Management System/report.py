from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk


class ReportClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Private Study Zone")
        self.root.geometry("1200x480+200+180")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========title===============
        title = Label(self.root, text="View Students Results", font=("goudy old style ", 20, "bold"), bg="orange",
                      fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)

        # ================== search ================
        self.var_search = StringVar()
        self.var_id = ""
        Label(self.root, text="Search By Roll No.", font=("goudy old style ", 20, "bold"), bg="white").place(x=280, y=100)
        Entry(self.root,textvariable=self.var_search, font=("goudy old style ", 20), bg="lightyellow").place(x=540, y=100,width=150)
        btn_search = Button(self.root, command=self.search,text="Search", font=("goudy old style ", 15, "bold"), bg="#03a9f4", fg="white",cursor="hand2").place(x=700, y=100, width=100, height=35)
        btn_clear = Button(self.root,command=self.clear ,text="Clear", font=("goudy old style ", 15, "bold"), bg="gray", fg="white",cursor="hand2").place(x=820, y=100, width=100, height=35)

        Label(self.root, text="Roll No.", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=150, y=230,width=150,height=50)
        Label(self.root, text="Name", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=300, y=230,width=150,height=50)
        Label(self.root, text="Course", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=450, y=230,width=150,height=50)
        Label(self.root, text="Mark Obtained", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=600, y=230,width=150,height=50)
        Label(self.root, text="Total Marks", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=750, y=230,width=150,height=50)
        Label(self.root, text="Percentage", font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE).place(x=900, y=230,width=150,height=50)


        self.roll=(Label(self.root,  font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE))
        self.roll.place(x=150, y=280,width=150,height=50)
        self.name=(Label(self.root,  font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE))
        self.name.place(x=300, y=280,width=150,height=50)
        self.course=(Label(self.root,  font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE))
        self.course.place(x=450, y=280,width=150,height=50)
        self.mark=Label(self.root,  font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE)
        self.mark.place(x=600, y=280,width=150,height=50)
        self.totalmark=Label(self.root, font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE)
        self.totalmark.place(x=750, y=280,width=150,height=50)
        self.percentage=(Label(self.root, font=("goudy old style ", 15, "bold"), bg="white",bd=2,relief=GROOVE))
        self.percentage.place(x=900, y=280,width=150,height=50)


        # ========== button delete
        btn_delete = Button(self.root,command=self.delete ,text="Delete", font=("goudy old style ", 15, "bold"), bg="red", fg="white",cursor="hand2").place(x=500, y=350, width=150, height=35)

        # ======== function ================

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if(self.var_search.get()==""):
                messagebox.showerror("Error","Roll Number should be required",parent = self.root)
            else:
                cur.execute("select*  from result where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if (row != None):
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.mark.config(text=row[4])
                    self.totalmark.config(text=row[5])
                    self.percentage.config(text=row[6])
                else:
                    messagebox.showerror("Error", "No Record Found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.mark.config(text="")
        self.totalmark.config(text="")
        self.percentage.config(text="")
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_id == "":
                messagebox.showerror("Error","Search student result first !",parent=self.root)
            else:
                cur.execute("select *  from result where rid=?",(self.var_id,))
                row = cur.fetchone()
                if(row==None):
                    messagebox.showerror("Error", "Invalid Student Result", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Are you Sure ?  ",parent = self.root)
                    if(op==True):
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Delete Successfully !!!",parent= self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()
