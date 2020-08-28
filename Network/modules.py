#!/usr/bin/python3

import socket
import requests

# Servidor Socket
def server_sock():

    # Criando o socket IPv4 - TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Parâmetros do servidor - Local:9999
    host = ''
    port = 9999

    # Modo de listen
    server.bind((host, port))
    server.listen(1) # Apenas uma conexão aceita
    print(f'Porta de comunicação: {port}')

    while True:
        client, ip = server.accept()

        print('Conectado à: ', ip)

        msg = 'Conectado'
        client.send(msg.encode('ascii'))
        client.close() # Encerra a conexão
