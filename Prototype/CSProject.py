#This program is a basic version of Library Management system
#created as an investigatory project

def login(tabledata,n=0):#Function to login to the management system
    print()
    lgid=input("Enter the id:")
    psswd=input("Enter the Password:")
    for dtls in tabledata:
        if(lgid==dtls[2])and(psswd==dtls[3]):
            time.sleep(1)
            print()
            print("Login Success\n")
            print('Welcome,',dtls[0])
            break
    else:
        time.sleep(1)
        print("\nLogin Failed")
        n=n+1
        if(n==10):
            print("\n10 Unsuccessful Login Attempts")
            time.sleep(1)
            print("Try again after 10 sec",end='')
            for i in range(10):
                time.sleep(1)
                print(end='.')
            login(tabledata)
        else:
            time.sleep(1)
            print('\nTry Again')
            login(tabledata,n)
    return lgid
def tblaccess(cursor,tblnm,condn=None,cname='*'):#Function to get resultset from Mysql
    if condn==None:
        str='select {0} from {1};'.format(cname,tblnm)
    else:
        str='select {0} from {1} where {2};'.format(cname,tblnm,condn)
    cursor.execute(str)
    tbl=cursor.fetchall()
    return tbl
def tabledetails(csr,table):#Function to get name of the table columns
    cmd='desc '+table+';'
    csr.execute(cmd)
    data=csr.fetchall()
    data1=[]
    data2=[]
    for row in data:
        data1.append(row[0])
        data2.append(str(row[1]))
    return data1,data2
def tabledisplay(data,csr,tbl):#Function to display the data obtained in the form of a proper table
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
def selectfn(csr,tbl):#Function to search a book
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
        data1=tblaccess(csr,tbl1,condn2,'*')
        if data1==[]:
            print('Book of that Genre is not Found')
        else:
            condn1+='b.BCODE LIKE \'{0}%\''.format(data1[0][0])
    print()
    try:
        data=tblaccess(csr,tbl,condn1,inpt)
        if data==[]:
            st='Book of that {0} is not found'.format(c)
            print(st)
        else:
            tbl=['book','copies']
            tabledisplay(data,csr,tbl)
    except:
        pass
def insertbookdata(cursor):#Function to insert new book data
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
        cursor.execute(cmd)
        mycon.commit()
        cursor.execute(cmd2)
        mycon.commit()
        print("Record Inserted!")
        ans=input("Do you want to insert another data?(y/n):")
def createacc(cursor):#Function to create a new account(Both employee and member account)
    cursor.execute('Use loginid')
    acctype=input("Enter the type of account(E/M):")
    if acctype=='E':
        tblnm='emplgnid'
    elif acctype=='M':
        tblnm='mbrlgnid'
    else:
        print("Invalid Account type")
        print('Try Again\n')
        createacc(cursor)
    name=input("Enter the name:")
    emailid=input("Enter your Email id:")
    usrnm=input("Enter the Username(Admission Code, if Member Login):")
    psswd=input("Enter the Password(Between 8 and 30 Characters):")
    cmd='insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\');'.format(tblnm,name,emailid,usrnm,psswd)
    cursor.execute(cmd)
    mycon.commit()
    time.sleep(1)
    print("Account Successfully Added\n")
    cursor.execute('Use library')
def changeaccdet(cursor,lgntp,usrnm,tp):#Function to change account details of the user
    cursor.execute('Use loginid;')
    if lgntp=='M':
        tblnm='mbrlgnid'
    if lgntp=='E':
        tblnm='emplgnid'
    condn='USRNM=\'{0}\''.format(usrnm)
    if tp not in 'pP':
        data=tblaccess(cursor,tblnm,condn,'name,emailid,usrnm')
        tabledisplay(data,cursor,tblnm)
        cnm=input("Enter the column of data to be changed:")
        data=input("Enter the new data:")
        cmd='update {0} set {1}=\'{2}\' where {3};'.format(tblnm,cnm,data,condn)
        cursor.execute(cmd)
        mycon.commit()
        time.sleep(1)
        print("Account Details Changed Successfully!!\n")
    else:
        oldps=input("Enter your old password:")
        newps=input("Enter your new password:")
        rnwps=input("Re-enter your new password:")
        if newps!=rnwps:
            print("Password typed is wrong")
            print("Try Again\n")
            time.sleep(1)
            changeaccdet(cursor,lgntp,usrnm,tp)
        else:
            cmd='update {0} set psswd=\'{1}\' where {2};'.format(tblnm,newps,condn)
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Password Changed Successfully\n")
    cursor.execute('Use library;')
def changedata(cursor):#Function to change data regarding books
    tname=input('Enter the Table Name(Book,Copies,Genrecode):')
    code=input("Enter the Book Code/Genre Code(First 3 Numbers of Book Code):")
    cmd1='select * from {0} where BCODE=\'{1}\';'.format(tname,code)
    csr.execute(cmd1)
    data1=csr.fetchall()
    if data1!=None:
        print('Data:')
        tabledisplay(data1,cursor,tname)
        cname=input("Enter the column name to be changed:")
        value=input("Enter the new data:")
        cmd2='update {0} set {1}=\'{2}\' where BCODE=\'{3}\';'.format(tname,cname,value,code)
        cursor.execute(cmd2)
        mycon.commit()
        print("Record Updated!\n")
    else:
        print("Data not Found\n")
def lendbook(cursor,lgtp):#Function to lend a book
    if lgtp=='M':
        bcode=input("Enter the code of the book you want to borrow:")
        cmd='update copies set ACP=ACP-1 where BCODE=\'{0}\';'.format(bcode)
        try:
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Request Sent to the Reception")
            time.sleep(1)
            print("Collect Book from the Reception Counter\n")
        except:
            time.sleep(2)
            print("Book of the given code doesn't exist in this Library")
            print("Try Again\n")
            time.sleep(1)
            lendbook(cursor,lgtp)
    if lgtp=='E':
        bcode=input("Enter the code of the book to be lended:")
        cmd='update copies set ACP=ACP-1 where BCODE=\'{0}\';'.format(bcode)
        try:
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Database Updated")
            time.sleep(1)
            print("Proceed to Give the Book\n")
        except:
            time.sleep(2)
            print("Book of the given code doesn't exist in this Library")
            print("Try Again\n")
            time.sleep(1)
            lendbook(cursor,lgtp)
def returnbook(cursor,lgtp):#Function to return a book
    if lgtp=='E':
        bcode=input("Enter the Book code:")
        cmd='update copies set ACP=ACP+1 where BCODE=\'{0}\';'.format(bcode)
        try:
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Database Updated")
            time.sleep(1)
            print('Proceed to collect the Book\n')
        except:
            time.sleep(2)
            print("Book of the given code doesn't exist in this Library")
            print("Try Again\n")
            time.sleep(1)
            returnbook(cursor,lgtp)
    if lgtp=='M':
        bcode=input("Enter the Book Code:")
        cmd='update copies set ACP=ACP+1 where BCODE=\'{0}\';'.format(bcode)
        try:
            cursor.execute(cmd)
            mycon.commit()
            time.sleep(1)
            print("Request Sent to the Reception")
            time.sleep(1)
            print("Return Book at the Reception Center\n")
        except:
            time.sleep(2)
            print("Book of the given code doesn't exist in this Library")
            print("Try Again\n")
            time.sleep(1)
            returnbook(cursor,lgtp)

#_main_ program
import time
import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='********')
csr=mycon.cursor()
while True:
    print("""
    Welcome to Sairam Vidyalaya's Library!!!!\n
1:Member Login
2:Employee login\n
""")#Program startup message
    csr.execute('Use loginid;')
    time.sleep(1)
    #Login process
    lgnoptn=int(input("Enter the type of login\n(New Member? Enter 3):"))
    if lgnoptn==1:
        data=tblaccess(csr,'mbrlgnid')
        usrnm=login(data)
        lgntype='M'
        break
    if lgnoptn==2:
        data=tblaccess(csr,'emplgnid')
        usrnm=login(data)
        lgntype='E'
        break
    if lgnoptn==3:
        createacc(csr)
csr.execute('Use library')
#Member login 
if lgntype=='M':
    time.sleep(1)
    while True:
        time.sleep(2)
        print("""
1:Search a Book
2:Request for a Book
3:Renew a Book
4:Return a Book
5:Change Account Details
6:Change Password
0:Logout and Exit
""")#Homepage for Member account
        time.sleep(1)
        choice=int(input("Enter your CHOICE:"))
        print()
        if choice==1:
            selectfn(csr,'book b,copies c')
        elif choice==2:
            lendbook(csr,lgntype)
        elif choice==3:
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print('Book renewed')
            time.sleep(1)
            print("Submission Date extended for 10 more days")
        elif choice==4:
            returnbook(csr,lgntype)
        elif choice==5:
            changeaccdet(csr,lgntype,usrnm,'R')
        elif choice==6:
            changeaccdet(csr,lgntype,usrnm,'P')
        elif choice==0:
            break
        else:
            print('Invalid choice')
            print("Try again")
        time.sleep(3)
#Employee Login
if lgntype=='E':
    time.sleep(1)
    while True:
        time.sleep(1)
        print("""
1:Search a Book
2:Insert a New Book 
3:Change a Book Data
4:Lend a Book
5:Renew a Book
6:Return a Book
7:Create a New Member Account
8:Change Account Details
9:Change Password
0:Logout and Exit
""")#Homepage for Employee account
        time.sleep(1)
        choice=int(input("Enter your Choice:"))
        print()
        if choice==1:
            selectfn(csr,'book b,copies c')
        elif choice==2:
            insertbookdata(csr)
        elif choice==3:
            changedata(csr)
        elif choice==4:
            lendbook(csr,lgntype)
        elif choice==5:
            nm=input("Enter the name of the book holder:")
            bcd=input("Enter the Book Code:")
            time.sleep(3)
            print("Book Renewed")
            time.sleep(1)
            print("Submission Date Extended for 10 more Days")
        elif choice==6:
            returnbook(csr,lgntype)
        elif choice==7:
            createacc(csr)
        elif choice==8:
            changeaccdet(csr,lgntype,usrnm,'R')
        elif choice==9:
            changeaccdet(csr,lgntype,usrnm,'P')
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
