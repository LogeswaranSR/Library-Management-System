import time
import lmstable as tb

def selectfn(db, tbl, clmn, value):
    '''Function to search a book'''
    inpt='b.bcode,bname,author,publ,price,slf,tcp,acp'
    condn1='b.bcode=c.bcode and '
    data=None
    if clmn==1:
        c='Name'
        condn1+='BNAME=\'{0}\''.format(value)
    if clmn==2:
        c='Code'
        condn1+='b.BCODE=\'{0}\''.format(value)
    if clmn==3:
        c='Publisher'
        condn1+='PUBL LIKE \'%{0}%\''.format(value)
    if clmn==4:
        c='Genre'
        gnre=value
        condn2='GENRE=\'{0}\''.format(gnre)
        tbl1='GENRECODE'
        data1=db.tblaccess(tbl1,condn2,'*')
        if data1==[]:
            data='Book of that Genre is not Found'
            tbl=[]
        else:
            condn1+='b.BCODE LIKE \'{0}%\''.format(data1[0][0])
    if data==None:
        try:
            data=db.tblaccess(tbl,condn1,inpt)
            if data==[]:
                tbl=[]
                data='Book of that {0} is not found'.format(c)
            else:
                tbl=['book','copies']
        except:
            pass
    return data, tbl
def insertbookdata(db, details):
    '''Function to insert new book data'''
    try:
        bname, aname, bcode, publ, price, sfcde, cps, avblcps=details
        cmd='insert into book values(\'{0}\',\'{1}\',\'{2}\',\'{3}\',{4},\'{5}\');'.format(bcode,bname,aname,publ,price,sfcde)
        cmd2='insert into copies values(\'{0}\',{1},{2});'.format(bcode,cps,avblcps)
        db.execute(cmd)
        db.execute(cmd2)
        return True
    except:
        return False

def changedata(db, changes, code):
    '''Function to change data regarding books'''
    try:
        if 'ACP' in changes:
            cmd2='update copies set ACP={0} where BCODE=\'{1}\';'.format(changes["ACP"],code)
            db.execute(cmd2)
        cmd='update book set '
        for col in changes:
            cmd+='{0}=\'{1}\','.format(col, changes[col])
        cmd=cmd[:-1]+' where BCODE=\'{}\';'.format(code)
        db.execute(cmd)
        return True
    except:
        return False
def lendbook(db, lgtp):
    '''Function to lend a book'''
    if lgtp=='M':
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
            lendbook(db,lgtp)
    if lgtp=='E':
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
            lendbook(db,lgtp)
def returnbook(db, lgtp):
    '''Function to return a book'''
    if lgtp=='E':
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
            returnbook(db,lgtp)
    if lgtp=='M':
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
            returnbook(db,lgtp)