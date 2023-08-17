# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:44:12 2023

@author: Loges
"""
import time
import mysql.connector as sqltor
import table as tb

class Database:
    def __init__(self, host, user, passwd, database):
        '''

        Parameters
        ----------
        host : str
            DESCRIPTION.
        user : str
            DESCRIPTION.
        passwd : str
            DESCRIPTION.
        database : str
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.conn=sqltor.connect(host=host,user=user,passwd=passwd,database=database)
        self.csr=self.conn.cursor()
        self.db=database
        
    def tabledetails(self, table):
        '''Function to get name of the table columns'''
        try:
            cmd='desc '+table+';'
            self.csr.execute(cmd)
            data=self.csr.fetchall()
            data1=[]
            data2=[]
            for row in data:
                data1.append(row[0])
                data2.append(str(row[1]))
            return data1,data2
        except:
            print("No such table exists")
    
    def tblaccess(self,tblnm,condn=None,cname='*'):
        '''Function to get resultset from Mysql'''
        if condn==None:
            str='select {0} from {1};'.format(cname,tblnm)
        else:
            str='select {0} from {1} where {2};'.format(cname,tblnm,condn)
        self.csr.execute(str)
        tbl=self.csr.fetchall()
        return tbl
        
class User:
    def __init__(self, name, lgid, type):
        self.name=name
        self.lgid=lgid
        self.lgtp=type
        self.mainpage=""
        if self.lgtp==1:
            self.mainpage="1:Search a Book\n2:Request for a Book\n3:Renew a Book\n4:Return a Book\n5:Change Account Details\n6:Change Password\n"
        else:
            self.mainpage="1:Search a Book\n2:Insert a New Book \n3:Change a Book Data\n4:Lend a Book\n5:Renew a Book\n6:Return a Book\n7:Create a New Member Account\n8:Change Account Details\n9:Change Password"
        self.mainpage+="0:Logout and Exit"
        
    