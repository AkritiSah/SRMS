from tkinter import*
from tkinter import messagebox
class myexam:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")


        self.exam_id=Label(self.root, text="Exam ID:", bg="#f0f0f0").pack()  
        self.exam_id_txt=Entry(self.root, width=30).pack(pady=5)  
        self.sub_id=Label(self.root, text="Subject ID:", bg="#f0f0f0").pack()  
        self.sub_txt=Entry(self.root, width=30).pack(pady=5)  
        self.exam_d=Label(self.root, text="Exam Date:", bg="#f0f0f0").pack()  
        self.exam_txt=Entry(self.root, width=30).pack(pady=5)  
        self.exam_n=Label(self.root, text="Exam Name:", bg="#f0f0f0").pack()  
        self.exam_n_txt=Entry(self.root, width=30).pack(pady=5) 
        self.course_id=Label(self.root, text="CourseId:", bg="#f0f0f0").pack()  
        self.course_txt=Entry(self.root, width=30).pack(pady=5) 
        self.total_m=Label(self.root, text="Total Marks:", bg="#f0f0f0").pack()  
        self.total_txt=Entry(self.root, width=30).pack(pady=5)
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   






if __name__=="__main__":
   
    root=Tk()
    obj=myexam(root)
    root.mainloop()
