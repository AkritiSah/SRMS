from tkinter import*
from tkinter import messagebox
class myteacher:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")


        self.teacher_id=Label(self.root, text="TeacherId:", bg="#f0f0f0").pack()  
        self.teach_id_txt=Entry(self.root, width=30).pack(pady=5)  
        self.dep_id=Label(self.root, text="DepartmentId:", bg="#f0f0f0").pack()  
        self.dep_txt=Entry(self.root, width=30).pack(pady=5)  
        self.first_n=Label(self.root, text="First Name:", bg="#f0f0f0").pack()  
        self.first_txt=Entry(self.root, width=30).pack(pady=5)
        self.last_n=Label(self.root, text="Last Name:", bg="#f0f0f0").pack()  
        self.last_n_txt=Entry(self.root, width=30).pack(pady=5) 
        self.phone=Label(self.root, text="Phone No:", bg="#f0f0f0").pack()  
        self.phone_txt=Entry(self.root, width=30).pack(pady=5) 
        self.email=Label(self.root, text="EmailId:", bg="#f0f0f0").pack()  
        self.email_txt=Entry(self.root, width=30).pack(pady=5)
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   








if __name__=="__main__":
   
    root=Tk()
    obj=myteacher(root)
    root.mainloop()