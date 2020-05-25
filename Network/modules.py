#!/usr/bin/python3

import socket
import requests

# Cliente Socket
def client_sock(host, port):

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

