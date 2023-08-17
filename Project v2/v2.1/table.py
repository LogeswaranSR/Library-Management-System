# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 15:55:59 2023

@author: Loges
"""

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
    print('|',end='')
    n=[]
    for i in range(len(data[0])):
        if 'int' in ctype[i] or 'char(3)' in ctype[i]:
            length=len(str(cname[i]))
            spln=5-length
            print(cname[i],end='')
            print(spln*' ',end='')
            print('|',end='')
            n.append(5)
        elif 'varchar(15)' in ctype[i]:
            length=len(cname[i])
            spln=15-length
            print(cname[i],end='')
            print(spln*' ',end='')
            print("|",end='')
            n.append(15)
        elif 'varchar' in ctype[i]:
            length=len(cname[i])
            spln=40-length
            print(cname[i],end='')
            print(spln*' ',end='')
            print("|",end='')
            n.append(40)
        else:
            pass
    print()
    print('+',end='')
    for i in n:
        print(i*'=',end='')
        print(end='+')
    print()
    for row in data:
        print('|',end='')
        clm=len(row)
        n=[]
        for col in range(0,clm):
            if 'int' in ctype[col] or 'char(3)' in ctype[col]:
                length=len(str(row[col]))
                spln=5-length
                print(row[col],end='')
                print(spln*' ',end='')
                print('|',end='')
                n.append(5)
            elif 'varchar(15)' in ctype[col]:
                length=len(row[col])
                spln=15-length
                print(row[col],end='')
                print(spln*' ',end='')
                print("|",end='')
                n.append(15)
            elif 'varchar' in ctype[col]:
                length=len(row[col])
                spln=40-length
                print(row[col],end='')
                print(spln*' ',end='')
                print("|",end='')
                n.append(40)
            else:
                print(row[col],end=' |')
                n.append(len(row[col])+2)
        print()
        print('+',end='')
        for i in n:
            print(i*'-',end='')
            print(end='+')
        print()
    print()