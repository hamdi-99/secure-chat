import rsa
from elgamal import generate_keys, encrypt, decrypt

rsa_public, rsa_private = rsa.newkeys(512)
elgamal_keys = generate_keys()
elgamal_public, elgamal_private = elgamal_keys['publicKey'], elgamal_keys['privateKey']


def encryptor_cli():
    message = input('entrer un message:\n')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'encrypted message :{encrypt_elgamal(message, elgamal_public)} ')
        print('gamal')
    elif choice_algo == 'b':
        print(f'encrypted message :{encrypt_rsa(message, rsa_public)} ')
        print('rsa')


def decryptor_cli():
    message = input('entrer un message:\n')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'decrypted message :{decrypt_elgamal(message, elgamal_private)} ')
        print('gamal')
    elif choice_algo == 'b':
        print(f'encrypted message :{decrypt_rsa(message, rsa_private)} ')
        print('rsa')


def encrypt_elgamal(message, elgamal_public):
    return encrypt(elgamal_public, message)


def decrypt_elgamal(message, elgamal_private):
    return decrypt(elgamal_private, message)


def encrypt_rsa(message, rsa_public):
    crypted: bytes = rsa.encrypt(message.encode(), rsa_public)
    return crypted.hex()


def decrypt_rsa(message, rsa_private):
    crypto: bytes = rsa.decrypt(bytes.fromhex(message), rsa_private)
    return crypto.decode("utf-8").strip()
