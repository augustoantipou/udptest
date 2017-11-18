# -*- coding: cp1252 -*-
# Teste para receber dados do X-Plane via UDP
# 2016 - Joz

# Importamos a biblioteca socket
from socket import *
import struct

# ip e porta do X-Plane
address = ('127.0.0.1', 49001)
# criamos um socket, precisamos definir uma família de endereço.
# Neste caso utilizaremos o IPv4 passando o parâmetro AF_INET
# E definimos nosso protocolo, se fosse TCP utilizaríamos SOCK_STREAM
# Mas como vamos utilizar o UDP, passamos o SOCK_DGRAM. 
server_socket = socket(AF_INET, SOCK_DGRAM)
# E finalizamos a criação do socket atrelando o endereço do X-Plane
server_socket.bind(address)

# O programa ficará escutando permanentemente
# Para parar o programa, dê um ctrl+c no idle
while True:
    # fazemos a leitura e passamos o dado para recv_data
    recv_data, addr = server_socket.recvfrom(512)

    # Extraimos o valor do pitch a partir do 9 ao 13 byte recebido
    pitch_degrees = struct.unpack('f', recv_data[9:13])
    print 'Pitch degrees:%.2f' % pitch_degrees