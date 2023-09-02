# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:28:25 2023

@author: Loges
"""

from tkinter import Button, Label, Radiobutton, LabelFrame
import tkinter as tkt
import account as ac
from basicclasses import LabelEntryPair

class CreateNewAccountPage:
    
    def __init__(self, root, db):
        self.root=root
        self.name=self.username=self.emailid=self.password=None
        self.logintype=None
        self.db=db
        
        self.text1 = Label(self.root, text="Create new account!!")
        self.accounttype = tkt.IntVar()
        
        self.frame = LabelFrame(self.root, text="Enter the Following Details")
        Radiobutton(self.frame, text="Member", variable=self.accounttype, value=1).grid(row=0, column=0)
        Radiobutton(self.frame, text="Employee", variable=self.accounttype, value=2).grid(row=0, column=1)
        self.Name  = LabelEntryPair(self.frame, text="Name:", width=50, borderwidth=5)
        self.Email = LabelEntryPair(self.frame, text="Email ID:", width=50, borderwidth=5)
        self.usrnm = LabelEntryPair(self.frame, text="User ID:", width=50, borderwidth=5)
        self.psswd = LabelEntryPair(self.frame, text="Password:", width=50, borderwidth=5)
        
        self.CreateButton = Button(self.root, text="Create", command=self.createaccount)
        self.ExitButton = Button(self.root, text="Cancel", command=self.root.destroy)
        
    def initialize(self):
        self.text1.grid(row=0, column=0, columnspan=2)
        self.frame.grid(row=1, column=0, columnspan=2)
        self.CreateButton.grid(row=2, column=0, padx=50, pady=25)
        self.ExitButton.grid(row=2, column=1, padx=50, pady=25)
        
        self.Name.grid(row=1)
        self.Email.grid(row=2)
        self.usrnm.grid(row=3)
        self.psswd.grid(row=4)
        
    def start(self):
        self.root.mainloop()
        
    def createaccount(self):
        self.name=self.Name.get()
        self.emailid=self.Email.get()
        self.username=self.usrnm.get()
        self.password=self.psswd.get()
        
        status, name = ac.checkacc(self.db, self.username, psswd=None, acctype=self.accounttype.get())
        if status:
            tkt.messagebox.showwarning("Already Exists","Username Already Exists\nPlease try another username")
        else:
            if self.accounttype.get()==1:
                tblnm='mbrlgnid'
            else:
                tblnm='emplgnid'
            cmd='insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\');'.format(tblnm,self.name,self.emailid,self.username,self.password)
            self.db.execute(cmd)
            tkt.messagebox.showinfo("Success","Account Successfully Added\nLogin with the given credentials to access the account")
            self.root.destroy()
            
class ChangeAccountDetailsPage:
    def __init__(self, root, db, ui):
        self.root=root
        self.db=db
        self.ui=ui
        
        self.greeting=Label(self.root, text="User Account Details")
        self.frame=LabelFrame(self.root)
        self.name=LabelEntryPair(self.frame, text="Name")
        self.email=LabelEntryPair(self.frame, text="Email")
        self.usrnm=LabelEntryPair(self.frame, text="Username:")
        self.updateButton=Button(self.root, text="Update", command=self.update)
        self.cancelButton=Button(self.root, text="Cancel", command=self.root.destroy)
        
    def initialize(self):
        self.greeting.grid(row=0, column=0, columnspan=2)
        self.frame.grid(row=1, column=0, columnspan=2)
        self.updateButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)
        self.fetchdata()
        self.name.grid(row=0)
        self.email.grid(row=1)
        self.usrnm.grid(row=2)
        
    def fetchdata(self):
        condn='USRNM=\'{0}\''.format(self.ui.lgid)
        data=self.db.tblaccess(self.ui.tblnm,condn,'name,emailid,usrnm')
        self.name.set(data[0][0])
        self.email.set(data[0][1])
        self.usrnm.set(data[0][2])
        
    def update(self):
        name=self.name.get()
        email=self.email.get()
        usrnm=self.usrnm.get()
        stat, msg = ac.changeaccdet(self.db, self.ui, name, usrnm, email)
        if not stat:
            tkt.messagebox.showerror(title="Error!", message=msg)
            self.initialize()
        else:
            tkt.messagebox.showinfo(title="Success", message=msg)
            self.root.destroy()
            
    def start(self):
        self.root.mainloop()
        
        
class ChangePasswordPage:
    def __init__(self, root, db, ui):
        self.root=root
        self.db=db
        self.ui=ui
        
        self.greeting=Label(self.root, text="Change Password")
        self.frame=LabelFrame(self.root)
        self.oldps=LabelEntryPair(self.frame, text="Old Password:")
        self.newps=LabelEntryPair(self.frame, text="New Password:")
        self.rnewps=LabelEntryPair(self.frame, text="Re-enter New Password")
        self.changeButton=Button(self.root, text="Change Password", command=self.change)
        self.cancelButton=Button(self.root, text="Cancel", command=self.root.destroy)
        
    def initialize(self):
        self.greeting.grid(row=0, column=0, columnspan=2)
        self.frame.grid(row=1, column=0, columnspan=2)
        self.changeButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)
        
        self.oldps.grid(row=0)
        self.newps.grid(row=1)
        self.rnewps.grid(row=2)
        
    def change(self):
        old=self.oldps.get()
        new=self.newps.get()
        rnew=self.rnewps.get()
        if new!=rnew:
            self.changeButton.grid_forget()
            self.changeButton=Button(self.root, text="Change Password", command=self.change, state='disabled')
            self.changeButton.grid(row=2, column=0)
            tkt.messagebox.showerror(title="Password doesn't match", message="New Password and Re-enter New Password doesn't match\nPlease Try Again")
            self.changeButton.grid_forget()
            self.changeButton=Button(self.root, text="Change Password", command=self.change)
            self.changeButton.grid(row=2, column=0)
            self.initialize()
        else:
            stat, msg = ac.changepassword(self.db, self.ui, old, new)
            if not stat:
                tkt.messagebox.showerror(title="Password doesn't match", message="Old Password mismatch\nPlease Try Again")
                self.initialize()
            else:
                tkt.messagebox.showinfo(title="Success!!", message=msg)
                self.root.destroy()
    
    def start(self):
        self.root.mainloop()

            
if __name__=='__main__':
    import basicclasses as bc
    db=bc.Database(host='localhost',user='root',passwd='14061703', database='loginid')
    ui=bc.User('abcxyz', 'abcxyz', 2, 'abcxyz@gmail.com')
    root=tkt.Tk()
    top=tkt.Toplevel(root)
    sample=ChangePasswordPage(top, db, ui)
    sample.initialize()
    sample.start()
    del db
    del ui