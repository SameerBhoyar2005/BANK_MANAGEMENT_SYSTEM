from sql_query import exec_query
from create_account import create_new_account
from show_data import fetch_data
from withdraw import withdraw_money
from deposit import deposit
import logger
import logging


def main():
    while True:
        choice=int(input("PRESS \n 1 : TO CREATE A NEW ACCOUNT \n 2 : TO SHOW INFORMATION FOR A USER ID \n 3 : TO DEPOSIT \n 4 : TO WITHDRAW \n 5 : TO EXIT \n GIVE ME YOUR CHOICE : "))
        
        if choice == 1:
            create_new_account()
        elif choice == 2:
           data=fetch_data()
           print(data)
        elif choice == 3:
            deposit()
        elif choice == 4:
            withdraw_money()
        elif choice == 5:
            print("THANK YOU AND COME AGAIN")
            return
        else:
            print("INVALID CHOICE")

if __name__=="__main__":
    main()