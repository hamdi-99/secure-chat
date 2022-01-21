import getpass
import hashlib

from phase12.User import User
from phase12.email_service import sendMail
from phase12.random_string import randomSring


def authenticate(mycursor):
    user = None
    while user is None:
        email = str(input("Enter your email: "))
        get_user_by_email_query = "SELECT * FROM users where email = %s"
        user_email = (email,)
        mycursor.execute(get_user_by_email_query, user_email)
        user = mycursor.fetchone();
        if user is None:
            print("wrong email")
            return None

    hashed = ''
    while hashed != user[3]:
        pwd = getpass.getpass("Enter password :")
        hashed = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        if hashed != user[3]:
            print("wrong password")
            return None
    """random = randomSring()
    sendMail(user[2], random)
    verif = ""
    while verif != random:
        verif = str(input("Enter verification code: "))
        if verif != random:
            print('invalid code')
            return None"""

    print("Welcome " + user[0] + " !")
    return User(user[0], user[2], user[3])
