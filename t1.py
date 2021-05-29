
import mysql.connector as mysql

con=mysql.connect(host='localhost',user='B',passwd='ROOt@1234',database='cryptologbook')
if con.is_connected():
    print('s')

c=con.cursor()

r=c.execute('create table if not exists a (S_NO int(60) primary key ,CRYPT_NAME VARCHAR(60),TOTAL_INVESTED float(10,5),VALUE_TODAY FLOAT(10,5),DIFFRENCE int(60));')   #creating table
con.close()


print('                                                 --------------------PROGRAM END--------------------                                     ')

import T2
exec(open('T2.py').read())
