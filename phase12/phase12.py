from phase12.authenticate import authenticate
from phase12.signup import signup
from phase3.phase3 import run_phase3


def run_phase12(db, mycursor):
    print('choose your option')
    print('1- Enregistrement')
    print('2- Authentification')
    print('3- Quitter')
    choice = int(input('choisissez une option :'))
    handle_choice12(db, mycursor, choice)


def handle_choice12(db, cursor, choice):
    while (1):
        if choice == 1:
            user = signup(db, cursor)
            if user:
                print('signup')
                run_phase3(user)
        elif choice == 2:
            user = authenticate(cursor)
            if user:
                print('auth')
                run_phase3(user)

        elif choice == 3:
            exit()
        else:
            print('faites un choix valide')
