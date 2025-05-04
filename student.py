from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
class mystudent:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1400x1000+50+20")

    
        self.label=Label(self.root, text="Student ID:", bg="#f0f0f0").pack()  
        self.std_txt=Entry(self.root,width=30).pack(pady=5) 
        self.first_n=Label(self.root, text="First Name:", bg="#f0f0f0").pack()  
        self.first_n_txt=Entry(self.root, width=30).pack(pady=5)  
        self.last_n=Label(self.root, text="Last Name:", bg="#f0f0f0").pack()  
        self.last_n_txt=Entry(self.root, width=30).pack(pady=5)  
        self.course_id=Label(self.root, text="Course ID:", bg="#f0f0f0").pack()  
        self.course_txt=Entry(self.root, width=30).pack(pady=5)

        self.email=Label(self.root, text="Email:", bg="#f0f0f0").pack()  
        self.email_txt=Entry(self.root, width=30).pack(pady=5)
        self.address=Label(self.root, text="Address:", bg="#f0f0f0").pack()  
        self.address_txt=Entry(self.root, width=30).pack(pady=5)
        self.phone=Label(self.root, text="Phone:", bg="#f0f0f0").pack()  
        self.phone_txt=Entry(self.root, width=30).pack(pady=5)
        self.dob=Label(self.root, text="D.o.b:", bg="#f0f0f0").pack()  
        self.dob_txt=Entry(self.root, width=30).pack(pady=5)
        self.enroll=Label(self.root, text="Enroll:", bg="#f0f0f0").pack()  
        self.enroll_txt=Entry(self.root, width=30).pack(pady=5)
        self.gender=Label(self.root,width=30,text="Gender:").pack()
        self.male=Radiobutton(self.root,value="Male",text="Male",variable=self.gender,fg="blue",bg="#f0f0f0").pack()
        #self.gender.set("Male")
        self.female=Radiobutton(self.root,value="Female",text="Female",variable=self.gender,fg="blue",bg="#f0f0f0").pack()
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white",height=2,width=18,font=("Arial",10)).pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white",height=2,width=14,font=("Arial",8)).pack(pady=5)  
        self.image=Image.open("images/student_profile.png")
        self.img_resize=self.image.resize((200,200),Image.Resampling.BICUBIC)
        self.convert_img=ImageTk.PhotoImage(self.img_resize)
        self.img_lab=Label(self.root,image=self.convert_img)
        self.img_lab.place(x=50,y=28)

        self.update_btn=Button(self.root,text="Update",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#4CAF50",width=8,fg="white")
        self.update_btn.place(x=100,y=280)

        self.delete_btn=Button(self.root,text="Delete",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#f44336",width=8,fg="white")
        self.delete_btn.place(x=100,y=400)
        self.table_frame=Frame(self.root,bd=10,relief=SUNKEN,bg="red")
        self.table_frame.place(x=50,y=650,width=1280,height=200)
        
        

        self.student_table=ttk.Treeview(self.table_frame,column=("first_n",
        "last_n","email","address","phone","gender","enroll_d","dob","student_id"
        ,"course_id"
        ),show="headings")
        self.student_table.pack(fill=BOTH,expand=True)

        self.student_table.heading("first_n",text="FirstName")
        self.student_table.heading("last_n",text="LastName")
        self.student_table.heading("email",text="EmailId")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("enroll_d",text="EnrollDate")
        self.student_table.heading("dob",text="D.O.B")
        self.student_table.heading("student_id",text="StudentId")
        self.student_table.heading("course_id",text="CourseId")

        self.student_table.column("first_n",width=100)
        self.student_table.column("last_n",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("phone",width=100)

        self.student_table.column("gender",width=100)
        self.student_table.column("enroll_d",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("student_id",width=100)
        self.student_table.column("course_id",width=100)
        self.scrollbar=ttk.Scrollbar(self.student_table,orient="vertical",command=self.student_table.yview)
        self.student_table.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right",fill="y")
        self.scrollbar_h=ttk.Scrollbar(self.student_table,orient="horizontal",command=self.student_table.set)
        self.student_table.config(xscrollcommand=self.scrollbar_h.set)
        self.scrollbar_h.pack(side="bottom",fill="x")
        

        
        
        
    
if __name__=="__main__":
   
    root=Tk()
    obj=mystudent(root)
    root.mainloop()
