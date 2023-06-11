# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:13:20 2023

@author: Loges
"""

#_main_ program
import time
import mysql.connector as sqltor
import table as tb
import account as ac
import lmsfunctions as lms

mycon=sqltor.connect(host='localhost',user='root',passwd='********')
csr=mycon.cursor()
while True:
    print("""
    Welcome to Sairam Vidyalaya's Library!!!!\n
1:Member Login
2:Employee login\n
""")#Program startup message
    csr.execute('Use loginid;')
    time.sleep(1)
    #Login process
    lgnoptn=int(input("Enter the type of login\n(New Member? Enter 3):"))
    if lgnoptn==1:
        data=tb.tblaccess(csr,'mbrlgnid')
        usrnm=ac.login(data)
        lgntype='M'
        break
    if lgnoptn==2:
        data=tb.tblaccess(csr,'emplgnid')
        usrnm=ac.login(data)
        lgntype='E'
        break
    if lgnoptn==3:
        ac.createacc(csr)
csr.execute('Use library')
#Member login 
if lgntype=='M':
    time.sleep(1)
    while True:
        time.sleep(2)
        print("""
1:Search a Book
2:Request for a Book
3:Renew a Book
4:Return a Book
5:Change Account Details
6:Change Password
0:Logout and Exit
""")#Homepage for Member account
        time.sleep(1)
        choice=int(input("Enter your CHOICE:"))
        print()
        if choice==1:
            lms.selectfn(csr,'book b,copies c')
        elif choice==2:
            lms.lendbook(csr,mycon,lgntype)
        elif choice==3:
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print('Book renewed')
            time.sleep(1)
            print("Submission Date extended for 10 more days")
        elif choice==4:
            lms.returnbook(csr,mycon,lgntype)
        elif choice==5:
            ac.changeaccdet(csr,mycon,lgntype,usrnm,'R')
        elif choice==6:
            ac.changeaccdet(csr,mycon,lgntype,usrnm,'P')
        elif choice==0:
            break
        else:
            print('Invalid choice')
            print("Try again")
        time.sleep(3)
#Employee Login
if lgntype=='E':
    time.sleep(1)
    while True:
        time.sleep(1)
        print("""
1:Search a Book
2:Insert a New Book 
3:Change a Book Data
4:Lend a Book
5:Renew a Book
6:Return a Book
7:Create a New Member Account
8:Change Account Details
9:Change Password
0:Logout and Exit
""")#Homepage for Employee account
        time.sleep(1)
        choice=int(input("Enter your Choice:"))
        print()
        if choice==1:
            lms.selectfn(csr,'book b,copies c')
        elif choice==2:
            lms.insertbookdata(csr,mycon)
        elif choice==3:
            lms.changedata(csr,mycon)
        elif choice==4:
            lms.lendbook(csr,mycon,lgntype)
        elif choice==5:
            nm=input("Enter the name of the book holder:")
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print("Book Renewed")
            time.sleep(1)
            print("Submission Date Extended for 10 more Days")
        elif choice==6:
            lms.returnbook(csr,mycon,lgntype)
        elif choice==7:
            ac.createacc(csr,mycon)
        elif choice==8:
            ac.changeaccdet(csr,mycon,lgntype,usrnm,'R')
        elif choice==9:
            ac.changeaccdet(csr,mycon,lgntype,usrnm,'P')
        elif choice==0:
            break
        else:
            print("Invalid Choice")
            print("Try again")
        time.sleep(3)
#Displaying the end message
time.sleep(5)
print("You have Logged out Successfully!!!!")
time.sleep(1)
print("Thank you for visiting our Library!!!")
mycon.close()
