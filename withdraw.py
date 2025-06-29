from sql_query import exec_query
import logger
import logging

def withdraw_money():
    mob=input("enter your registered mobile number :")
    passwrd=input("enter your password :")
    amt=int(input("enter amount:"))

    qur1="select BALANCE from users where PHONE_NO=%s and PASSWORD=%s"
    cur_amt=exec_query(qur1,(mob,passwrd),fetch=True)
    logging.info("FETCHING DATA FROM DATABASE..")
    if cur_amt[0][0] < amt:
        print("INSUFFICIENT BALANCE.....")
        logging.error(f"INSUFFICIENT BALANCE FOR {mob}")
        return
    
    qur2="update users set BALANCE=BALANCE-%s where PHONE_NO=%s and PASSWORD=%s"
    exec_query(qur2,(amt,mob,passwrd))
    print("YOUR TRANSACTION IS SUCCESSFULL.")
    logging.info(f"TRANSACTION SUCCESSFUL OF RS. {amt} FOR {mob}")

    choice= int(input("press 1 to check remaining balance otherwise press any key :"))
    if choice == 1:
        qur3="select BALANCE from users where PHONE_NO=%s and PASSWORD=%s"
        cur_amt=exec_query(qur3,(mob,passwrd),fetch=True)
        logging.info(f"CHECKING BALANCE FOR {mob}")
        print(f"YOUR REMAINING BALANCE IS {cur_amt[0][0]}")
        print("THANK YOU !!")
    else:
        print("THANK YOU !!")