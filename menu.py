#!/usr/bin/python3

from time import sleep
import datetime
import random

# Estrutura de menu

corLetra = random.randrange(30,37)

print(f'''\033[1;{corLetra}m
███    ███ ███████ ███    ██ ██    ██ 
████  ████ ██      ████   ██ ██    ██ 
██ ████ ██ █████   ██ ██  ██ ██    ██ 
██  ██  ██ ██      ██  ██ ██ ██    ██ 
██      ██ ███████ ██   ████  ██████ \033[m''')


menu = ('''
1) Contagem Regressiva
2) Poema
3) Data
0) Sair
''')

print(menu)


data = datetime.datetime.now()

while True:
    
    opcao = input('Digite a opção desejada ('m' para ver o menu): ')
    
    if opcao in 'Mm':
        print(menu)
    
    if opcao == 1:
        for c in range(10, 0, -1):
            print(c)
            sleep(0.1)  # Timer para execução do laço
        print('\033[1;31m\nACABOU!!!\033[m')

    elif opcao == 2:
        print('''\033[1m
        If the water forms
        the forms of the weeds, there—

        a long life is not by that
        a necessarily happy one.

        My friend. We
        reckon on a simple

        agreement,
        the fashion of a stone

        underground.\033[m''')

    elif opcao == 3:
        print(data)

    elif opcao == 0:
        break

    else:
        print('\033[1;31m\nOpção inválida!\033[m')
        print('*' * 20)
        opcao = int(input('Digite a opção desejada: '))

print('\nAté logo!')
