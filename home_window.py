from tkinter import*
from tkinter.ttk import*
import login
import changepassword
import managecontact

class Homewindow(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)


        self.title("home")
        self.state("zoomed")

        s=Style()
        s.configure("Header.TFrame",background='light pink')

        header_frame=Frame(self, style='Header.TFrame',height=50)
        header_frame.pack(fill=X)

        s.configure("Header.TLabel",background='light pink',font=('arial',25))


        header_label=Label(header_frame,text='My Contact Book',style='Header.TLabel')
        header_label.pack(pady=10)
        
        navigation=Frame(self,style='Header.TFrame')
        navigation.pack(side=LEFT,fill=Y)

        s.configure("navigation.TButton",width=30,font=('arial',12))

        manage_contact_button=Button(navigation,text="manage contact" ,style="navigation.TButton",command=self.manage_contacts_button_click)
        manage_contact_button.pack(ipady=10,pady=1)

        
        manage_password_button=Button(navigation,text="change password",style="navigation.TButton",command=self.change_password_button_click)
        manage_password_button.pack(ipady=10,pady=1)


        
        manage_logout_button=Button(navigation,text="logout",style="navigation.TButton",command=self.logout_button_click)
        manage_logout_button.pack(ipady=10,pady=1)


        s.configure("Navigation.TFrame",background='light yellow')
        self.content_frame=Frame(self,style="Navigation.TFrame")
        self.content_frame.pack(fill=BOTH,expand=TRUE)

        managecontact.ManagecontactsFrame(self.content_frame)

    def logout_button_click(self):
        self.destroy()
        login.loginwindow()

    def change_password_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
        changepassword.ChangePassword(self.content_frame)

    def manage_contacts_button_click(self):
        for inner_frame in self.content_frame.winfo_children():
            inner_frame.destroy()
         
        managecontact.ManagecontactsFrame(self.content_frame)
            

        
