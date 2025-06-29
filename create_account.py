from sql_query import exec_query
import logger
import logging

def create_new_account():
    ##TAKING INFORMATIN FOR NEW ACOUNT
    Name=input("Enter your full name in FN MN LN format: ")
    Gender=input("Enter your Gender: ")
    Age=int(input("Enter your Age : "))
    phone_number=input("Enter your phone number: ")
    date_of_birth=input("enter your date in 'YYYY-MM-DD' format :")
    password=input("Set your strong pasword which you have to remember for services :")
    balance=float(input("You have to deposit some amount :"))


    ## QUERY FOE INSERTING DATA
    query="insert into users (NAME,GENDER,AGE,PHONE_NO,DATE_OF_BIRTH,PASSWORD,BALANCE)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    data=(Name,Gender,Age,phone_number,date_of_birth,password,balance)


    ## EXECUTING QUERRY BY USING METHOD
    exec_query(query,data)
    print("ACCOUNT CREATED SUCCESSFULLY..")
    logging.info("ACCOUNT CREATED SUCCESSFULLY..")
    

    


