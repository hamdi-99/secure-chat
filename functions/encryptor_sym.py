from Crypto.Cipher import AES, DES
import base64

key_des = '12345678'
key_aes = '1234567890123456'


def encryptor_sym_cli():
    message = input('entrer un message:\n')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'encrypted message :{encrypt_des(key_des, message)} ')
        print('des')
    elif choice_algo == 'b':
        print(f'encrypted message :{encrypt_aes(key_aes, message)} ')
        print('aes')


def decryptor_sym_cli():
    message = input('entrer un message:')
    choice_algo = input('choisissez un algorithme : \n')
    if choice_algo == 'a':
        print(f'decrypted message :{decrypt_des(key_des, message)} ')
        print('des')
    elif choice_algo == 'b':
        print(f'encrypted message :{decrypt_aes(key_aes, message)} ')
        print('aes')


def pad(text):
    n = len(text) % 8
    return text + (' ' * (8 - n))


def encrypt_des(key, message):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(message)
    encrypted_text = des.encrypt(padded_text)
    return base64.b64encode(encrypted_text).decode('utf-8')


def decrypt_des(key, cipher):
    des = DES.new(key, DES.MODE_ECB)
    message = base64.b64decode(cipher)
    decryptedMsg = des.decrypt(message)
    return decryptedMsg.decode("utf-8").strip()


c = encrypt_des('12345678', 'hamza')
print(c)
print(decrypt_des('12345678', c))


def pad_16(text):
    n = len(text) % 16
    return text + (' ' * (16 - n))


def encrypt_aes(key, message):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    message = pad_16(message)
    ciphertext = obj.encrypt(message)
    return base64.b64encode(ciphertext).decode('utf-8')


def decrypt_aes(key, cipher):
    obj = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    message = base64.b64decode(cipher)
    decrypted_message = obj.decrypt(message)
    return decrypted_message.decode("utf-8").strip()
