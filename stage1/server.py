import socket
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001

import socket

# AF_INETを使用し、UDPソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '0.0.0.0'
server_port = 9001
print('starting up on port {}'.format(server_port))

# ソケットを特殊なアドレス0.0.0.0とポート9001に紐付け
sock.bind((server_address, server_port))

clients_address = {}

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    if address not in clients_address:
        clients_address[address] = datetime.now()
    else:
        clients_address[address] = datetime.now()

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        for client in clients_address:
            time_difference = datetime.now() - clients_address[client]
            if time_difference.seconds > 60:
                print('Client {} is offline'.format(client))
                clients_address.pop(client)
            if client == address:
                continue

            print('sending data to {}'.format(client))
            sent = sock.sendto(data, client)

