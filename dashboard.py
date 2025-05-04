from tkinter import*
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox
from student import mystudent
from course import mycourse
from exam import myexam
from department import mydepartment
from fee import myfee
from result import myresult
from grade import mygrade
from subject import mysubject
from teacher import myteacher
from attendance import myattendance

class mydashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        # self.root.geometry("800x700+50+20")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # ===icons===
        # self.logo_dash=ImageTk.PhotoImage(file="images/RMS_logo_1.jpeg")
        title=Label(self.root,text="Student Result Management System",font=("goudy old style",20,"bold"),bg="#033054", fg="white").place(x=0,y=0,relwidth=1,height=50)
        self.menu_frame=Frame(self.root,bg="#2C3E50")
        self.menu_frame.pack(fill="y",side=LEFT)

        self.label_frame=LabelFrame(self.menu_frame,bd=3,relief=SUNKEN,bg="#2C3E50")
        self.label_frame.pack(fill=BOTH,expand=1)

        self.std_btn=Button(self.label_frame,text="Student",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_student)
        self.std_btn.pack(fill="x",pady=3)
        self.course_btn=Button(self.label_frame,text="Course",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_course)
        self.course_btn.pack(fill="x",pady=3)
        self.dept_btn=Button(self.label_frame,text="Department",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_department)
        self.dept_btn.pack(fill="x",pady=3)
        self.result_btn=Button(self.label_frame,text="Result",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_result)
        self.result_btn.pack(fill="x",pady=3)
        self.fee_btn=Button(self.label_frame,text="Fee",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_fee)
        self.fee_btn.pack(fill="x",pady=3)
        self.atten_btn=Button(self.label_frame,text="Attendance",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_attendance)
        self.atten_btn.pack(fill="x",pady=3)
        self.exam_btn=Button(self.label_frame,text="Exam",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_exam)
        self.exam_btn.pack(fill="x",pady=3)
        
        self.teacher_btn=Button(self.label_frame,text="Teacher",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_teacher)
        self.teacher_btn.pack(fill="x",pady=3)
        self.teacher_btn=Button(self.label_frame,text="Grade",font=("Roboto",16,),bg="#34495E",fg="white",command=self.show_grade)
        self.teacher_btn.pack(fill="x",pady=3)
        
    
       
    name="praveen"    
    if name=="praveen":
      
        
    
        def show_student(self):
          self.top=Toplevel()
          self.new_win=mystudent(self.top)
        def show_course(self):
          self.top=Toplevel()
          self.new_win=mycourse(self.top)
        def show_department(self):
          self.top=Toplevel()
          self.new_win=mydepartment(self.top)
        def show_exam(self):
          self.top=Toplevel()
          self.new_win=myexam(self.top)
        def show_result(self):
          self.top=Toplevel()
          self.new_win=myresult(self.top)
        def show_grade(self):
          self.top=Toplevel()
          self.new_win=mygrade(self.top)
        def show_attendance(self):
          self.top=Toplevel()
          self.new_win=myattendance(self.top)
        def show_fee(self):
          self.top=Toplevel()
          self.new_win=myfee(self.top)
    
        def show_subject(self):
          self.top=Toplevel()
          self.new_win=mysubject(self.top)


        def show_teacher(self):

          self.top=Toplevel()
          self.new_win=myteacher(self.top)
    


      








                              
                              

                              

                              

                              

                              

                              

                              

                              







if __name__=="__main__":
   
    root=Tk()
    obj=mydashboard(root)
    root.mainloop()
    login_win.mainloop()

