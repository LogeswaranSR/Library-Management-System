# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:55:59 2023

@author: Loges
"""

from tabulate import tabulate
from tkinter import LabelFrame, Label

def tblaccess(cursor,tblnm,condn=None,cname='*'):
    '''Function to get resultset from Mysql'''
    if condn==None:
        str='select {0} from {1};'.format(cname,tblnm)
    else:
        str='select {0} from {1} where {2};'.format(cname,tblnm,condn)
    cursor.execute(str)
    tbl=cursor.fetchall()
    return tbl
def tabledetails(csr,table):
    '''Function to get name of the table columns'''
    cmd='desc '+table+';'
    csr.execute(cmd)
    data=csr.fetchall()
    data1=[]
    data2=[]
    for row in data:
        data1.append(row[0])
        data2.append(str(row[1]))
    return data1,data2
def tabledetails2(db, tbl):
    cname=db.tabledetails(tbl[0])
    cname2=db.tabledetails(tbl[1])
    cname.append(cname2[1])
    cname.append(cname2[2])
    return cname
def tabledisplay(data,db,tbl):
    '''Function to display the data obtained in the form of a proper table'''
    if 'list' in str(type(tbl)):
        cname = tabledetails2(db, tbl)
    else:
        cname = db.tabledetails(tbl)
    printstr=tabulate(data, cname, 'grid')
    print(printstr)
    return printstr
def tableframe(data, root, db, tbl):
    frame=LabelFrame(root)
    cname=tabledetails2(db, tbl)
    for i in range(len(cname)):
        lbl=Label(frame, text=cname[i])
        lbl.grid(row=0, column=i)
    r=1
    for row in data:
        for i in range(len(row)):
            lbl=Label(frame, text=row[i])
            lbl.grid(row=r, column=i)
        r+=1
    return frame
