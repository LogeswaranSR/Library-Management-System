# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:55:59 2023

@author: Loges
"""
from tabulate import tabulate
def tblaccess(cursor,tblnm,condn=None,cname='*'):
    '''Function to get resultset from Mysql'''
    if condn==None:
        str='select {0} from {1};'.format(cname,tblnm)
    else:
        str='select {0} from {1} where {2};'.format(cname,tblnm,condn)
    cursor.execute(str)
    tbl=cursor.fetchall()
    return tbl
def tabledetails(csr,table):
    '''Function to get name of the table columns'''
    cmd='desc '+table+';'
    csr.execute(cmd)
    data=csr.fetchall()
    data1=[]
    data2=[]
    for row in data:
        data1.append(row[0])
        data2.append(str(row[1]))
    return data1,data2
def tabledisplay(data,csr,tbl):
    '''Function to display the data obtained in the form of a proper table'''
    if 'list' in str(type(tbl)):
        cname,ctype=tabledetails(csr,tbl[0])
        cname2,ctype2=tabledetails(csr,tbl[1])
        cname.append(cname2[1])
        cname.append(cname2[2])
        ctype.append(ctype2[1])
        ctype.append(ctype2[2])
    else:
        cname,ctype=tabledetails(csr,tbl)
    table=tabulate(data, cname, 'grid')
    print(table)