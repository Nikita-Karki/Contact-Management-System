from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
from sqlite3 import*
import home_window
class loginwindow(Tk):
    def __init__(self,*args,**kwarg):
        Tk.__init__(self,*args,**kwarg)
            
        self.title("contact")
        self.geometry("800x600")

        style=Style()
        style.configure("Header.TFrame", background='skyblue')
        
        Header_frame=Frame(self,style='Header.TFrame')
        Header_frame.pack(fill=X)


        style.configure("header.TLabel",background="skyblue", foreground="grey",font=('serif',25))
        

        hed=Label(Header_frame,text="My contact book",style="Header.TLabel")
        hed.pack(pady=10)

        style.configure('content.TFrame', background="sky blue")

        content_frame=Frame(self,style='content.TFrame')
        content_frame.pack(fill=BOTH, expand=TRUE)

        login_frame=Frame(content_frame,style='content.TFrame')
        login_frame.place(relx=0.5,rely=0.5,anchor=CENTER)

        style.configure("login.TLabel")

        user_label=Label(login_frame ,text="Username:",font=('serif',15),style='login.TLabel')
        user_label.grid(row=0,column=0)

        self.user_entry=Entry(login_frame,font=('serif',15))
        self.user_entry.grid(row=0,column=1,pady=5)

        
        user_password=Label(login_frame ,text="Password:",font=('serif',15),style='login.TLabel')
        user_password.grid(row=1,column=0,pady=5)
        
        style.configure("login.TButton",font=("serif",15))

        self.password_entry=Entry(login_frame,font=('serif',15), show='*')
        self.password_entry.grid(row=1,column=1,pady=5)

    

        login_button=Button(login_frame,text="login",style='login.TButton',width=15, command=self.login_button_click)
        login_button.grid(row=2,column=1,pady=5)
        login_button.bind('<Return>',self.login_button_click)

    def login_button_click(self,event=None):
        con=connect('contact.contact.db')
        cur=con.cursor()
        cur.execute("select *from login where username=? and password=?",(self.user_entry.get(),self.password_entry.get()))
        row=cur.fetchone()
        if row is not None:
            self.destroy()
            home_window.Homewindow()
        else:
            messagebox.showerror("error message","invalid id or password")
            
            

if __name__=='__main__':
    lw=loginwindow()
    lw.mainloop()
 
