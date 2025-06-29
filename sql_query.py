import mysql.connector 
import os
from dotenv import load_dotenv
load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
passwd=os.getenv("passwrd")
database=os.getenv("database")

def connection_to_database():
    return mysql.connector.connect(
    host=host,
    user=user,
    database=database,
    password=passwd
)
def exec_query(query,params=None,fetch=False):
    con=connection_to_database()
    cur=con.cursor()
    cur.execute(query,params)
    data=None
    if fetch:
        return cur.fetchall()
    if not fetch:
        con.commit()
    con.close()
    cur.close()
    


