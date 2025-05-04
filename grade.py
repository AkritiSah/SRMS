from tkinter import*
from tkinter import messagebox
class mygrade:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")

        self.grade_id=Label(self.root, text="Grade ID:", bg="#f0f0f0").pack()  
        self.grade_txt=Entry(self.root, width=30).pack(pady=5)  
        self.grade=Label(self.root, text="Grade:", bg="#f0f0f0").pack()  
        self.grade_id_txt=Entry(self.root, width=30).pack(pady=5)  
        self.min_marks=Label(self.root, text="Min Marks:", bg="#f0f0f0").pack()  
        self.min_txt=Entry(self.root, width=30).pack(pady=5) 
        self.max_marks=Label(self.root, text="Max Marks:", bg="#f0f0f0").pack()  
        self.marks_txt=Entry(self.root, width=30).pack(pady=5) 
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
            
if __name__=="__main__":
   
    root=Tk()
    obj=mygrade(root)
    root.mainloop()
