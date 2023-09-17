from tkinter import *
from PIL import Image, ImageTk
from courses import CourseClass
from students import studentClass
from results import ResultClass
from  report import  ReportClass
import sqlite3
from tkinter import ttk,messagebox
class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Private Study Zone")
        self.root.geometry("1350x700+100+50")
        self.root.resizable(False,False)
        self.root.config(bg="white")
        # ========icon===============
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # ========title===============
        title = Label(self.root, text="Private Study Zone", image=self.logo_dash, padx=20, compound=LEFT,
                      font=("goudy old style ", 20, "bold"), bg="#033054",
                      fg="white")
        title.place(x=0, y=0, relwidth=1, height=50)

        # ========menu===============
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2",command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                             cursor="hand2",command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2",command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame,command=self.add_report, text="View Students", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2").place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                            cursor="hand2").place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",
                          cursor="hand2").place(x=1120, y=5, width=200, height=40)

        #-------------------------content window-----
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920,350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lb_bg = Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        # ================ UPDATE DETAILS ===================
        self.lbl_courses = (Label(self.root,text=f"Total Courses\n[ {self.showCourse()} ]",bg="#e43b06",fg="white",bd=10, relief=RIDGE,font=("goudy old style",20)))
        self.lbl_courses.place(x=400,y=530,width=300,height=100)

        self.lbl_students = (Label(self.root,text=f"Total Students\n[ {self.showStudents()} ]",bg="#0676ad",fg="white",bd=10, relief=RIDGE,font=("goudy old style",20)))
        self.lbl_students.place(x=710,y=530,width=300,height=100)

        self.lbl_result = (Label(self.root,text="Total Results\n[ 0 ]",bg="#038074",fg="white",bd=10, relief=RIDGE,font=("goudy old style",20)))
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        # ========footer===============
        footer = Label(self.root, text="PSZ - Private Study Zone\n Contact us For any Technical issue : +8801777400185",
                      font=("goudy old style ", 12,), bg="#262626",fg="white")
        footer.pack(side=BOTTOM, fill = X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_ob = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_ob = studentClass(self.new_win)
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_ob = ReportClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_ob = ResultClass(self.new_win)

    def showCourse(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select *  from course")
            rows = cur.fetchall()
            return len(rows)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def showStudents(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select *  from students")
            rows = cur.fetchall()
            return len(rows)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")



if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
