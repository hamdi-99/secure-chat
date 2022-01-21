import socket
import errno
import select

from functions.encryptor_asym import decrypt_rsa, encrypt_rsa
from functions.encryptor_sym import encrypt_des, decrypt_des

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

def start_chat( my_username):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((IP, PORT))

    client_socket.setblocking(False)

    username = my_username.encode('utf-8')
    username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(username_header + username)
    print('****************************CHAT ROOM************************************')

    while True:

        message = input(f'{my_username} > ')

        if message:
            crypted = encrypt_rsa( message).encode('utf-8')
            message_header = f"{len(crypted):<{HEADER_LENGTH}}".encode('utf-8')
            client_socket.send(message_header + crypted)

        try:
            while True:

                username_header = client_socket.recv(HEADER_LENGTH)

                if not len(username_header):
                    print('Connection closed by the server')
                    exit()

                username_length = int(username_header.decode('utf-8').strip())

                username = client_socket.recv(username_length).decode('utf-8')

                message_header = client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                rcv = client_socket.recv(message_length).decode('utf-8')
                m = decrypt_rsa(rcv)

                print(f'{username} > {m}')

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                print('Reading error: {}'.format(str(e)))
                exit()
            continue

        except Exception as e:
            print('Reading error: {}'.format(str(e)))
            exit()
