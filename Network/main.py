#!/usr/bin/python3

import modules
import random

# Estrutura de menu
def menu():
    corLetra = random.randrange(30, 37)
    texto = ' By: Hagur0 '

    print(f'''\033[1;{corLetra}m
    ╔═╗┌─┐┌┐┌┌┬┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┬  ┌─┐
    ╠═╝├┤ │││ │ ├┤ └─┐ │    ║ │ ││ ││  └─┐
    ╩  └─┘┘└┘ ┴ └─┘└─┘ ┴    ╩ └─┘└─┘┴─┘└─┘
    \033[m''')

    print(f'\n{texto:=^35}')

    menu = ('''
        1) Socket Cliente
        2) Socket Servidor
        0) Sair
        ''')

    print(menu)

    while True:

        opcao = int(input('Digite a opção desejada (`999` para ver o menu): '))

        if opcao == 999:
            print(menu)

        elif opcao == 1:
            host = input('Digite o host: ')
            port = int(input('Digite o número da porta: '))

            modules.client_sock(host, port)

        elif opcao == 2:
            modules.server_sock()

        elif opcao == 0:
            break

        else:
            print('\033[1;31m\nOpção inválida!\033[m\n')
            print('*' * 20)
            opcao = int(input('\nDigite a opção desejada: '))

    print('\nAté logo!')

# Programa Principal

menu()
