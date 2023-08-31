# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:44:12 2023

@author: Loges
"""
import time
import mysql.connector as sqltor
import lmstable as tb
import tkinter as tkt

class Database:
    def __init__(self, host, user, passwd, database):
        self.conn=sqltor.connect(host=host,user=user,passwd=passwd,database=database)
        self.csr=self.conn.cursor()
        self.donotcommit=['select', 'desc']
        self.db=database
        
    def tabledetails(self, table):
        '''Function to get name of the table columns'''
        try:
            cmd='desc '+table+';'
            data=self.get(cmd)
            data1=[]
            for row in data:
                data1.append(str(row[0]))
            return data1
        except:
            print("No such table exists")
    
    def tblaccess(self,tblnm,condn=None,cname='*'):
        '''Function to get resultset from Mysql'''
        if condn==None:
            cmd='select {0} from {1};'.format(cname,tblnm)
        else:
            cmd='select {0} from {1} where {2};'.format(cname,tblnm,condn)
        tbl=self.get(cmd)
        return tbl
    
    def close(self):
        self.conn.close()
        
    def __del__(self):
        self.close()
        
    def execute(self, command):
        self.csr.execute(command)
        stat=True
        for cmd in self.donotcommit:
            stat=stat and cmd in command
        if stat:
            self.conn.commit()
        
    def get(self, command):
        self.execute(command)
        return self.csr.fetchall()
        
class User:
    def __init__(self, name, lgid, type, emailid):
        self.name=name
        self.lgid=lgid
        self.lgtp=type
        self.email=emailid
        self.mainpage=""
        if self.lgtp==1:
            self.tblnm="mbrlgnid"
            self.mainpage="1:Search a Book\n2:Request for a Book\n3:Renew a Book\n4:Return a Book\n5:Change Account Details\n6:Change Password\n"
        else:
            self.tblnm="emplgnid"
            self.mainpage="1:Search a Book\n2:Insert a New Book \n3:Change a Book Data\n4:Lend a Book\n5:Renew a Book\n6:Return a Book\n7:Create a New Member Account\n8:Change Account Details\n9:Change Password\n"
        self.mainpage+="0:Logout and Exit"
        
class LabelEntryPair:
    def __init__(self, root, text, width=50, borderwidth=5):
        self.label=tkt.Label(root, text=text)
        self.entry=tkt.Entry(root, width=width, borderwidth=borderwidth)
        
    def grid(self, row):
        self.label.grid(row=row, column=0)
        self.entry.grid(row=row, column=1)
        
    def get(self):
        return self.entry.get()
    
    def set(self, text):
        self.entry.insert(0, text)
    
    def forget(self):
        self.label.grid_forget()
        self.entry.grid_forget()