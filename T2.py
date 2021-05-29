# CRPTO LOGBOOK MENU

import mysql.connector as mysql

con = mysql.connect(host='localhost', user='B', passwd='ROOt@1234', database='cryptologbook')


if con.is_connected():
    print('s')

c = con.cursor()


LOGIN_ID = int(input('login id'))  # LOGIN AND PASSWORD,VERY EASY TO FIND
PASSWORD = int(input('password'))  #TO CHANGE LOGIN AND PASSWORD
if LOGIN_ID==0 and PASSWORD==0:#TO CHANGE LOGIN AND PASSWORD WRITE YOUR PASSWORD INSTEAD OF ZERO
                                #TO CHANGE THE PASSWORD INTO AN VARCHAR VALUE REMOVE int from LOGIN ID AND PASSWORD
    print('---------------CRYPTO LOGBOOK----------------')
    print('---------------ENTER YOUR CHOICE-------------')

    print('INSERT VALUES==', 1)
    print('SHOW RECORDS==', 2)
    print('DELETE RECORDS==', 3)
    print('RETURN TO MENU==', 4)
    print('QUIT==', 5)
    choice = int(input('ENTER CHOICE'))

    if choice == 1:
        SNO = int(input('INPUT SERIAL NUMBER'))
        CNAME = input('CRYPTO NAME')
        TOTALINVESTED = int(input('INVESTED AMOUNT'))
        VALUETODAY = int(input('VALUE TODAY'))
        DIFFRENCE =int(input('diffrence'))
        c.execute('insert into a values(%s,%s,%s,%s,%s);', (SNO, CNAME, TOTALINVESTED, VALUETODAY, DIFFRENCE))
        con.commit()
    elif choice == 2:
        c.execute('select * from a;')
        r=c.fetchall()
        for x in r:
            print(x)
    elif choice == 3:
        SERIALNUMBER = int(input('SERIAL NUMBER'))
        c.execute('delete from a where SNO= %s ;',(SERIALNUMBER))
        '''con.commit()
        r=c.fetchall()
        for x in r:
            print(x)'''
    elif choice == 4:
        print('---------------CRYPTO LOGBOOK----------------')
        print('---------------ENTER YOUR CHOICE-------------')

        print('INSERT VALUES==', 1)
        print('SHOW RECORDS==', 2)
        print('DELETE RECORDS==', 3)
        print('RETURN TO MENU==', 4)
        print('QUIT==', 5)
        choice = int(input('ENTER CHOICE'))

        if choice == 1:
            SNO = int(input('INPUT SERIAL NUMBER'))
            CNAME = input('CRYPTO NAME')
            TOTALINVESTED = float(input('INVESTED AMOUNT'))
            VALUETODAY = float(input('VALUE TODAY'))
            DIFFRENCE = TOTALINVESTED - VALUETODAY
            c.execute('insert into a values(?,?,?,?,?)', (SNO, CNAME, TOTALINVESTED, VALUETODAY, DIFFRENCE))
            con.commt()
            print('success')
        elif choice == 2:
            c.execute('select * from a;')
            print('DATA')
        elif choice == 3:
            SERIALNUMBER = int(input('SERIAL NUMBER'))
            c.execute('delete from a where SNO=%S;', SERIALNUMBER)
            con.commit()
            print('DELETED VALUES')
        elif choice == 5:
            con.close()
            if con.isnotconnected():
                print('BYE!!')
    elif choice == 5:
        con.close()
        if con.is_connected():
            print('coted!!')
        else:
            print('BYE!!')

else:
    print('ERROR!!')