import mysql.connector

def getpassword():
    return "Ztr@p18042001"

def connect():
    return mysql.connector.connect(
        host = "localhost",
        user = "khanh",
        password = "Ztr@p18042001",
        database = "Nhansu"
    )

def get(table: str) -> tuple | list:
    '''
    header: tuple
    table: 2D list
    '''
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute(f"Select * from {table}")
    yield mycursor.column_names
    myresult = mycursor.fetchall()
    listresult = list(myresult)
    for i in range(len(myresult)):
        listresult[i] = list(listresult[i])
        for j in range(4,6):
            listresult[i][j] = listresult[i][j].hex()
    yield listresult

def get_Decrypt(table: str,password: str) -> tuple | list:
    '''
    header: tuple
    table: 2D list
    '''
    mydb = connect()
    mycursor = mydb.cursor()
    # print(f"Select Ho, Ten, Address, aes_decrypt(SDT,\"{password}\") as SDT , aes_decrypt(CMT,\"{password}\") as CMT from {table}")
    mycursor.execute(f"Select STT, Ho, Ten, Address, aes_decrypt(SDT,\"{password}\") as SDT , aes_decrypt(CMT,\"{password}\") as CMT from {table}")
    yield mycursor.column_names
    myresult = mycursor.fetchall()
    listresult = list(myresult)
    for i in range(len(myresult)):
        listresult[i] = list(listresult[i])
        for j in range(4,6):
            listresult[i][j] = listresult[i][j].decode("utf-8")
    yield listresult

def add(ho, ten, diachi, sdt, cmt):
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute(f"Insert into Ketoan (Ho, Ten, Address, SDT, CMT)\
     values (\"{ho}\",\"{ten}\",\"{diachi}\",\
	 AES_ENCRYPT(\"{sdt}\",\"Ztr@p18042001\"), AES_ENCRYPT(\"{cmt}\", \"Ztr@p18042001\"))")
    mydb.commit()

# ho,ten,diachi,sdt,cmt = "Phan","Ngan","Tan Binh","016325","45646"
# print(f"Insert into Ketoan (Ho, Ten, Address, SDT, CMT)\
#  values (\"{ho}\",\"{ten}\",\"{diachi}\",\
#  AES_ENCRYPT(\"{sdt}\",\"Ztr@p18042001\"), AES_ENCRYPT(\"{cmt}\", \"Ztr@p18042001\"))")

# add("Phan","Khanh","TanBinh","0375933570","01522")

# # byte = bytearray(b'0707316556')
# # list = byte.decode("utf-8")
# # print(type(byte),list)
# head, val = get("KeToan")
# print(head)
# print(val)