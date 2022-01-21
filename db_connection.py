import mysql.connector
from dotenv import load_dotenv
import os


def connect_db():
    load_dotenv()
    db = mysql.connector.connect(host=os.getenv('db_host'),
                                 user=os.getenv('db_user'),
                                 password=os.getenv('db_password'),
                                 port=os.getenv('db_port'),
                                 database=os.getenv('db_name'))
    mycursor = db.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS users(nom TEXT, prenom TEXT, email Text, pwd TEXT);")
    print('connected to database successfully!')
    return db, mycursor
