from tkinter import*
from tkinter import messagebox
class myfee:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")

        self.fee_id=Label(self.root, text="Fee ID:", bg="#f0f0f0").pack()  
        self.fee_id_txt=Entry(self.root, width=30).pack(pady=5)  
        self.std=Label(self.root, text="Student ID:", bg="#f0f0f0").pack()  
        self.std_txt=Entry(self.root, width=30).pack(pady=5)  
        self.amount=Label(self.root, text="Amount:", bg="#f0f0f0").pack()  
        self.amount_txt=Entry(self.root, width=30).pack(pady=5)  
        self.payment_s=Label(self.root, text="Payment Status:", bg="#f0f0f0").pack()  
        self.payment_txt=Entry(self.root, width=30).pack(pady=5)
        self.sub_btn=Button(self.root, text="Submit", bg="#4CAF50", fg="white").pack(pady=10)  
        self.clr_btn=Button(self.root, text="Clear", bg="#f44336", fg="white").pack(pady=5)  
   





if __name__=="__main__":
   
    root=Tk()
    obj=myfee(root)
    root.mainloop()