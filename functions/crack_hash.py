import hashlib


def get_password_list_generator():
    with open("/home/hamdiharaketi/PycharmProjects/projet-securite/functions/passwords.txt", "r") as f:
        for i in f.readlines():
            yield (i)

def cracking_cli():
    message = input('enter your message\n')
    choice = input('choisissez un algorithme\n')
    if choice == 'a':
        cracked = crack_md5(message)
        if cracked:
            print(f'password is {cracked}')
        else:
            print(f"\n{message} cannot be cracked using md5 and given dict\n")
    elif choice == 'b':
        cracked = crack_sh1(message)
        if cracked:
            print(f'password is {cracked}')
        else:
            print(f"\n{message} cannot be cracked using sh1 and given dict\n")
    elif choice == 'c':
        cracked = crack_md5(message)
        if cracked:
            print(f'password is {cracked}')
        else:
            print(f"\n{message} cannot be cracked using sha256 and given dict\n")
    else:
        print('choix non valide')

def crack_md5(message):
    for i in get_password_list_generator():
        if hashlib.md5(i.encode('utf-8')).hexdigest() == message:
            return i
    return None


def crack_sh1(message):
    for i in get_password_list_generator():
        if hashlib.sha1(i.encode('utf-8')).hexdigest() == message:
            return i


def crack_sha256(message):
    for i in get_password_list_generator():
        if hashlib.sha256(i.encode('utf-8')).hexdigest() == message:
            print(f"\ncracked Message:\n{i}\n")
            return

