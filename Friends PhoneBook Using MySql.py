#Internship Project
#Problem Statement
    #To store a data into a database using MySql with the specification.

    #Write a menu driven program to input your friend's name,address and their phone numbers to store them in the dictionary as key-value

#----------------------------------------------------------------------------------------------------------

#Performed Functions

#1.Display the name and phone number of all your firends.
#2.Search a firend phone number by his name.
#3.add new key--value pair in the dictionary.
#4.Modify the number of existing friend
#5.Sort the dictionary in ascending order by name.
#6.Delete a particular friend from the Table.

#----------------------------------------------------------------------------------------------------------
import mysql.connector as mcon

class phoneBook():
    flag=0 #flag used to connection is Established or not
    def __init__(self):

        #Constructor used to Create Databse And Tables Using MySql.
        try:
            myconn=mcon.connect(host="localhost",user="root",passwd="")#connrct to sql server
            cur=myconn.cursor() #cursor object for executing sql query
            chkdb="SHOW DATABASES LIKE 'phonebook'" #used to check db is present or not
            cur.execute(chkdb)
            data=cur.fetchone()
            if data==None:
                try:
                    #query for creting database

                    db_query="CREATE DATABASE phonebook"#it creates DB
                    cur.execute(db_query)

                    print("Database is Created Successfully...!")

                except:
                    print("DataBase Connection Error...!")


                #query for creating table

                try:
                    myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
                    cur=myconn.cursor() #cursor object for executing sql query
                    
                    tbl_query='''CREATE TABLE myphonebook(id int AUTO_INCREMENT PRIMARY KEY,
                                                            name VARCHAR(50) NOT NULL,
                                                            phone VARCHAR(10) NOT NULL,
                                                            address VARCHAR(50) NOT NULL )'''
                    cur.execute(tbl_query)
                    print("Table is Created Successfully...!")
            
                except:
                    print("DataBase Connection Error...!")
            else:
                print("\nDatabase Connection Established Successfully...!")
                
        except:
            self.flag=1
            print("DataBase Connection Error...!")

        
        

    def addFriend(self):
        try:
            myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
            cur=myconn.cursor() #cursor object for executing sql query
        
            
            print("=======================Add Friend========================")
            name=input("Enter Name : ").strip().lower()#strip() used to remove blank spaces of starting and ending , lower() used to convert string to lower case
            while True:
                if name=="":
                    print("=========================================================")
                    print("\nName Cannot Be Emapty...!\n")
                    print("=========================================================")
                    name=input("Enter Name : ").strip().lower()
                else:
                    break
            chknm=f"SELECT * FROM myphonebook WHERE name='{name}'"#used to check name present in table or not

            cur.execute(chknm)
            dt=cur.fetchall()
            if len(dt)!=0:
                print("=========================================================")
                print("\nFriend Alreday Exits...!\n")
                self.addFriend()
                

            phone=input("Enter Phone No. : ").strip()
            while True:
                if not phone.isdecimal():#checks string conatons decimals
                    print("=========================================================")
                    print("\nPhone No. Should Only Conatin Contain Digits...!\n")
                    print("=========================================================")
                    phone=input("Enter Phone No. : ").strip()
                    continue
                if phone[0]!='8' and phone[0]!='9':#only start with 8 or 9
                    print("=========================================================")
                    print("\nPhone No. Should Begin With 8 Or 9\n")
                    print("=========================================================")
                    phone=input("Enter Phone No. : ").strip()
                    continue
                if len(phone)!=10:#lenght should be 10
                    print("=========================================================")
                    print("\nPhone No. Should Be 10 Digits\n")
                    print("=========================================================")
                    phone=input("Enter Phone No. : ").strip()
                    continue
                break
            
            
            address=input("Enter Address : ").strip()
            while True:
                if address=="":
                    print("=========================================================")
                    print("\nAddress Cannot Be Empty...!\n")
                    print("=========================================================")
                    address=input("Enter Address : ").strip()
                else:
                    break

            #insert query to insert data in table
            insquery=f"INSERT INTO myphonebook (name,phone,address) VALUES ('{name}','{phone}','{address}')"
            cur.execute(insquery)
            myconn.commit()#save changes in db
            print("=========================================================")
            print("\nData Inserted Successfully...!\n")
            print("=========================================================")
        except:
            print("=========================================================")
            print("DataBase Connection Error...!")
            print("\n=========================================================")

    def searchFriendData(self):
        myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
        cur=myconn.cursor() #cursor object for executing sql query
        print("======================Search Friend======================")
        fd_name=input("Enter Name : ")
        print("========================Friend Data======================\n")
        chknm=f"SELECT * FROM myphonebook WHERE name LIKE '%{fd_name}%'"#like kyeword for search from both side
        #checks name is present in table or not
        cur.execute(chknm)
        dt=cur.fetchall()
        if len(dt)==0:
            print("=========================================================")
            print("\nFriend Not Exits...!\n")
            self.searchFriendData()
        else:
            print("{:^10} {:^10} {:^15} {:^10}".format("Id","Name","Phone No.","Address"))
            for i in dt:
                print("{:^10} {:^10} {:^15} {:^10}".format(i[0],i[1],i[2],i[3]))
        
            
    def showAllFriends(self):
        try:
            myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
            cur=myconn.cursor() #cursor object for executing sql query
            print("======================All Friends========================\n")
            sel="SELECT * FROM myphonebook"
            #get all rows from table

            cur.execute(sel)

            dt=cur.fetchall()
            
            print("{:^10} {:^10} {:^15} {:^10}".format("Id","Name","Phone No.","Address"))

            for i in dt:
                print("{:^10} {:^10} {:^15} {:^10}".format(i[0],i[1],i[2],i[3]))
        except:
            print("DataBase Connection Error...!")
            
        

    def updateFriendData(self):
        myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
        cur=myconn.cursor() #cursor object for executing sql query
        print("====================Update Friend Data===================")
        fd_id=int(input("Enter Id : "))

        chkid=f"SELECT * FROM myphonebook WHERE id={fd_id}"
        #checks id is exists or not in table
        cur.execute(chkid)
        dt=cur.fetchall()

        if len(dt)==0:
            print("=========================================================")
            print("\nId Dosen't Exits...!\n")
            self.updateFriendData()

        fd_phone=input("Enter New Phone No. : ").strip()
        while True:
            if not fd_phone.isdecimal():
                print("=========================================================")
                print("\nPhone No. Should Only Conatin Contain Digits...!\n")
                print("=========================================================")
                fd_phone=input("Enter Phone No. : ").strip()
                continue
            if fd_phone[0]!='8' and fd_phone[0]!='9':
                print("=========================================================")
                print("\nPhone No. Should Begin With 8 Or 9\n")
                print("=========================================================")
                fd_phone=input("Enter Phone No. : ").strip()
                continue
            if len(fd_phone)!=10:
                print("=========================================================")
                print("\nPhone No. Should Be 10 Digits\n")
                print("=========================================================")
                fd_phone=input("Enter Phone No. : ").strip()
                continue
            break
        
        fd_address=input("Enter New Address : ").strip()
        while True:
            if fd_address=="":
                print("=========================================================")
                print("\nAddress Cannot Be Empty...!\n")
                print("=========================================================")
                fd_address=input("Enter Address : ").strip()
            else:
                break

        try:
            #query for update existing data in table
            updt=f"UPDATE myphonebook set phone='{fd_phone}',address='{fd_address}' WHERE id='{fd_id}'"
            cur.execute(updt)
            myconn.commit()#saves changes
            print("=========================================================")
            print("\nData Updated Successfully...!\n")
        except Exception as z:
            print("=========================================================")
            print("\nDatabase Error...!",z)
            
        
    def delFriendData(self):
        myconn=mcon.connect(host="localhost",user="root",passwd="",database="phonebook")#connrct to sql server
        cur=myconn.cursor() #cursor object for executing sql query
        print("====================Delete Friend Data===================")
        fd_id=int(input("Enter Id : "))

        chkid=f"SELECT * FROM myphonebook WHERE id={fd_id}"
        cur.execute(chkid)
        dt=cur.fetchall()

        if len(dt)==0:
            print("=========================================================")
            print("\nId Dosen't Exits...!\n")
            self.delFriendData()
        try:
            #query to delete data from table
            delq=f"DELETE FROM myphonebook WHERE id={fd_id}"
            cur.execute(delq)
            myconn.commit()
            print("=========================================================")
            print("\nData is Deleted Successfully...!")
        except Exception as z:
            print("=========================================================")
            print("\nDatabase Error...!",z)

        
#__main()__
            
obj=phoneBook()#object for class

if obj.flag==0:#cheks if connection is Established or not if yes then execute 
    while True:
        print("\n====================Friend's PhoneBook===================")
        print('''1).Add Friend Deatils
2).Search Friend By Name
3).Dispaly All Friends
4).Modify Friend Details
5).Delete Friend Deatils
6).Exit''')
        print("=========================================================")
        ch=input("Enter Your Choice : ")

        #choices to perform various operation
        if ch=='1':
            obj.addFriend()
        elif ch=='2':
            obj.searchFriendData()
        elif ch=='3':
            obj.showAllFriends()
        elif ch=='4':
            obj.updateFriendData()
        elif ch=='5':
            obj.delFriendData()
        elif ch=='6':
            break
        else:
            print("=========================================================")
            print("\nEnter Correct Choice...!")
