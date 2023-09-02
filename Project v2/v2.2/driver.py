# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:13:20 2023

@author: Loges
"""

#_main_ program
import time
import pgmclasses as pc

logindb=pc.Database('localhost', 'root', '********', 'loginid')
librarydb=pc.Database('localhost', 'root', '********', 'library')
#Program startup message
print("""
    Welcome to XXXXXXXXXX Library!!!!\n
1:Member Login
2:Employee login\n
""")
ui = pc.User(logindb)#Login process
print(ui.mainpage)  
#Member options
if ui.lgtp==1:
    while True:
        choice=int(input("Enter your CHOICE:"))
        print()
        if choice==1:
            ui.selectfn(librarydb,'book b,copies c')
        elif choice==2:
            ui.lendbook(librarydb)
        elif choice==3:
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print('Book renewed')
            time.sleep(1)
            print("Submission Date extended for 10 more days")
        elif choice==4:
            ui.returnbook(librarydb)
        elif choice==5:
            ui.changeaccdet('R')
        elif choice==6:
            ui.changeaccdet('P')
        elif choice==0:
            break
        else:
            print('Invalid choice')
            print("Try again")
        time.sleep(3)
        print(ui.mainpage)
#Employee Login
if ui.lgtp==2:
    while True:
        choice=int(input("Enter your Choice:"))
        print()
        if choice==1:
            ui.selectfn(librarydb,'book b,copies c')
        elif choice==2:
            ui.insertbookdata(librarydb)
        elif choice==3:
            ui.changedata()
        elif choice==4:
            ui.lendbook(librarydb)
        elif choice==5:
            nm=input("Enter the name of the book holder:")
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print("Book Renewed")
            time.sleep(1)
            print("Submission Date Extended for 10 more Days")
        elif choice==6:
            ui.returnbook(librarydb)
        elif choice==7:
            ui.createacc()
        elif choice==8:
            ui.changeaccdet('R')
        elif choice==9:
            ui.changeaccdet('P')
        elif choice==0:
            break
        else:
            print("Invalid Choice")
            print("Try again")
        time.sleep(3)
        print(ui.mainpage)
#Displaying the end message
del librarydb
del logindb
del ui