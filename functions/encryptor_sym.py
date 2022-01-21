from Crypto.Cipher import AES, DES
import base64

key_des = '12345678'
key_aes = '1234567890123456'


def pad(text: str, modulo: int):
    n = len(text) % modulo
    return text.encode() + (b" " * (modulo - n))


def encryptor_sym_cli():
    message = input('entrer un message:\n')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'encrypted message :{encrypt_des(key_des, message)} ')
        print('des')
    elif choice_algo == 'b':
        print(f'encrypted message :{encrypt_aes256(key_aes, message)} ')
        print('aes')


def decryptor_sym_cli():
    message = input('entrer un message:\n')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'decrypted message :{decrypt_des(key_des, message)} ')
        print('des')
    elif choice_algo == 'b':
        print(f'encrypted message :{decrypt_aes256(key_aes, message)} ')
        print('aes')


def encrypt_des(key, message):
    des = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(message, 8)
    encrypted_text: bytes = des.encrypt(padded_text)
    return encrypted_text


def encrypt_aes256(key, message):
    padded_text = pad(message, 16)
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    cipher_text: bytes = cipher.encrypt(padded_text)
    return base64.b64encode(cipher.encrypt(padded_text))


def decrypt_des(key, message):
    des = DES.new(key.encode(), DES.MODE_ECB)
    decrypted_text: bytes = des.decrypt(bytes.fromhex(message))
    result = decrypted_text.decode("utf-8").strip()
    return result


def decrypt_aes256(key, message):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    enc = base64.b64decode(message)
    ciphertext: bytes = cipher.decrypt(bytes.fromhex(message))
    result = ciphertext.decode("utf-8").strip()
    return result
