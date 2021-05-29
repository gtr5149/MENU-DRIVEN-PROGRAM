#DATABASE CREATION.py

#import pandas as pd
import mysql.connector as mysql

con=mysql.connect(host='localhost',user='B',passwd='ROOt@1234');
if con.is_connected():
    print('s')

c=con.cursor()

c.execute('create database if not exists cryptologbook;')

c.execute('show databases;')               #to check if database is created
for x in c:
    print(x)


print('                                       ------------------------------PROGRAM END------------------------------                             ')


import t1
exec(open('t1.py').read())
