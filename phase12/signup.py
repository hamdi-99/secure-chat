import mysql.connector
import getpass
import hashlib

from phase12.User import User


def signup(db, mycursor):
    prenom = str(input("Enter your name: "))
    nom = str(input("Enter your last name: "))
    email = str(input("Enter your email: "))
    while (email != prenom + '.' + nom + '@insat.ucar.tn'):
        print('email must respect the format name.lastname@insat.ucar.tn')
        email = str(input("Enter your email: "))

    pwd = getpass.getpass("Enter your password: ")
    pwd_conf = getpass.getpass("Confirm your password: ")
    while pwd != pwd_conf:
        print('no password match')
        pwd_conf = getpass.getpass("Confirm your password: ")

    hashed = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
    insert_user_query = "INSERT INTO users (nom, prenom, email, pwd) VALUES (%s, %s, %s, %s)"
    values = (nom, prenom, email, hashed)
    mycursor.execute(insert_user_query, values)
    db.commit()

    print("user added successfully!")
    return User(prenom, email, hashed)
