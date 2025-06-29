from sql_query import exec_query
import logger
import logging

def fetch_data():
    mob=input("enter your registered mobile number :")
    passwrd=input("enter your password :")
    query="select USER_ID,NAME,GENDER,AGE,DATE_OF_BIRTH,BALANCE from users where PHONE_NO=%s and PASSWORD=%s;"
    info=(mob,passwrd)
    data=exec_query(query,info,fetch=True)
    print(f"FETCHING DATA FOR {mob}")
    logging.info(f"FETCHING DATA FOR {mob}")
    print(data) 
