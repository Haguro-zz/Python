#!/usr/bin/python3

import modules
import random

# Estrutura de menu
def menu():
    corLetra = random.randrange(30, 37)
    author = ' By: Hagur0 '

    print(f'''\033[1;{corLetra}m
    ╔═╗┌─┐┌┐┌┌┬┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┬  ┌─┐
    ╠═╝├┤ │││ │ ├┤ └─┐ │    ║ │ ││ ││  └─┐
    ╩  └─┘┘└┘ ┴ └─┘└─┘ ┴    ╩ └─┘└─┘┴─┘└─┘
    \033[m''')

    print(f'\n{author:=^45}')

    menu = ('''
        1) Socket Server (Listening Mode)
        0) Sair
        ''')

    print(menu)

    while True:

        opcao = input('Digite a opção desejada ("M" para ver o menu): ')

        if opcao in 'mM':
            print(menu)

        elif opcao == '1':
            modules.server_sock()

        elif opcao == '0':
            break

        else:
            print('\033[1;31m\nOpção inválida!\033[m\n')
            print('*' * 20)
            print('\n')

    print('\nAté logo!')

# Programa Principal

menu()
