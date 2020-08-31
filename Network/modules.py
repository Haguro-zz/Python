#!/usr/bin/python3

import socket
import requests
import optparse
import threading

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

def portscanner(host, port):

    #Estabelecimento de conexão
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for p in port:
        newPort = int(p)

        if sock.connect_ex((host,newPort)):
            print(f'\n\033[1,31m][-] A porta {newPort} está fechada!\n')
        else:
            print(f'\033[1,32][+] A porta {newPort} está aberta!\n')
