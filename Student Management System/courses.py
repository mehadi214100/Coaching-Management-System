from tkinter import *
from  tkinter import  ttk,messagebox
import  sqlite3
from PIL import Image, ImageTk


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Private Study Zone")
        self.root.geometry("1200x480+200+180")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========title===============
        title = Label(self.root, text="Manage Course Details", font=("goudy old style ", 20, "bold"), bg="#033054",
                      fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # =============variables================
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charge = StringVar()

        # =======================widgets=====================

        lbl_course_Name = Label(self.root, text="Course Name", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,
                                                                                                                  y=100)
        lbl_charge = Label(self.root, text="Charges", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,
                                                                                                               y=140)
        lbl_descroption = Label(self.root, text="Description", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=180)

        # ==============Entry Fileds ================

        self.text_course_Name = (
            Entry(self.root, textvariable=self.var_course, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.text_course_Name.place(x=150, y=60, width=200)
        text_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style ", 15, "bold"),
                              bg="lightyellow").place(x=150, y=100, width=200)
        text_charge = Entry(self.root, textvariable=self.var_charge, font=("goudy old style ", 15, "bold"),
                            bg="lightyellow").place(x=150, y=140, width=200)
        self.text_descroption = (Text(self.root, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.text_descroption.place(x=150, y=180, width=500, height=130)


        # ============ Buttons =============

        self.btn_add = Button(self.root,text="Save", font=("goudy old style ", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height =40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style ", 15, "bold"), bg="#4caf50", fg="white",
                              cursor="hand2",command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style ", 15, "bold"), bg="#f44336", fg="white",
                              cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style ", 15, "bold"), bg="#607d8b", fg="white",
                              cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)


        # ==============Search Panel ==============
        self.var_search = StringVar()

        lbl_search_course_Name = Label(self.root, text="Course Name", font=("goudy old style ", 15, "bold"), bg="white").place(x=720, y=60)
        text_search_course_Name = (Entry(self.root, textvariable=self.var_search, font=("goudy old style ", 15, "bold"), bg="lightyellow")).place(x=870, y=60, width=180)
        btn_search = Button(self.root,text="Search", font=("goudy old style ", 15, "bold"), bg="#03a9f4", fg="white", cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height =28)


        # ============ content
        self.C_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=720, y= 100,width =470, height=340)

        scrolly = Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame,orient=HORIZONTAL)

        self.course_Table = ttk.Treeview(self.C_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill = X)
        scrolly.pack(side=RIGHT,fill = Y)
        scrollx.config(command=self.course_Table.xview)
        scrolly.config(command=self.course_Table.yview)

        self.course_Table.heading("cid",text="Course ID")
        self.course_Table.heading("name",text="Name")
        self.course_Table.heading("duration",text="Duration")
        self.course_Table.heading("charges",text="Charges")
        self.course_Table.heading("description",text="Description")
        self.course_Table["show"] = 'headings'

        self.course_Table.column("cid",width=100)
        self.course_Table.column("name",width=100)
        self.course_Table.column("duration",width=100)
        self.course_Table.column("charges",width=100)
        self.course_Table.column("description",width=150)

        self.course_Table.pack(fill=BOTH, expand=1)
        self.course_Table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#========================================================

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute(f"select *  from course where name LIKE '%{self.var_search.get()}%'")
            rows = cur.fetchall()
            self.course_Table.delete(*self.course_Table.get_children())
            for row in rows:
                self.course_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charge.set("")
        self.var_search.set("")
        self.text_descroption.delete("1.0",END)
        self.text_course_Name.config(state=NORMAL)


    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select *  from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if(row==None):
                    messagebox.showerror("Error", "Please select course from  course list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Are you Sure ?  ",parent = self.root)
                    if(op==True):
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Delete Successfully !!!",parent= self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def get_data(self,ev):
        self.text_course_Name.config(state='readonly')
        r = self.course_Table.focus()
        content = self.course_Table.item(r)
        row = content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charge.set(row[3])
        self.text_descroption.delete("1.0",END)
        self.text_descroption.insert(END,row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select *  from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if(row!=None):
                    messagebox.showerror("Error", "Course Name Already present", parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.text_descroption.get("1.0",END)

                    ))
                    con.commit()
                    messagebox.showinfo("Success","Courses Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select *  from course")
            rows = cur.fetchall()
            self.course_Table.delete(*self.course_Table.get_children())
            for row in rows:
                self.course_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select *  from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if(row==None):
                    messagebox.showerror("Error", "Select Course from List", parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where  name=?",(
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.text_descroption.get("1.0",END),
                        self.var_course.get()))

                    con.commit()
                    messagebox.showinfo("Success","Courses Update Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
