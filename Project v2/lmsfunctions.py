import time
import table as tb

def selectfn(csr,tbl):
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
        data1=tb.tblaccess(csr,tbl1,condn2,'*')
        if data1==[]:
            print('Book of that Genre is not Found')
        else:
            condn1+='b.BCODE LIKE \'{0}%\''.format(data1[0][0])
    print()
    try:
        data=tb.tblaccess(csr,tbl,condn1,inpt)
        if data==[]:
            st='Book of that {0} is not found'.format(c)
            print(st)
        else:
            tbl=['book','copies']
            tb.tabledisplay(data,csr,tbl)
    except:
        pass
def insertbookdata(cursor, mycon):
    '''Function to insert new book data'''
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

def changedata(cursor, mycon):
    '''Function to change data regarding books'''
    tname=input('Enter the Table Name(Book,Copies,Genrecode):')
    code=input("Enter the Book Code/Genre Code(First 3 Numbers of Book Code):")
    cmd1='select * from {0} where BCODE=\'{1}\';'.format(tname,code)
    cursor.execute(cmd1)
    data1=cursor.fetchall()
    if data1!=None:
        print('Data:')
        tb.tabledisplay(data1,cursor,tname)
        cname=input("Enter the column name to be changed:")
        value=input("Enter the new data:")
        cmd2='update {0} set {1}=\'{2}\' where BCODE=\'{3}\';'.format(tname,cname,value,code)
        cursor.execute(cmd2)
        mycon.commit()
        print("Record Updated!\n")
    else:
        print("Data not Found\n")
def lendbook(cursor, mycon, lgtp):
    '''Function to lend a book'''
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
def returnbook(cursor, mycon, lgtp):
    '''Function to return a book'''
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