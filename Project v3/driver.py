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
import loginpage as lp
import basicclasses as bc

mycon=sqltor.connect(host='localhost',user='root',passwd='14061703')
csr=mycon.cursor()
sample=lp.loginpage(csr)
csr.execute('Use loginid;')
#Login process
sample.initialize()
details=sample.start()
ui=bc.User(details[0], details[1], details[2])
    # if lgnoptn==3:
    #     ac.createacc(csr)
csr.execute('Use library')
#Member login 
if ui.lgtp==1:
    time.sleep(1)
    while True:
        time.sleep(2)
        print(ui.mainpage)#Homepage for Member account
        time.sleep(1)
        choice=int(input("Enter your CHOICE:"))
        print()
        if choice==1:
            lms.selectfn(csr,'book b,copies c')
        elif choice==2:
            lms.lendbook(csr,mycon,ui.lgtp)
        elif choice==3:
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print('Book renewed')
            time.sleep(1)
            print("Submission Date extended for 10 more days")
        elif choice==4:
            lms.returnbook(csr,mycon,ui.lgtp)
        elif choice==5:
            ac.changeaccdet(csr,mycon,ui.lgtp,ui.lgid,'R')
        elif choice==6:
            ac.changeaccdet(csr,mycon,ui.lgtp,ui.lgid,'P')
        elif choice==0:
            break
        else:
            print('Invalid choice')
            print("Try again")
        time.sleep(3)
#Employee Login
if ui.lgtp==2:
    time.sleep(1)
    while True:
        time.sleep(1)
        print(ui.mainpage)#Homepage for Employee account
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
            lms.lendbook(csr,mycon,ui.lgtp)
        elif choice==5:
            nm=input("Enter the name of the book holder:")
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print("Book Renewed")
            time.sleep(1)
            print("Submission Date Extended for 10 more Days")
        elif choice==6:
            lms.returnbook(csr,mycon,ui.lgtp)
        elif choice==7:
            ac.createacc(csr,mycon)
        elif choice==8:
            ac.changeaccdet(csr,mycon,ui.lgtp,ui.lgid,'R')
        elif choice==9:
            ac.changeaccdet(csr,mycon,ui.lgtp,ui.lgid,'P')
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
