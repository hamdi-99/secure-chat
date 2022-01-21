from functions import *
from functions.encoder import encoder_cli
from functions.hasher import hasher_cli
from functions.encryptor_sym import encryptor_sym_cli, decryptor_sym_cli
from functions.encryptor_asym import encryptor_cli, decryptor_cli
from functions.crack_hash import cracking_cli
from chatroom.client import start_chat

def handle_choice3(choice, user):
    if choice == 1:
        encoder_cli()
    elif choice == 2:
        hasher_cli()
    elif choice == 3:
        cracking_cli()
    elif choice == 4:
        c1 = int(input('1-Encode\n 2-Decode\n faites votre choix'))
        if c1 == 1:
            encryptor_sym_cli()
        elif c1 == 2:
            decryptor_sym_cli()
        else:
            print('choix invalide !')
    elif choice == 5:
        c = int(input('1-Encode\n 2-Decode\n faites votre choix'))
        if c == 1:
            encryptor_cli()
        elif c == 2:
            decryptor_cli()
        else:
            print('choix invalide !')
    elif choice == 6:
         start_chat(user)
    elif choice == 7:
        exit(1)


def run_phase3(user):
    print('1- Codage et décodage d\'un message\n'
          '     a-Codage\n'
          '     b-Décodage')
    print('2- Hashage d\'un message\n'
          '     a-Md5\n'
          '     b-SHA1\n'
          '     b-SHA256')
    print('3- Craquage d\'un message\n'
          '     a-Md5\n'
          '     b-SHA1\n'
          '     b-SHA256')
    print('4- Chiffrement et déchiffrement symetrique d\'un message\n'
          '     a-DES\n'
          '     b-AES256')
    print('5- Chiffrement et déchiffrement asymétrique d\'un message\n'
          '     a-RSA\n'
          '     b-Elgamal')
    print('6-Communication sécurisé entre deux clients')
    print('7-Quitter\n')
    choice = int(input('Choisis une option\n'))
    handle_choice3(choice, user)
