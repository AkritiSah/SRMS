from tkinter import*
from tkinter import messagebox
class myattendance:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")




        self.attendance=Label(self.root, text="Attendance ID:", bg="#f0f0f0").pack()  
        self.atte_txt=Entry(self.root, width=30).pack(pady=5)  
        self.std_id=Label(self.root, text="Student ID:", bg="#f0f0f0").pack()  
        self.std_txt=Entry(self.root, width=30).pack(pady=5)  
        self.sub_id=Label(self.root, text="Subject ID:", bg="#f0f0f0").pack()  
        self.sub_txt=Entry(self.root, width=30).pack(pady=5)  
        self.date=Label(self.root, text="Date:", bg="#f0f0f0").pack()  
        self.date_txt=Entry(self.root, width=30).pack(pady=5)
        self.status=Label(self.root, text="Status:", bg="#f0f0f0").pack()  
        self.status_txt=Entry(self.root, width=30).pack(pady=5)  
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   








if __name__=="__main__":
   
    root=Tk()
    obj=myattendance(root)
    root.mainloop()