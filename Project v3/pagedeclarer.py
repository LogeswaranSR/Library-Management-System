# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:00:43 2023

@author: Loges
"""

import menupages as mpgs
from accountpage import CreateNewAccountPage as CNAPage
import tkinter as tkt

def caprocess(root, db):
    top=tkt.Toplevel(root)
    cna=CNAPage(top, db)
    cna.initialize()
    cna.start()
    
def searchbookprocess(page, root, db):
    page.forget()
    sbpage=mpgs.SearchBookPage(root, db)
    sbpage.declare()
    sbpage.initialize()