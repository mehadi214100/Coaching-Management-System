from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Private Study Zone")
        self.root.geometry("1200x480+200+180")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========title===============
        title = Label(self.root, text="Add Students Results", font=("goudy old style ", 20, "bold"), bg="orange",
                      fg="#262626")
        title.place(x=10, y=15, width=1180, height=50)


        # ================ widgets ========================

        # ---------------variables ------------------
        self.var_roll  =  StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmarks = StringVar()
        self.roll_list = []
        self.fetch_roll()
        Label(self.root, text="Select Student", font=("goudy old style ", 20, "bold"), bg="white").place(x=50, y=100)
        Label(self.root, text="Name", font=("goudy old style ", 20, "bold"), bg="white").place(x=50, y=160)
        Label(self.root, text="Course", font=("goudy old style ", 20, "bold"), bg="white").place(x=50, y=220)
        Label(self.root, text="Mark Obtained", font=("goudy old style ", 20, "bold"), bg="white").place(x=50, y=280)
        Label(self.root, text="Full Marks", font=("goudy old style ", 20, "bold"), bg="white").place(x=50, y=340)


        self.student = (ttk.Combobox(self.root, textvariable=self.var_roll, font=("goudy old style ", 15, "bold"),state='readonly', justify=CENTER,values=(self.roll_list)))
        self.student.place(x=280, y=100, width=200)
        self.student.set("Select")
        btn_search = Button(self.root,command=self.search, text="Search", font=("goudy old style ", 15, "bold"), bg="#03a9f4", fg="white",cursor="hand2").place(x=500, y=100, width=100, height=28)

        self.txt_name = (Entry(self.root, textvariable=self.var_name, font=("goudy old style ", 20, "bold"), bg="lightyellow", state="readonly")).place(x=280, y=160, width=320)
        self.txt_course = (Entry(self.root, textvariable=self.var_course, font=("goudy old style ", 20, "bold"), bg="lightyellow", state="readonly")).place(x=280, y=220, width=320)
        self.txt_marks = (Entry(self.root, textvariable=self.var_marks, font=("goudy old style ", 20, "bold"), bg="lightyellow")).place(x=280, y=280, width=320)
        self.txt_fullmarks = (Entry(self.root, textvariable=self.var_fullmarks, font=("goudy old style ", 20, "bold"), bg="lightyellow")).place(x=280, y=340, width=320)

        # ====================================  button =======================================]
        btn_add = Button(self.root, text="Submit",command=self.add ,font=("times new roman", 15), bg="lightgreen",activebackground="lightgreen" ,cursor="hand2").place(x=300, y=420, width=120, height=35)
        btn_clear = Button(self.root,command=self.clear, text="Clear", font=("times new roman", 15), bg="lightgray",activebackground="lightgray",cursor="hand2").place(x=430, y=420, width=120, height=35)


        # =================== image ==========================


        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((500,300))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lb_bg = Label(self.root,image=self.bg_img).place(x=650,y=100)

# =================== function ================
    def fetch_roll(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from students")
            rows = cur.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name,course  from students where roll=?",(self.var_roll.get(),))
            row = cur.fetchone()
            if(row!=None):
               self.var_name.set(row[0])
               self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cur.execute("select *  from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row = cur.fetchone()
                if(row!=None):
                    messagebox.showerror("Error", "Result Already Present", parent=self.root)
                else:
                    per = int((int(self.var_marks.get())*100)/int(self.var_fullmarks.get()))
                    cur.execute("insert into result (roll,name,course,marks_ob,full_mark,percentage) values(?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks.get(),
                        self.var_fullmarks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def clear(self):
        self.var_roll.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmarks.set("")



if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
