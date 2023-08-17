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
            strcmd='select {0} from {1};'.format(cname,tblnm)
        else:
            strcmd='select {0} from {1} where {2};'.format(cname,tblnm,condn)
        self.csr.execute(strcmd)
        tbl=self.csr.fetchall()
        return tbl
    
    def execute(self, command):
        self.csr.execute(command)
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
        
class User:
    def __init__(self, logindb):
        '''
        

        Parameters
        ----------
        logindb : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.lgtp=int(input("Enter the type of login\n(New Member? Enter 3):"))
        self.logindb=logindb
        if self.lgtp==3:
            self.createacc()
        self.login()
        self.mainpage=""
        if self.lgtp==1:
            self.mainpage="1:Search a Book\n2:Request for a Book\n3:Renew a Book\n4:Return a Book\n5:Change Account Details\n6:Change Password\n"
        else:
            self.mainpage="1:Search a Book\n2:Insert a New Book \n3:Change a Book Data\n4:Lend a Book\n5:Renew a Book\n6:Return a Book\n7:Create a New Member Account\n8:Change Account Details\n9:Change Password"
        self.mainpage+="0:Logout and Exit"
        
    def login(self):
        '''Function to login to the management system'''
        print()
        n=0
        if self.lgtp==2:
            tblnm='emplgnid'
        else:
            tblnm='mbrlgnid'
        tabledata=self.logindb.tblaccess(tblnm)
        status=False
        while not status:
            self.usrnm=input("Enter the id:")
            psswd=input("Enter the Password:")
            for dtls in tabledata:
                if(self.usrnm==dtls[2])and(psswd==dtls[3]):
                    print()
                    print("Login Success\n")
                    print('Welcome,',dtls[0])
                    status=True
                    break
            else:
                print("\nLogin Failed")
                n=n+1
                if(n==10):
                    print("\n10 Unsuccessful Login Attempts")
                    print("Try again after 10 sec",end='')
                    for i in range(10):
                        time.sleep(1)
                        print(end='.')
                    n=0
                else:
                    print('\nTry Again')
    
    def createacc(self):
        '''Function to create a new account(Both employee and member account)'''
        while self.lgtp==3:
            acctype=input("Enter the type of account(E/M):")
            if acctype=='E':
                tblnm='emplgnid'
                self.lgtp=1
            elif acctype=='M':
                tblnm='mbrlgnid'
                self.lgtp=2
            else:
                print("Invalid Account type")
                print('Try Again\n')
        name=input("Enter the name:")
        emailid=input("Enter your Email id:")
        usrnm=input("Enter the Username(Admission Code, if Member Login):")
        psswd=input("Enter the Password(Between 8 and 30 Characters):")
        cmd='insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\');'.format(tblnm,name,emailid,usrnm,psswd)
        self.logindb.execute(cmd)
        print("Account Successfully Added\n")
        
    def changeaccdet(self,tp):
        '''Function to change account details of the user'''
        if self.lgtp==1:
            tblnm='mbrlgnid'
        if self.lgtp==2:
            tblnm='emplgnid'
        condn='USRNM=\'{0}\''.format(self.usrnm)
        if tp not in 'pP':
            data=self.logindb.tblaccess(tblnm,condn,'name,emailid,usrnm')
            tb.tabledisplay(data,self.logindb,tblnm)
            cnm=input("Enter the field to be changed:")
            data=input("Enter the new data:")
            cmd='update {0} set {1}=\'{2}\' where {3};'.format(tblnm,cnm,data,condn)
            self.logindb.execute(cmd)
            print("Account Details Changed Successfully!!\n")
        else:
            status=False
            while not status:
                oldps=input("Enter your old password:")
                newps=input("Enter your new password:")
                rnwps=input("Re-enter your new password:")
                if newps!=rnwps:
                    print("Password typed is wrong")
                    print("Try Again\n")
                else:
                    cmd='update {0} set psswd=\'{1}\' where {2};'.format(tblnm,newps,condn)
                    self.logindb.execute(cmd)
                    status=True
                    print("Password Changed Successfully\n")
    def selectfn(self,db,tbl):
        '''Function to search a book'''
        inpt='b.bcode,bname,author,publ,price,slf,tcp,acp'
        print()
        time.sleep(1)
        clmn=int(input('''How do you like to search the book?
    1:Book Name
    2:Book Code
    3:Publisher
    4:Genre
    Enter your Choice:'''))
        condn1='b.bcode=c.bcode and '
        if clmn==1:
            c='Name'
            bname=input("Enter the Book Name:")
            condn1+='BNAME=\'{0}\''.format(bname)
        if clmn==2:
            c='Code'
            bcode=input("Enter the Book Code:")
            condn1+='b.BCODE=\'{0}\''.format(bcode)
        if clmn==3:
            c='Publisher'
            publ=input("Enter the Publishers of the Book:")
            condn1+='PUBL LIKE \'%{0}%\''.format(publ)
        if clmn==4:
            c='Genre'
            gnre=input("Enter the Genre:")
            condn2='GENRE=\'{0}\''.format(gnre)
            tbl1='GENRECODE'
            data1=db.tblaccess(tbl1,condn2,'*')
            if data1==[]:
                print('Book of that Genre is not Found')
            else:
                condn1+='b.BCODE LIKE \'{0}%\''.format(data1[0][0])
        print()
        try:
            data=db.tblaccess(tbl,condn1,inpt)
            if data==[]:
                st='Book of that {0} is not found'.format(c)
                print(st)
            else:
                tbl=['book','copies']
                tb.tabledisplay(data,db,tbl)
        except:
            pass
    
    def changedata(self, db):
        '''Function to change data regarding books'''
        if self.lgtp==2:
            tname=input('Enter the Table Name(Book,Copies,Genrecode):')
            code=input("Enter the Book Code/Genre Code(First 3 Numbers of Book Code):")
            cmd1='select * from {0} where BCODE=\'{1}\';'.format(tname,code)
            db.csr.execute(cmd1)
            data1=db.csr.fetchall()
            if data1!=None:
                print('Data:')
                tb.tabledisplay(data1,db,tname)
                cname=input("Enter the column name to be changed:")
                value=input("Enter the new data:")
                cmd2='update {0} set {1}=\'{2}\' where BCODE=\'{3}\';'.format(tname,cname,value,code)
                db.execute(cmd2)
                print("Record Updated!\n")
            else:
                print("Data not Found\n")
        else:
            print("Resticted Function\nOnly Employees can change the database")
            
    def lendbook(self, db):
        '''Function to lend a book'''
        if self.lgtp==1:
            bcode=input("Enter the code of the book you want to borrow:")
            cmd='update copies set ACP=ACP-1 where BCODE=\'{0}\';'.format(bcode)
            try:
                db.execute(cmd)
                time.sleep(1)
                print("Request Sent to the Reception")
                time.sleep(1)
                print("Collect Book from the Reception Counter\n")
            except:
                time.sleep(2)
                print("Book of the given code doesn't exist in this Library")
                print("Try Again\n")
                time.sleep(1)
                self.lendbook(db)
        if self.lgtp==2:
            bcode=input("Enter the code of the book to be lended:")
            cmd='update copies set ACP=ACP-1 where BCODE=\'{0}\';'.format(bcode)
            try:
                db.execute(cmd)
                time.sleep(1)
                print("Database Updated")
                time.sleep(1)
                print("Proceed to Give the Book\n")
            except:
                time.sleep(2)
                print("Book of the given code doesn't exist in this Library")
                print("Try Again\n")
                time.sleep(1)
                self.lendbook(db)
    
    def returnbook(self, db):
        '''Function to return a book'''
        if self.lgtp==1:
            bcode=input("Enter the Book code:")
            cmd='update copies set ACP=ACP+1 where BCODE=\'{0}\';'.format(bcode)
            try:
                db.execute(cmd)
                time.sleep(1)
                print("Database Updated")
                time.sleep(1)
                print('Proceed to collect the Book\n')
            except:
                time.sleep(2)
                print("Book of the given code doesn't exist in this Library")
                print("Try Again\n")
                time.sleep(1)
                self.returnbook(db)
        if self.lgtp==2:
            bcode=input("Enter the Book Code:")
            cmd='update copies set ACP=ACP+1 where BCODE=\'{0}\';'.format(bcode)
            try:
                db.execute(cmd)
                time.sleep(1)
                print("Request Sent to the Reception")
                time.sleep(1)
                print("Return Book at the Reception Center\n")
            except:
                time.sleep(2)
                print("Book of the given code doesn't exist in this Library")
                print("Try Again\n")
                time.sleep(1)
                self.returnbook(db)
    
    def insertbookdata(self, db):
        '''Function to insert new book data'''
        if self.lgtp==2:
            ans='y'
            while ans=='y':
                bname=input("Enter the Book Name:")
                aname=input("Enter the Name of the Author:")
                bcode=input("Enter the Book code:")
                publ=input("Enter the Publishers of the book:")
                price=int(input("Enter the Price of the book:"))
                sfcde=input("Enter the Shelf Code:")
                cps=int(input("Enter the Total no. of copies:"))
                avblcps=int(input("Enter the available no. of Copies:"))
                cmd='insert into book values(\'{0}\',\'{1}\',\'{2}\',\'{3}\',{4},\'{5}\');'.format(bcode,bname,aname,publ,price,sfcde)
                cmd2='insert into copies values(\'{0}\',{1},{2});'.format(bcode,cps,avblcps)
                db.execute(cmd)
                db.execute(cmd2)
                print("Record Inserted!")
                ans=input("Do you want to insert another data?(y/n):")
        else:
            print("Resticted Function\nOnly Employees can change the database")
        
    def __del__(self):
        print("You have Logged out Successfully!!!!")
        time.sleep(1)
        print("Thank you for visiting our Library!!!")
    