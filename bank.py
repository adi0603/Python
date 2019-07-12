#Python program of database connectivity.

import sqlite3
db=sqlite3.connect("Bank.db")
cursor=db.cursor()
#cursor.execute("DROP Table ACCOUNT")
sql="""Create table ACCOUNT If not Exist("ACC_NO" int Primary key,"Name" varchar(30) not null,"BALANCE" int not null)"""
cursor.execute(sql)
patt1="--------------------------------------------------------------------"
patt2="                         WELCOME TO BANK                            "
choice=1
while(choice!=0):
    print(patt1)
    print(patt2)
    print("1 - CREATE NEW ACCOUNT\t\t2 - DELETE A ACCOUNT\n3 - DEPOSIT\t\t\t4 - WITHDRAWL\n5 - DISPLAY DETAIL\t\t0 - EXIT")
    choice=int(input("Enter your choice : "))
    if(choice==1):
        name=input("Enter Name : ")
        acc=input("Enter Account Number : ")
        bal=input("Enter Amount to Deposit : ")
        cursor.execute("INSERT into ACCOUNT values(?,?,?)",(acc,name,bal))
        db.commit()
    elif(choice==2):
        acc=input("Enter Account Number : ")
        cursor.execute("DELETE FROM ACCOUNT where ACC_NO=(%s)"%(acc))
        db.commit()
    elif(choice==3):
        acc=input("Enter Account Number : ")
        bal=input("Enter Amount to Deposit : ")
        cursor.execute("UPDATE ACCOUNT SET BALANCE=BALANCE+(%s) where ACC_NO=(%s)"%(bal,acc))
        db.commit()
    elif(choice==4):
        acc=input("Enter Account Number : ")
        bal=input("Enter Amount to Withdrawl : ")
        cursor.execute("UPDATE ACCOUNT SET BALANCE = BALANCE -(%s) where ACC_NO=(%s) and BALANCE > (%s)"%(bal,acc,bal))
        db.commit()
    elif(choice==5):
        acc=input("Enter Account Number : ")
        print("Details of customer :")
        cursor.execute("SELECT * from ACCOUNT where ACC_NO=(%s)"%(acc))
        result=cursor.fetchall()
        for row in result:
            print("Account - ",row[0])
            print("Name    - ",row[1])
            print("Balance - ",row[2])
    elif(choice!=0):
        print("Invalid choice")
    print(patt1)
db.close()
