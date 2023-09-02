# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:01:55 2023

@author: Loges
"""

from tkinter import Button, Label, Entry, Radiobutton, LabelFrame
import tkinter as tkt
from basicclasses import LabelEntryPair
import lmsfunctions as lf
import lmstable as tb

class SearchBookPage:
    def __init__(self, root, db):
        self.root=root
        self.db=db
        self.clmn=tkt.IntVar()
        
    def declare(self, mainpage):
        self.greeting=Label(self.root, text="Search a Book")
        self.f1=LabelFrame(self.root, text="Select any of the fields below")
        self.f2=LabelFrame(self.root)
        self.SearchButton=Button(self.root, text="Search", command=self.search)
        self.CancelButton=Button(self.root, text="Cancel", command=lambda: self.back(mainpage))
        
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
        if self.details!=None:
            self.details.grid_forget()
        data, tbl=lf.selectfn(self.db, 'book b,copies c', typeval, searchval)
        if(type(data)==str):
            self.details=Label(self.root, text=data)
        else:
            self.details=tb.tableframe(data, self.root, self.db, tbl)
        self.details.grid(row=4, column=0, columnspan=2)
        
    def back(self, mainpage):
        self.forget()
        mainpage.initialize()
        
class InsertBookPage:
    def __init__(self, page, root, db):
        self.mainpage=page
        self.root=root
        self.db=db
        
    def declare(self):
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
        self.CancelButton=Button(self.root, text="Cancel", command=self.back)
        
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
        details=(bn, an, bc, publ, pr, scode, cps, avblcps)
        stat=lf.insertbookdata(self.db, details)
        if stat:
            tkt.messagebox.showinfo(title='Success', message="Book Inserted Successfully!!!")
            self.back()
        else:
            tkt.messagebox.showerror(title="Error", message="Some error Occured!!\nTry Again")
    
    def forget(self):
        self.greeting.grid_forget()
        self.frame.grid_forget()
        self.SubmitButton.grid_forget()
        self.CancelButton.grid_forget()
        
    def back(self):
        self.forget()
        self.mainpage.initialize()
        
class ChangeBookInfoPage:
    def __init__(self, mainpage, root, db):
        self.mainpage=mainpage
        self.root=root
        self.db=db
        
    def declare(self):
        self.greeting=Label(self.root, text="Change Book Details")
        self.info=Label(self.root, text="Enter Book Code", anchor=tkt.W)
        self.bcode=LabelEntryPair(self.root, "Book Code:")
        self.fetchButton=Button(self.root, text="Fetch", command=self.fetch)
        self.cancelButton=Button(self.root, text="Cancel", command=self.back)
        self.stage=1
        self.bookdetails=None
        
        self.frame=LabelFrame(self.root, text="Book details")
        self.details=[None,
        LabelEntryPair(self.frame, "Book Name:"),
        LabelEntryPair(self.frame, "Author:"),
        LabelEntryPair(self.frame, "Publisher:"),
        LabelEntryPair(self.frame, "Price:"),
        LabelEntryPair(self.frame, "Shelf Code:"),
        LabelEntryPair(self.frame, "Total Copies:")
        ]
        self.updateButton=Button(self.root, text="Update", command=self.update)

        
    def initialize(self):
        self.greeting.grid(row=0, column=0, columnspan=2)
        self.info.grid(row=1, column=0, columnspan=2)
        self.bcode.grid(2)
        self.fetchButton.grid(row=3, column=0)
        self.cancelButton.grid(row=3, column=1)
        
    def fetch(self):
        bcode=self.bcode.get()
        self.bookdetails, tbl=lf.selectfn(self.db, 'book b,copies c', 2, bcode)
        self.bookdetails=self.bookdetails[0]
        print(self.bookdetails)
        if(type(self.bookdetails)==str):
            tkt.messagebox.showerror(title="Book not found",message=self.bookdetails)
        else:
            self.display()
            
    def display(self):
        self.forget()
        self.stage=2
        self.frame.grid(row=1, column=0, columnspan=2)
        self.updateButton.grid(row=2, column=0)
        self.cancelButton.grid(row=2, column=1)
        
        self.details[0]=LabelEntryPair(self.frame, "Book Code:")
        for i in range(len(self.details)):
            self.details[i].grid(i)
            self.details[i].set(self.bookdetails[i])
        
        
    def update(self):
        changes={}
        cols=["BCODE","BNAME","AUTHOR","PUBL","PRICE","SLF","TCP"]
        code=self.bookdetails[0]
        for i in range(len(self.details)):
            temp=self.details[i].get()
            if temp!=self.bookdetails[i]:
                changes[cols[i]]=temp
        stat=lf.changedata(self.db, changes, code)
        if stat:
            tkt.messagebox.showinfo(title='Success', message="Book Updated Successfully!!!")
            self.back()
        else:
            tkt.messagebox.showerror(title="Error", message="Some error Occured!!\nTry Again")
        
    def back(self):
        self.forget()
        if self.mainpage:
            self.mainpage.initialize()
        
    def forget(self):
        if self.stage==1:
            self.info.grid_forget()
            self.bcode.forget()
            self.fetchButton.grid_forget()
        else:
            self.frame.grid_forget()
            self.greeting.grid_forget()
            self.updateButton.grid_forget()
        self.cancelButton.grid_forget()
        
class LendReturnBookPage:
    def __init__(self, root, db):
        self.root=root
        self.db=db
        
if __name__=='__main__':
    from basicclasses import Database
    db=Database(host='localhost',user='root',passwd='14061703', database="library")
    root=tkt.Tk()
    sample=ChangeBookInfoPage(None, root, db)
    sample.declare()
    sample.initialize()
    root.mainloop()
    db.close()
    