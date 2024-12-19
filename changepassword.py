from tkinter import*
from tkinter.ttk import*
from sqlite3 import*
from tkinter import messagebox


class ChangePassword(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)

        s=Style()
        s.configure("TFrame",background='light yellow')
        s.configure("TLabel",background='white',font=('Arial',15))
        s.configure("TButton",width=15,font=("arial",15))


        self.place(relx=.5,rely=.5,anchor=CENTER)

        old_password_label=Label(self,text="old Password:")
        old_password_label.grid(row=0,column=0,sticky=E)

        self.old_password_entry=Entry(self,font=('arial',15),show='*')
        self.old_password_entry.grid(row=0,column=1,pady=5)

        new_password_label=Label(self,text="new password:")
        new_password_label.grid(row=1,column=0,sticky=E)

        self.new_password_entry=Entry(self,font=('arial',15),show='*')
        self.new_password_entry.grid(row=1,column=1,pady=5)

        confirm_password_label=Label(self,text="confirm password:")
        confirm_password_label.grid(row=2,column=0,sticky=E)

        self.confirm_password_entry=Entry(self,font=('arial',15),show='*')
        self.confirm_password_entry.grid(row=2,column=1,pady=5)

        change_password_button=Button(self,text="change password",command=self.change_password_button_click)
        change_password_button.grid(row=3,column=0,columnspan=2)

    def change_password_button_click(self):
            con=connect('contact.contact.db')
            cur=con.cursor()
            cur.execute("select * from login where password=?",(self.old_password_entry.get(),))
            record=cur.fetchone()
            if record is not None:
                if self.new_password_entry.get()==self.confirm_password_entry.get():
                    cur.execute("update login set password=? where password=?",(self.new_password_entry.get(),self.old_password_entry.get()))
                    con.commit()
                    messagebox.showinfo('Success Message','Password is changed successfully') 
                else:
                    messagebox.showerror("Error Message","new password and confirm password are not march!")
                    
            else:
                messagebox.showerror("Error Message","Incorrect old password")
        
        
