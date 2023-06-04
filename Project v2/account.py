# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:06:41 2023

@author: Loges
"""
import time
import table as tb

def login(tabledata,n=0):
    '''Function to login to the management system'''
    print()
    lgid=input("Enter the id:")
    psswd=input("Enter the Password:")
    for dtls in tabledata:
        if(lgid==dtls[2])and(psswd==dtls[3]):
            time.sleep(1)
            print()
            print("Login Success\n")
            print('Welcome,',dtls[0])
            break
    else:
        time.sleep(1)
        print("\nLogin Failed")
        n=n+1
        if(n==10):
            print("\n10 Unsuccessful Login Attempts")
            time.sleep(1)
            print("Try again after 10 sec",end='')
            for i in range(10):
                time.sleep(1)
                print(end='.')
            login(tabledata)
        else:
            time.sleep(1)
            print('\nTry Again')
            login(tabledata,n)
    return lgid
def createacc(cursor,mycon):
    '''Function to create a new account(Both employee and member account)'''
    cursor.execute('Use loginid')
    acctype=input("Enter the type of account(E/M):")
    if acctype=='E':
        tblnm='emplgnid'
    elif acctype=='M':
        tblnm='mbrlgnid'
    else:
        print("Invalid Account type")
        print('Try Again\n')
        createacc(cursor)
    name=input("Enter the name:")
    emailid=input("Enter your Email id:")
    usrnm=input("Enter the Username(Admission Code, if Member Login):")
    psswd=input("Enter the Password(Between 8 and 30 Characters):")
    cmd='insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\');'.format(tblnm,name,emailid,usrnm,psswd)
    cursor.execute(cmd)
    mycon.commit()
    time.sleep(1)
    print("Account Successfully Added\n")
    cursor.execute('Use library')
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