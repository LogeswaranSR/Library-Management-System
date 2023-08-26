# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:01:55 2023

@author: Loges
"""

from tkinter import Button, Label, Entry, Radiobutton, LabelFrame
import tkinter as tkt
from basicclasses import LabelEntryPair
from lmsfunctions import insertbookdata, selectfn

class SearchBookPage:
    def __init__(self, root, db):
        self.root=root
        self.db=db
        self.clmn=tkt.IntVar()
        
        self.greeting=Label(self.root, text="Search a Book")
        self.f1=LabelFrame(self.root, text="Select any of the fields below")
        self.f2=LabelFrame(self.root)
        self.SearchButton=Button(self.root, text="Search", command=self.search)
        self.CancelButton=Button(self.root, text="Cancel", command=self.forget)
        
        Radiobutton(self.f1, text="Book Name", variable=self.clmn, value=1).grid(row=0, column=0)
        Radiobutton(self.f1, text="Book Code", variable=self.clmn, value=2).grid(row=0, column=1)
        Radiobutton(self.f1, text="Publisher", variable=self.clmn, value=3).grid(row=0, column=2)
        Radiobutton(self.f1, text="Genre", variable=self.clmn, value=4).grid(row=0, column=3)
        
        self.value=Entry(self.f2, width=100, borderwidth=5)
        self.details=None
        
    def initialize(self):
        self.greeting.grid(row=0, column=0, columnspan=2)
        self.f1.grid(row=1, column=0, columnspan=2)
        self.f2.grid(row=2, column=0, columnspan=2)
        self.SearchButton.grid(row=3, column=0)
        self.CancelButton.grid(row=3, column=1)
        self.value.pack()
        
    def forget(self):
        self.greeting.grid_forget()
        self.f1.grid_forget()
        self.f2.grid_forget()
        self.SearchButton.grid_forget()
        self.CancelButton.grid_forget()
        if self.details:
            self.details.grid_forget()
        
    def search(self):
        typeval=self.clmn.get()
        searchval=self.value.get()
        printstr=selectfn(self.db, 'book b,copies c', typeval, searchval)
        if self.details!=None:
            self.details.grid_forget()
        self.details=Label(self.root, text=printstr)
        self.details.grid(row=4, column=0, columnspan=2)
        
class InsertBookPage:
    def __init__(self, root, db):
        self.root=root
        self.db=db
        self.greeting=Label(self.root, text="Insert a Book")
        self.frame=LabelFrame(self.root)
        
        self.bname=LabelEntryPair(self.frame, text="Book Name:")
        self.aname=LabelEntryPair(self.frame, text="Author Name:")
        self.publisher=LabelEntryPair(self.frame, text="Publisher:")
        self.bcode=LabelEntryPair(self.frame, text="Book Code:")
        self.price=LabelEntryPair(self.frame, text="Price")
        self.shelfcode=LabelEntryPair(self.frame, text="Shelf Code")
        self.totalcopies=LabelEntryPair(self.frame, text="Total Copies")
        self.availablecopies=LabelEntryPair(self.frame, text="Available Copies")
        
        self.SubmitButton=Button(self.root, text='Submit', command=self.insert)
        self.CancelButton=Button(self.root, text="Cancel", command=self.forget)
        
    def initialize(self):
        self.greeting.grid(row=0, column=0, columnspan=2)
        self.frame.grid(row=1, column=0, columnspan=2)
        self.SubmitButton.grid(row=2, column=0)
        self.CancelButton.grid(row=2, column=1)
        
        self.bname.grid(row=0)
        self.aname.grid(row=1)
        self.publisher.grid(row=2)
        self.bcode.grid(row=3)
        self.price.grid(row=4)
        self.shelfcode.grid(row=5)
        self.totalcopies.grid(row=6)
        self.availablecopies.grid(row=7)
        
    def insert(self):
        bn=self.bname.get()
        an=self.aname.get()
        publ=self.publisher.get()
        bc=self.bcode.get()
        pr=self.price.get()
        scode=self.shelfcode.get()
        cps=self.totalcopies.get()
        avblcps=self.availablecopies.get()
        stat=insertbookdata(self.db, bn, an, bc, publ, pr, scode, cps, avblcps)
        if stat:
            tkt.messagebox.showinfo(title='Success', message="Book Inserted Successfully!!!")
        else:
            tkt.messagebox.showerror(title="Error", message="Some error Occured!!\nTry Again")
    
    def forget(self):
        self.greeting.grid_forget()
        self.frame.grid_forget()
        self.SubmitButton.grid_forget()
        self.CancelButton.grid_forget()
        
        
        
class ChangeBookInfoPage:
    def __init__(self, root, csr):
        self.root=root
        
class LendReturnBookPage:
    def __init__(self, root, csr):
        self.root=root
        
if __name__=='__main__':
    from basicclasses import Database
    db=Database(host='localhost',user='root',passwd='14061703', database="library")
    root=tkt.Tk()
    sample=SearchBookPage(root, db)
    sample.initialize()
    root.mainloop()
    db.close()
    