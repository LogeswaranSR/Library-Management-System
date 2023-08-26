# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:36:29 2023

@author: Loges
"""

from tkinter import Tk, Button, Label, Entry, Radiobutton, LabelFrame
import tkinter as tkt
from time import sleep
from createaccountpage import CreateNewAccountPage as CNAPage
from account import login

class LoginPage:
    n=0
    def __init__(self, cursor, mycon):
        self.root=Tk()
        # root.geometry("1920x1080+0+0")
        self.csr=cursor
        self.conn=mycon
        self.root.title("Login Page")
        self.frame=LabelFrame(self.root, text="Login Details")
        self.logintype=tkt.IntVar()
        
        self.Greeting = Label(self.root, text="Welcome to Sairam Vidyalaya's Library!!!!")
        self.Text1 = Label(self.root, text="Please Login")
        Radiobutton(self.frame, text="Member", variable=self.logintype, value=1).grid(row=0, column=0)
        Radiobutton(self.frame, text="Employee", variable=self.logintype, value=2).grid(row=0, column=1)
        self.Text2 = Label(self.frame, text="User ID:")
        self.usrnm = Entry(self.frame, width=50, borderwidth=5)
        self.Text3 = Label(self.frame, text="Password:")
        self.psswd = Entry(self.frame, width=50, borderwidth=5)
        self.Loginbutton = Button(self.root, text="Login", command=self.loginprocess)
        self.ExitButton = Button(self.root, text="Cancel", command=self.stop)
        self.CreateAccountButton = Button(self.root, text="Create new Account", command=self.caprocess)
        self.status=Label(self.root, text="Login Failed\nPlease Try Again")
        self.name=self.username=None
        self.loggedin=False
    
    def loginprocess(self):
        self.username=self.usrnm.get()
        password=self.psswd.get()
        lgtp=self.logintype.get()
        self.loggedin, self.name, LoginPage.n = login(self.username, password, lgtp, self.csr, LoginPage.n)
        if self.loggedin:
            self.status.grid_forget()
            self.status=Label(self.root, text="Login Success\n Redirecting")
            self.status.grid(row=5, column=0, columnspan=2, padx=50, pady=50)
            self.stop()
        elif LoginPage.n==10:
            LoginPage.n=0
            self.status.grid_forget()
            self.Loginbutton = Button(self.root, text="Login", command=self.loginprocess, state=tkt.DISABLED)
            self.Loginbutton.grid(row=3, column=0, padx=50, pady=50)
            tkt.messagebox.showwarning(title="Login Failed", message="10 Unsuccessful Attempts\nPlease Try Again after 10 seconds")
            sleep(10)
            self.Loginbutton = Button(self.root, text="Login", command=self.loginprocess)
            self.Loginbutton.grid(row=3, column=0, padx=50, pady=50)
        else:
            self.status.grid_forget()
            self.status=Label(self.root, text="Login Failed\nPlease Try Again")
            self.status.grid(row=5, column=0, columnspan=2, padx=50, pady=50)
            
    
    def initialize(self):
        self.Greeting.grid(row=0, column=0, columnspan=2)
        self.Text1.grid(row=1, column=0, columnspan=2)
        self.frame.grid(row=2, column=0, columnspan=2)
        self.Text2.grid(row=1, column=0)
        self.Text3.grid(row=2, column=0)
        self.usrnm.grid(row=1, column=1)
        self.psswd.grid(row=2, column=1)
        self.Loginbutton.grid(row=3, column=0, padx=50, pady=25)
        self.ExitButton.grid(row=3, column=1, padx=50, pady=25)
        self.CreateAccountButton.grid(row=4, column=0, columnspan=2, pady=50)
    
    def start(self):
        self.root.mainloop()
        return (self.loggedin, self.name, self.username, self.logintype.get())
        
    def stop(self):
        if self.loggedin:
            sleep(2)
        self.root.destroy()
        
    def caprocess(self):
        top=tkt.Toplevel()
        cna=CNAPage(top, self.csr, self.conn)
        cna.initialize()
        cna.start()
        
if __name__=='__main__':
    import mysql.connector as sqltor
    mycon=sqltor.connect(host='localhost',user='root',passwd='14061703')
    csr=mycon.cursor()
    csr.execute('Use loginid;')
    sample=LoginPage(csr, mycon)
    sample.initialize()
    sample.start()
    mycon.close()