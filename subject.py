from tkinter import*
from tkinter import messagebox
class mysubject:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")


        self.sub_id=Label(self.root, text="Subject ID:", bg="#f0f0f0").pack()  
        self.sub_txt=Entry(self.root, width=30).pack(pady=5)  
        self.sub_n=Label(self.root, text="Subject Name:", bg="#f0f0f0").pack()  
        self.sub_n_txt=Entry(self.root, width=30).pack(pady=5)  
        self.course=Label(self.root, text="Course ID:", bg="#f0f0f0").pack()  
        self.course_txt=Entry(self.root, width=30).pack(pady=5) 
        self.teacher=Label(self.root, text="TeacherId:", bg="#f0f0f0").pack()  
        self.teacher_txt=Entry(self.root, width=30).pack(pady=5) 
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   





if __name__=="__main__":
   
    root=Tk()
    obj=mysubject(root)
    root.mainloop()













