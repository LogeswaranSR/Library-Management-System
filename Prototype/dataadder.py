import mysql.connector as sqltor
mycon=sqltor.connect(host='localhost',user='root',passwd='14061703')
myfile=open(r'data.txt','r')
if mycon.is_connected():
    print("Connection SUCCESS")
csr=mycon.cursor()
cmd=' '
while cmd:
    cmd=myfile.readline()
    csr.execute(cmd)
    if 'insert into' in cmd:
        mycon.commit()
        print('/',end=' ')
    print("SUCCESS")
mycon.commit()
myfile.close()
mycon.close()
