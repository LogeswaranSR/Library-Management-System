# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:13:20 2023

@author: Loges
"""

#_main_ program
import sys
import pagedeclarer as pd
import mainmenupage as mp
import loginpage as lp
import basicclasses as bc

logindb=bc.Database(host='localhost',user='root',passwd='14061703', database='loginid')
sample=lp.LoginPage(logindb)
#Login process
sample.initialize()
user=sample.start()
print(user)
if not user:
    del logindb
    sys.exit()
librarydb=bc.Database(host='localhost',user='root',passwd='14061703', database='library')
#Member login 
mainpage=mp.MainMenuPage(user, librarydb)
pagedeclns=[lambda: pd.caprocess(mainpage.root, logindb),
            lambda: pd.searchbookprocess(mainpage, mainpage.root, librarydb),
            lambda: pd.changeaccdetprocess(mainpage.root, logindb, user),
            lambda: pd.changepasswordprocess(mainpage.root, logindb, user)]
if user.lgtp==2:
    pagedeclns.extend([lambda: pd.insertbookprocess(mainpage, mainpage.root, librarydb)])
mainpage.declare(pagedeclns)
mainpage.initialize()
mainpage.start()
del user
librarydb.close()
logindb.close()
