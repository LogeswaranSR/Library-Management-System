# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:06:41 2023

@author: Loges
"""
import time
import table as tb

def login(usrnm, psswd, lgtp, db,n=0):
    '''Function to login to the management system'''
    status, name = checkacc(db, lgtp, usrnm, psswd)
    if not status:
        n=n+1
        if(n==10):
            name="\n10 Unsuccessful Login Attempts"
        else:
            name=None
    return status,name,n
def checkacc(db, acctype, usrnm, psswd):
    if acctype==1:
        tabledata=db.tblaccess('mbrlgnid')
    elif acctype==2:
        tabledata=db.tblaccess('emplgnid')
    status=False
    name=None
    for dtls in tabledata:
        condn=(usrnm==dtls[2])
        if psswd!=None:
            psswd=psswd and (psswd==dtls[3])
        if condn:
            status=True
            name=dtls[0]
            break
    return status, name
def changeaccdet(cursor,mycon,lgntp,usrnm,tp):
    '''Function to change account details of the user'''
    cursor.execute('Use loginid;')
    if lgntp=='M':
        tblnm='mbrlgnid'
    if lgntp=='E':
        tblnm='emplgnid'
    condn='USRNM=\'{0}\''.format(usrnm)
    if tp not in 'pP':
        data=tb.tblaccess(cursor,tblnm,condn,'name,emailid,usrnm')
        tb.tabledisplay(data,cursor,tblnm)
        cnm=input("Enter the column of data to be changed:")
        data=input("Enter the new data:")
        cmd='update {0} set {1}=\'{2}\' where {3};'.format(tblnm,cnm,data,condn)
        cursor.execute(cmd)
        mycon.commit()
        time.sleep(1)
        print("Account Details Changed Successfully!!\n")
    else:
        oldps=input("Enter your old password:")
        newps=input("Enter your new password:")
        rnwps=input("Re-enter your new password:")
        if newps!=rnwps:
            print("Password typed is wrong")
            print("Try Again\n")
            time.sleep(1)
            changeaccdet(cursor,lgntp,usrnm,tp)
        else:
            cmd='update {0} set psswd=\'{1}\' where {2};'.format(tblnm,newps,condn)
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Password Changed Successfully\n")
    cursor.execute('Use library;')