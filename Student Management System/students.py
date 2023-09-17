from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Private Study Zone")
        self.root.geometry("1200x480+200+180")
        self.root.config(bg="white")
        self.root.focus_force()

        # ========title===============
        title = Label(self.root, text="Students Information", font=("goudy old style ", 20, "bold"), bg="#033054",
                      fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # =============variables================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # =======================widgets=====================
        # ==================Column 1 ====================== #
        lbl_roll = Label(self.root, text="Roll No.", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,
                                                                                                          y=100)
        lbl_email = Label(self.root, text="email", font=("goudy old style ", 15, "bold"), bg="white").place(x=10,
                                                                                                            y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=180)

        lbl_state = Label(self.root, text="State", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=220)

        self.txt_state = (
            Entry(self.root, textvariable=self.var_state, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.txt_state.place(x=150, y=220, width=150)


        lbl_city = Label(self.root, text="City", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=310, y=220)

        self.txt_city = (
            Entry(self.root, textvariable=self.var_city, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.txt_city.place(x=380, y=220, width=100)

        lbl_pin = Label(self.root, text="Pin", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=500, y=220)

        self.txt_pin = (
            Entry(self.root, textvariable=self.var_pin, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.txt_pin.place(x=560, y=220, width=120)


        lbl_address = Label(self.root, text="Address", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=10, y=260)

        # ==============Entry Filed ================

        self.txt_roll = (
            Entry(self.root, textvariable=self.var_roll, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.txt_roll.place(x=150, y=60, width=200)
        text_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style ", 15, "bold"),
                          bg="lightyellow").place(x=150, y=100, width=200)
        text_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style ", 15, "bold"),
                           bg="lightyellow").place(x=150, y=140, width=200)

        self.text_gender = (ttk.Combobox(self.root, textvariable=self.var_gender, font=("goudy old style ", 15, "bold"),
                                         state='readonly', justify=CENTER,
                                         values=("Select", "Male", "Female", "Others")))
        self.text_gender.place(x=150, y=180, width=200)
        self.text_gender.current(0)

        # ==============Column 2 ============================

        lbl_dob = Label(self.root, text="D.O.B", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=360, y=60)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style ", 15, "bold"), bg="white").place(x=360,
                                                                                                             y=100)
        lbl_admission = Label(self.root, text="Admission", font=("goudy old style ", 15, "bold"), bg="white").place(x=360,
                                                                                                                y=140)
        lbl_course = Label(self.root, text="Course", font=("goudy old style ", 15, "bold"), bg="white").place(
            x=360, y=180)

        # ============================   column 2 Entry Form
        self.courseList = []

        self.fetch_course()

        self.txt_dob = (
            Entry(self.root, textvariable=self.var_dob, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.txt_dob.place(x=480, y=60, width=200)
        text_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style ", 15, "bold"),
                          bg="lightyellow").place(x=480, y=100, width=200)
        text_admission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style ", 15, "bold"),
                           bg="lightyellow").place(x=480, y=140, width=200)

        self.text_course = (ttk.Combobox(self.root, textvariable=self.var_course, font=("goudy old style ", 15, "bold"),
                                         state='readonly', justify=CENTER,
                                         values=(self.courseList)))
        self.text_course.place(x=480, y=180, width=200)
        self.text_course.set("Select")

        # ================Text Address =======================

        self.text_address = (Text(self.root, font=("goudy old style ", 15, "bold"), bg="lightyellow"))
        self.text_address.place(x=150, y=270, width=540, height=100)

        # ============ Buttons =============

        self.btn_add = Button(self.root, text="Save", font=("goudy old style ", 15, "bold"), bg="#2196f3", fg="white",
                              cursor="hand2", command=self.add)
        self.btn_add.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text="Update", font=("goudy old style ", 15, "bold"), bg="#4caf50",
                                 fg="white",
                                 cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text="Delete", font=("goudy old style ", 15, "bold"), bg="#f44336",
                                 fg="white",
                                 cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text="Clear", font=("goudy old style ", 15, "bold"), bg="#607d8b",
                                fg="white",
                                cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        # ==============Search Panel ==============
        self.var_search = StringVar()

        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style ", 15, "bold"),
                                       bg="white").place(x=720, y=60)
        text_search_roll = (Entry(self.root, textvariable=self.var_search, font=("goudy old style ", 15, "bold"),
                                         bg="lightyellow")).place(x=870, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style ", 15, "bold"), bg="#03a9f4", fg="white",
                            cursor="hand2", command=self.search).place(x=1070, y=60, width=120, height=28)

        # ============ content
        self.C_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_frame.place(x=720, y=100, width=470, height=340)

        scrolly = Scrollbar(self.C_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)

        self.course_Table = ttk.Treeview(self.C_frame, columns=("roll", "name", "email", "gender", "dob","contact","admission","course","state","city","pin","address"),
                                         xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.course_Table.xview)
        scrolly.config(command=self.course_Table.yview)

        self.course_Table.heading("roll", text="Roll No.")
        self.course_Table.heading("name", text="Name")
        self.course_Table.heading("email", text="Email")
        self.course_Table.heading("gender", text="Gender")
        self.course_Table.heading("dob", text="Date of Birth")
        self.course_Table.heading("contact", text="Contact")
        self.course_Table.heading("admission", text="Admission Date")
        self.course_Table.heading("course", text="Course")
        self.course_Table.heading("state", text="State")
        self.course_Table.heading("city", text="City")
        self.course_Table.heading("pin", text="Pin")
        self.course_Table.heading("address", text="Address")

        self.course_Table["show"] = 'headings'
        self.course_Table.column("roll", width=100)
        self.course_Table.column("name", width=100)
        self.course_Table.column("email", width=100)
        self.course_Table.column("gender", width=100)
        self.course_Table.column("dob", width=150)
        self.course_Table.column("contact", width=150)
        self.course_Table.column("admission", width=150)
        self.course_Table.column("course", width=150)
        self.course_Table.column("state", width=150)
        self.course_Table.column("city", width=150)
        self.course_Table.column("pin", width=150)
        self.course_Table.column("address", width=150)

        self.course_Table.pack(fill=BOTH, expand=1)
        self.course_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        self.fetch_course()

    # ========================================================

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select *  from students where roll=?",(self.var_search.get(),))
            row = cur.fetchone()
            if(row!=None):
                self.course_Table.delete(*self.course_Table.get_children())
                self.course_Table.insert('', END, values=row)
            else:
                messagebox.showerror("Error","No Record Found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.text_address.delete("1.0", END)
        self.text_address.insert(END,"")
        self.var_search.set("")
        self.txt_roll.config(state=NORMAL)
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll should be required", parent=self.root)
            else:
                cur.execute("select *  from students where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if (row == None):
                    messagebox.showerror("Error", "Please select Students from  course list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Are you Sure ?  ", parent=self.root)
                    if (op == True):
                        cur.execute("delete from students where roll=?", (self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Delete Successfully !!!", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        r = self.course_Table.focus()
        content = self.course_Table.item(r)
        row = content["values"]

        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.text_address.delete("1.0", END)
        self.text_address.insert(END,row[11])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll No  should be required", parent=self.root)
            else:
                cur.execute("select *  from students where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if (row != None):
                    messagebox.showerror("Error", "Roll No Already present", parent=self.root)
                else:
                    cur.execute("insert into students (roll, name, email, gender, dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.text_address.get("1.0", END)

                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select *  from students")
            rows = cur.fetchall()
            self.course_Table.delete(*self.course_Table.get_children())
            for row in rows:
                self.course_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select name  from course")
            rows = cur.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.courseList.append(row[0])

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error", "Roll Noshould be required", parent=self.root)
            else:
                cur.execute("select *  from students where roll=?", (self.var_roll.get(),))
                row = cur.fetchone()
                if (row == None):
                    messagebox.showerror("Error", "Select Students from List", parent=self.root)
                else:
                    cur.execute("update students set name=?, email=?, gender=?, dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?", (
                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.text_address.get("1.0", END),
                    self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Student Update Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()
