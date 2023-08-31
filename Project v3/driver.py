# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:13:20 2023

@author: Loges
"""

#_main_ program
import time
import lmstable as tb
import sys
import pagedeclarer as pd
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
pagedeclns=[lambda: pd.caprocess(mainpage.root, logindb),
            lambda: pd.searchbookprocess(mainpage, mainpage.root, librarydb),
            lambda: pd.insertbookprocess(mainpage, mainpage.root, librarydb)]
mainpage.declare(pagedeclns)
mainpage.initialize()
mainpage.start()
#Employee Login
#Displaying the end message
print("You have Logged out Successfully!!!!")
print("Thank you for visiting our Library!!!")
del ui
librarydb.close()
logindb.close()
