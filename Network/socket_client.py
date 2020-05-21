#!/usr/bin/python3

import socket

host = input('Digite o host: ')
port = int(input('Digite o número da porta: '))

# Criando um cliente IPv4 - TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Iniciando a conexão
cliente.connect((host, port))

# Enviando uma mensagem de solicitação de página index.html ao host
mensagem = (f'GET /index.html HTTP/1.1\r\nHost: {host}:{port}\r\n\r\n')
cliente.send(mensagem.encode('ascii')) # Converte a mensagem em Bytes

# Recebendo a resposta com buffer = 4096
resposta = cliente.recv(4096)
print(resposta)