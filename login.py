from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import messagebox
import os
class login:
    def __init__(self,root):
        self.root=root
        self.root.title('Login System | Developed SAURABH KAPOOR | M.R.S Technology, Varanasi')
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False,False)
        #=========BG Image===========
        self.bg=ImageTk.PhotoImage(file='images/login.png')
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #==============login Frame==============
        Frame_login=Frame(self.root,bg='white')
        Frame_login.place(x=425,y=210,height=340,width=500)


        title=Label(Frame_login,text='Login Here',font=('Impact',35,'bold'),fg='#d77337',bg='white').place(x=90,y=30) 
        desc=Label(Frame_login,text='Accountant Employee Login Area',font=('Goudy Old Style',15,'bold'),fg='#d25d17',bg='white').place(x=90,y=100)

        lbl_user=Label(Frame_login,text='Username',font=('Goudy',15,'bold'),fg='gray',bg='white').place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=('times new roman',15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text='Password',font=('Goudy',15,'bold'),fg='gray',bg='white').place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=('times new roman',15),bg='lightgray',show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        #forget_btn=Button(Frame_login,text='Forget Password?',cursor='hand2',bg='white',fg='#d77337',bd=0,font=('times new roman',12)).place(x=90,y=280)
        login_btn=Button(self.root,command=self.login_function,cursor='hand2',text='Login',bg='#d77337',fg='white',font=('times new roman',20)).place(x=685,y=500,width=180,height=40)
        
    def login_function(self):
        if self.txt_pass.get()=='' or self.txt_user.get()=='':
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_pass.get()!='000000' and self.txt_user.get()=='Saurabh Kapoor':
            messagebox.showinfo("Welcome",f'Welcome {self.txt_user.get()}')
            self.redirect()
        else:
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)

    def redirect(self):
        self.root.destroy()
        os.system("python employee.py")    
       

root=Tk()
obj=login(root)
root.mainloop()        