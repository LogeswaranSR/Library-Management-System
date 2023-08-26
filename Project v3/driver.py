# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:13:20 2023

@author: Loges
"""

#_main_ program
import time
import mysql.connector as sqltor
import lmstable as tb
import sys
import account as ac
import lmsfunctions as lms
import mainmenupage as mp
import loginpage as lp
import basicclasses as bc

logindb=bc.Database(host='localhost',user='root',passwd='14061703', database='loginid')
sample=lp.LoginPage(logindb)
#Login process
sample.initialize()
details=sample.start()
if not details[0]:
    print(details)
    del logindb
    sys.exit()
ui=bc.User(details[1], details[2], details[3])
librarydb=bc.Database(host='localhost',user='root',passwd='14061703', database='library')
#Member login 
mainpage=mp.MainMenuPage(ui, librarydb)
mainpage.declare([])
mainpage.initialize()
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
