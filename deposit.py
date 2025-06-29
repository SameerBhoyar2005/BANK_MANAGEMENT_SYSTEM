from sql_query import exec_query
import logger
import logging

def deposit():
    id=int(input("enter your user id :"))
    amt=int(input("enter amount :"))
    query="update users set BALANCE = BALANCE + %s where USER_ID = %s"
    exec_query(query,(amt,id))
    logging.info(f"AMOUNT {amt} DEPOSITED SUCCESSFULLY FOR USER ID {id}")
    choice=int(input("press 1 to check current balance or press any key to exit :"))
    if choice == 1:
        mob=input("enter your mobile number which is registerd :")
        passwrd=input("enter your password :")
        qur3="select BALANCE from users where PHONE_NO=%s and PASSWORD=%s"
        cur_amt=exec_query(qur3,(mob,passwrd),fetch=True)
        logging.info(f"CURRENT BALANCE FOR {mob} IS {cur_amt[0][0]}")
        print(cur_amt[0][0])
        print("THANK YOU !!")
    else:
        print("THANK YOU !!")