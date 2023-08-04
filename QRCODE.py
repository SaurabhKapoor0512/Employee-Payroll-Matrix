from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class QRCode:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed SAURABH KAPOOR | M.R.S Technology, Varanasi")
        self.root.resizable(False,False) # Args(width and Hiegth)
        self.root.focus_force()
        title=Label(self.root,text="  QR Code Generator",font=("times new roman",40),bg="#053246",fg="white",anchor="w").place(x=0,y=0,relwidth=1)

        #====Employee Details Window======
        #===Variables===

        self.var_EmpCode=StringVar()
        self.var_EmpName=StringVar()
        self.var_EmpDepart=StringVar()
        self.var_EmpDesig=StringVar()



        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)

        lbl_ID=Label(emp_Frame,text="Employee ID",font=("Times New Roman",15,'bold'),bg="white").place(x=20,y=60)
        lbl_name=Label(emp_Frame,text="Name",font=("Times New Roman",15,'bold'),bg="white").place(x=20,y=100)
        lbl_depart=Label(emp_Frame,text="Department",font=("Times New Roman",15,'bold'),bg="white").place(x=20,y=140)
        lbl_desig=Label(emp_Frame,text="Designation",font=("Times New Roman",15,'bold'),bg="white").place(x=20,y=180)

        txt_ID=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_EmpCode,bg="Light Yellow").place(x=200,y=60)
        txt_name=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_EmpName,bg="Light Yellow").place(x=200,y=100)
        txt_depart=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_EmpDepart,bg="Light Yellow").place(x=200,y=140)
        txt_desig=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_EmpDesig,bg="Light Yellow").place(x=200,y=180)

        gen_btn=Button(emp_Frame,text="QR Generate",command=self.Generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=180,height=30)
        clr_btn=Button(emp_Frame,text="Clear",command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)

        self.msg=''
        self.display_msg=Label(emp_Frame,text=self.msg,font=("Times New Roman",20),bg="white",fg='green')
        self.display_msg.place(x=0,y=310,relwidth=1)

         #====Employee QR Window======

        QR_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        QR_Frame.place(x=600,y=100,width=250,height=380)
        QR_title=Label(QR_Frame,text="Employee QR Code",font=("goudy old style",20),bg="#043256",fg="white").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(QR_Frame,text='No QR Code \n Available',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief='ridge')
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_EmpCode.set('')
        self.var_EmpName.set('')
        self.var_EmpDepart.set('')
        self.var_EmpDesig.set('')
        self.msg=''
        self.display_msg.config(text=self.msg)
        self.qr_code.config(image='')



    def Generate(self):
        if self.var_EmpCode.get()=='' or self.var_EmpName.get()=='' or self.var_EmpDepart.get()=='' or self.var_EmpDesig.get()=='':
            self.msg='All Fields are Required!!!'
            self.display_msg.config(text=self.msg,fg='red')
        else:

            qr_data=(f'Employee ID: {self.var_EmpCode.get()}\nEmployee Name: {self.var_EmpName.get()}\nEmployee Department: {self.var_EmpDepart.get()}\nEmployee Designation: {self.var_EmpCode.get()}')
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("EMPLOYEE_QR/Emp_"+str(self.var_EmpCode.get())+'.png')

            #=============QR Code Update============
            self.im=ImageTk.PhotoImage(file="EMPLOYEE_QR/Emp_"+str(self.var_EmpCode.get())+'.png')
            self.qr_code.config(image=self.im)
            #========updating notification===========
            self.msg='QR Generated Successfully!!!'
            self.display_msg.config(text=self.msg,fg='Green')
if __name__=="__main__":
    root = Tk()
    obj=QRCode(root)
    root.mainloop()