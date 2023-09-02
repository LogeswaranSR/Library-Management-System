# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:00:43 2023

@author: Loges
"""

import menupages as mpgs
import accountpage as acc
import tkinter as tkt

def caprocess(root, db):
    top=tkt.Toplevel(root)
    cna=acc.CreateNewAccountPage(top, db)
    cna.initialize()
    cna.start()
    del cna
    
def searchbookprocess(page, root, db):
    page.forget()
    sbpage=mpgs.SearchBookPage(root, db)
    sbpage.declare(page)
    sbpage.initialize()
    
    
def insertbookprocess(page, root, db):
    page.forget()
    ibpage=mpgs.InsertBookPage(page, root, db)
    ibpage.declare()
    ibpage.initialize()
    
def changebookinfoprocess(page, root, db):
    page.forget()
    cbinfopage=mpgs.ChangeBookInfoPage(page, root, db)
    cbinfopage.declare()
    cbinfopage.initialize()
    
    
def changeaccdetprocess(root, db, ui):
    top=tkt.Toplevel(root)
    cad=acc.ChangeAccountDetailsPage(top, db, ui)
    cad.initialize()
    cad.start()
    del cad
    
def changepasswordprocess(root, db, ui):
    top=tkt.Toplevel(root)
    cpwd=acc.ChangePasswordPage(top, db, ui)
    cpwd.initialize()
    cpwd.start()
    del cpwd