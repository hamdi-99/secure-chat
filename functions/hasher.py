import hashlib


def hash_md5(message):
    return hashlib.md5(message.encode('utf-8'))


def hash_sha1(message):
    return hashlib.sha1(message.encode('utf-8'))


def hash_256(message):
    return hashlib.sha256(message.encode('utf-8'))

def hasher_cli():
    message = input('entrer un message : \n')
    choice = input('choisissez un algorithme\n')
    if choice == 'a':
        print(f'message hashed : {hash_md5(message).hexdigest()}\n')
    elif choice == 'b':
        print(f'message hashed : {hash_sha1(message).hexdigest()}\n')
    elif choice == 'c':
        print(f'message hashed : {hash_256(message).hexdigest()}\n')
    else:
        print('choix non valide\n')