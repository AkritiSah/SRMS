from tkinter import*
from tkinter import messagebox
from dashboard import mydashboard
class mylogin:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("800x700+50+20")


        self.user_n=Label(self.root,text="Username:",bg="#f0f0f0",font=("Arial",19,"bold")).pack()
        self.user_txt=Entry(self.root,width=45).pack(pady=10)
        self.password=Label(self.root,text="Password:",bg="#f0f0f0",font=("Arial",19,"bold"),show="*").pack()
        self.password_txt=Entry(self.root,width=45).pack(pady=10)

        self.login_btn=Button(self.root,text="Login",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#4CAF50",width=8,fg="white",command=self.show_login)
        self.login_btn.pack(pady=40)

        self.login_btn=Button(self.root,text="Clear",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#f44336",width=8,fg="white")
        self.login_btn.pack(pady=10)

        self.forget_btn=Button(self.root,text="Forgot Password",bd=2,relief=SUNKEN,font=("Roboto",17),bg="#0056bc",width=15,fg="white")
        self.forget_btn.place(x=310,y=376,height=40,width=185)

    def show_login(self):
        username=self.user_txt.get()
        password=self.password_txt.get()
        if username=="praveen"and password=="Praveen@123":
            messagebox.showinfo("sucess","successfully login")
            self.root=mydashboard()

        else:
            messagebox.showerror("error","invalid password and username")
            
        












if __name__=="__main__":
   
    root=Tk()
    obj=mylogin(root)
    root.mainloop()
