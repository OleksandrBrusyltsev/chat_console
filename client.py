# import time, socket, sys
#
# socket_server = socket.socket()
# server_host = socket.gethostname()
# ip = socket.gethostbyname(server_host)
# sport = 8080
#
# print('This is your IP address: ', ip)
# server_host = input('Enter friend\'s IP address:')
# name = input('Enter Friend\'s name: ')
#
# socket_server.connect((server_host, sport))
#
# socket_server.send(name.encode())
# server_name = socket_server.recv(1024)
# server_name = server_name.decode("UTF-8")
#
# print(server_name, ' has joined...')
# while True:
#     message = (socket_server.recv(1024)).decode()
#     print(server_name, ":", message)
#     message = input("Me : ")
#     socket_server.send(message.encode())


import socket, threading



def send():
    while True:
        msg = input('\nMe > ')
        cli_sock.send(msg.encode(encoding="utf-8"))


def receive():
    while True:
        sen_name = cli_sock.recv(1024).decode('utf-8')
        data = cli_sock.recv(1024).decode('utf-8')

        print('\n' + str(sen_name) + ' > ' + str(data))


if __name__ == "__main__":
    # socket
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect
    HOST = 'localhost'
    PORT = 5023
    cli_sock.connect((HOST, PORT))
    print('Connected to remote host...')
    uname = input('Enter your name to enter the chat > ')
    cli_sock.send(uname.encode())

    thread_send = threading.Thread(target=send)
    thread_send.start()

    thread_receive = threading.Thread(target=receive)
    thread_receive.start()