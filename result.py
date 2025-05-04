from tkinter import*
from tkinter import messagebox
class myresult:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")



        self.result=Label(self.root, text="Result ID:", bg="#f0f0f0").pack()  
        self.result_txt=Entry(self.root, width=30).pack(pady=5)  
        self.std=Label(self.root, text="Student ID:", bg="#f0f0f0").pack()  
        self.std_txt=Entry(self.root, width=30).pack(pady=5)  
        self.subject=Label(self.root, text="Subject ID:", bg="#f0f0f0").pack()  
        self.sub_txt=Entry(self.root, width=30).pack(pady=5)  
        self.marks_obt=Label(self.root, text="Marks Obtained:", bg="#f0f0f0").pack()  
        self.marks_txt=Entry(self.root, width=30).pack(pady=5) 
        self.total_marks=Label(self.root, text="Total Marks:", bg="#f0f0f0").pack()  
        self.marks_txt=Entry(self.root, width=30).pack(pady=5)
        self.result=Label(self.root, text="Result Date:", bg="#f0f0f0").pack()  
        self.result_txt=Entry(self.root, width=30).pack(pady=5) 
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
     






if __name__=="__main__":
   
    root=Tk()
    obj=myresult(root)
    root.mainloop()
