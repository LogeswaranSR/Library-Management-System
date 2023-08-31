# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:06:41 2023

@author: Loges
"""
import time
import table as tb

def login(usrnm, psswd, lgtp, db,n=0):
    '''Function to login to the management system'''
    status, name, emailid = checkacc(db, usrnm, psswd=psswd, acctype=lgtp)
    if not status:
        n=n+1
        if(n==10):
            name="\n10 Unsuccessful Login Attempts"
        else:
            name=None
    return status,name,emailid,n

def checkacc(db, usrnm, acctype=None, ui=None, psswd=None):
    if acctype==1:
        tabledata=db.tblaccess('mbrlgnid')
    elif acctype==2:
        tabledata=db.tblaccess('emplgnid')
    else:
        tabledata=db.tblaccess(ui.tblnm)
    status=False
    name=emailid=None
    for dtls in tabledata:
        condn=(usrnm==dtls[2])
        if psswd!=None:
            condn=condn and (psswd==dtls[3])
        if condn:
            status=True
            name=dtls[0]
            emailid=dtls[1]
            break
    return status, name, emailid

def changeaccdet(db,ui,name,usrnm,email):
    '''Function to change account details of the user'''
    chk=(usrnm==ui.lgid)
    data=checkacc(db, ui.lgid, ui=ui)
    print(data)
    chk = chk and (name==data[1]) and (email==data[2])
    if chk:
        db.conn.commit()
        return True, "No change"
    condn='USRNM=\'{0}\''.format(ui.lgid)
    if not (usrnm==ui.lgid):
        alreadyExists, name, emailid = checkacc(db, usrnm, ui=ui)
        if alreadyExists:
            return False, "Username Already exists\nPlease Try another Username"
    cnm=("name","emailid","usrnm")
    cmd='update {0} set {1}=\'{2}\',{3}=\'{4}\',{5}=\'{6}\' where {7};'.format(ui.tblnm,cnm[0],name,cnm[1],email,cnm[2],usrnm,condn)
    db.execute(cmd)
    ui.name=name
    ui.lgid=usrnm
    ui.email=email
    return True, "Account Details Changed"

def changepassword(db, ui, oldps, newps):
    condn='USRNM=\'{0}\''.format(ui.lgid)
    sameOldps, __, _ = checkacc(db, ui.lgid, psswd=oldps, ui=ui)
    if not sameOldps:
        return False, "Old password"
    cmd='update {0} set psswd=\'{1}\' where {2};'.format(ui.tblnm,newps,condn)
    db.execute(cmd)
    return True, "Password Changed Successfully!!!"
