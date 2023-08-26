# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 21:28:25 2023

@author: Loges
"""

from tkinter import Button, Label, Entry, Radiobutton, LabelFrame
import tkinter as tkt
from account import checkacc
from basicclasses import LabelEntryPair

class CreateNewAccountPage:
    
    def __init__(self, root, csr, conn):
        self.root=root
        self.name=self.username=self.emailid=self.password=None
        self.logintype=None
        self.csr=csr
        self.conn=conn
        
        self.text1 = Label(self.root, text="Create new account!!")
        self.accounttype = tkt.IntVar()
        
        self.frame = LabelFrame(self.root, text="Enter the Following Details")
        Radiobutton(self.frame, text="Member", variable=self.accounttype, value=1).grid(row=0, column=0)
        Radiobutton(self.frame, text="Employee", variable=self.accounttype, value=2).grid(row=0, column=1)
        self.Name  = LabelEntryPair(self.frame, text="Name:", width=50, borderwidth=5)
        self.Email = Entry(self.frame, text="Email ID:", width=50, borderwidth=5)
        self.usrnm = Entry(self.frame, text="User ID:", width=50, borderwidth=5)
        self.psswd = Entry(self.frame, text="Password:", width=50, borderwidth=5)
        
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
        
        status, name = checkacc(self.csr, self.accounttype.get(), self.username, None)
        if status:
            tkt.messagebox.showwarning("Already Exists","Username Already Exists\nPlease try another username")
        else:
            if self.accounttype.get()==1:
                tblnm='mbrlgnid'
            else:
                tblnm='emplgnid'
            cmd='insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\');'.format(tblnm,self.name,self.emailid,self.username,self.password)
            self.csr.execute(cmd)
            self.conn.commit()
            tkt.messagebox.showinfo("Success","Account Successfully Added\nLogin with the given credentials to access the account")
            self.root.destroy()
            
class ChangeAccountDetailsPage:
    def __init__(self, root, csr):
        self.root=root
        
class ChangePasswordPage:
    def __init__(self, root, csr):
        self.root=root
            
if __name__=='__main__':
    import mysql.connector as sqltor
    mycon=sqltor.connect(host='localhost',user='root',passwd='14061703')
    csr=mycon.cursor()
    csr.execute('Use loginid;')
    root=tkt.Tk()
    sample=CreateNewAccountPage(root, csr, mycon)
    sample.initialize()
    sample.start()
    mycon.close()