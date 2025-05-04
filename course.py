from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
class mycourse:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1050x700+50+20")


        self.course=Label(self.root, text="Course ID:", bg="#f0f0f0").pack()  
        self.course_txt=Entry(self.root, width=30).pack(pady=5)  
        self.course_n=Label(self.root, text="Course Name:", bg="#f0f0f0").pack()  
        self.course_n_txt=Entry(self.root, width=30).pack(pady=5)  
        self.duration=Label(self.root, text="Duration:", bg="#f0f0f0").pack()  
        self.duration_txt=Entry(self.root, width=30).pack(pady=5)  
        self.department=Label(self.root, text="DepartmentId:", bg="#f0f0f0").pack()  
        self.depart_txt=Entry(self.root, width=30).pack(pady=5) 
        self.charges=Label(self.root, text="Charges:", bg="#f0f0f0").pack()  
        self.charges_txt=Entry(self.root, width=30).pack(pady=5) 
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5) 


        self.image=Image.open("images/course_profile.png")
        self.img_resize=self.image.resize((250,250),Image.Resampling.BICUBIC)
        self.convert_img=ImageTk.PhotoImage(self.img_resize)
        self.img_lab=Label(self.root,image=self.convert_img)
        self.img_lab.place(x=30,y=28) 


        self.update_btn=Button(self.root,text="Update",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#4CAF50",width=8,fg="white")
        self.update_btn.place(x=700,y=150)

        self.delete_btn=Button(self.root,text="Delete",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#f44336",width=8,fg="white")
        self.delete_btn.place(x=840,y=150)


        self.table_frame=Frame(self.root,bd=5,relief=SUNKEN)
        self.table_frame.place(x=50,y=400,width=890,height=400)

        self.course_table=ttk.Treeview(self.table_frame,column=("course_n","courseid","dep_id","duration"),show="headings")
        self.course_table.pack(fill=BOTH,expand=True)

        self.course_table.heading("course_n",text="CourseName")
        self.course_table.heading("courseid",text="CourseID")
        self.course_table.heading("dep_id",text="DepartmentID")
        self.course_table.heading("duration",text="Duration")




        self.course_table.column("course_n",width=100)
        self.course_table.column("courseid",width=100)
        self.course_table.column("dep_id",width=100)
        self.course_table.column("duration",width=100)

        self.courses_lab=Label(self.root,text="Search Courses Here",font=("Arial",20,"bold"),bg="#4CAF50")
        self.courses_lab.place(x=700,y=20)
        self.search_course=Entry(self.root,bd=3,relief=SUNKEN)
        self.search_course.place(x=650,y=80,width=200,height=30)

        self.search_btn=Button(self.root,bd=3,relief=RAISED,font=("Roboto",15),bg="blue",fg="white",text="Search")
        self.search_btn.place(x=850,y=80,height=30,width=195)
       
        
    




if __name__=="__main__":
   
    root=Tk()
    obj=mycourse(root)
    root.mainloop()

