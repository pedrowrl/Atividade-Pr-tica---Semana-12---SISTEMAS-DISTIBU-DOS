# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267. 

import socket

multicast_group = '224.0.0.1'
server_address = ('', 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def inverter_string(string):
    return string[::-1]

while True:
    print('Aguardando mensagem...')

    data, address = sock.recvfrom(1024)
    message = data.decode('utf-8')
    print(f'Recebido "{message}" de {address}')

    inverted_message = inverter_string(message)

    sock.sendto(inverted_message.encode('utf-8'), address)
