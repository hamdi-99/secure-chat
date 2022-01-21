def encode_message(message):
    return message.encode("utf-8").hex()


def decode_message(message):
    return bytes.fromhex(message).decode("utf-8")


def encoder_cli():
    message = input('entrer votrer message\n')
    choice = input('codage ou decodage\n')
    if choice == 'a':
        print(f'message coded : {encode_message(message)}\n')
    elif choice == 'b':
        print(f'message decoded : {decode_message(message)}\n')
    else:
        print('choix non valide\n')