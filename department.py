from tkinter import*
from tkinter import messagebox
class mydepartment:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")
        self.dep_name=Label(self.root,text="DepartmentID:",bg="#f0f0f0").pack()
        self.dep_txt=Entry(self.root,width=30).pack(pady=5)
        self.dep_name=Label(self.root,text="Department Name:",bg="#f0f0f0").pack()
        self.dep_name_txt=Entry(self.root,width=30).pack(pady=5)

        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   






if __name__=="__main__":
   
    root=Tk()
    obj=mydepartment(root)
    root.mainloop()