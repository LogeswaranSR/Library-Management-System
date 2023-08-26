# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:38:33 2023

@author: Loges
"""

from tkinter import Button, Label, LabelFrame
import tkinter as tkt

class MainMenuPage:
    def __init__(self, ui, db):
        self.root=tkt.Tk()
        self.ui=ui
        self.db=db
        
    def declare(self, lst):
        self.Label=Label(self.root, text="Main Page")
        self.frame=LabelFrame(self.root)
        self.ChangeADButton=Button(self.root, text="Change Account Details")
        self.ChangePasswordButton=Button(self.root, text="Change Password")
        self.LogoutButton=Button(self.root, text="Logout", command=self.sample)
        
        self.SearchBookButton=Button(self.frame, text="Search a Book", command=lst[1])
        self.RequestBookButton=Button(self.frame,text="Request a Book")
        self.RenewBookButton=Button(self.frame, text="Renew a Book")
        self.ReturnBookButton=Button(self.frame, text="Return a Book")
        
        if self.ui.lgtp==2:
            self.RequestBookButton=Button(self.frame, text="Lend a Book")
            self.InsertBookButton=Button(self.frame, text="Insert a New Book")
            self.ChangeBDButton=Button(self.frame, text="Change a Book Data")
            self.CreateNewMemberButton=Button(self.frame, text="Create a New Member Account", command=lst[0])
        
    
    def initialize(self):
        self.Label.grid(row=0, column=0, columnspan=3)
        self.frame.grid(row=1, column=0, columnspan=3)
        self.ChangeADButton.grid(row=2, column=0, padx=50, pady=10)
        self.ChangePasswordButton.grid(row=2, column=1, padx=50, pady=10)
        self.LogoutButton.grid(row=2, column=2, padx=50, pady=10)
        
        self.SearchBookButton.grid(row=0, column=1, padx=50, pady=10)
        self.RequestBookButton.grid(row=1, column=0, padx=50, pady=10)
        self.RenewBookButton.grid(row=1, column=1, padx=50, pady=10)
        self.ReturnBookButton.grid(row=1, column=2, padx=50, pady=10)
        
        if self.ui.lgtp==2:
            self.InsertBookButton.grid(row=0, column=0, padx=50, pady=10)
            self.ChangeBDButton.grid(row=0, column=2, padx=50, pady=10)
            self.CreateNewMemberButton.grid(row=2, column=0, columnspan=3, padx=50, pady=10)
        
    def forget(self):
        self.Label.grid_forget()
        self.frame.grid_forget()
        self.ChangeADButton.grid_forget()
        self.ChangePasswordButton.grid_forget()
        self.LogoutButton.grid_forget()
        
    def start(self):
        self.root.mainloop()
        
    def sample(self):
        self.forget()
        # self.declare()
        self.initialize()
        

if __name__=='__main__':
    import mysql.connector as sqltor
    from basicclasses import User, Database
    mycon=sqltor.connect(host='localhost',user='root',passwd='14061703')
    csr=mycon.cursor()
    ui=User('abcxyz','abcxyz',2)
    page=MainMenuPage(csr, ui)
    page.declare()
    page.initialize()
    page.start()
    mycon.close()
        