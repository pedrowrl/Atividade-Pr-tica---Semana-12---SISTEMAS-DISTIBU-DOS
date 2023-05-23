# Aluno: Pedro Wilson Rodrigues de Lima.
# Nº de Matrícula: 2020267.

import socket

multicast_group = '224.0.0.1'
server_address = ('', 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

message = input('Digite uma mensagem: ')

sock.sendto(message.encode('utf-8'), server_address)

data, address = sock.recvfrom(1024)
inverted_message = data.decode('utf-8')

print(f'Resposta do servidor: {inverted_message}')

sock.close()
