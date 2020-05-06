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

print('''
1) Contagem Regressiva
2) Poema
3) Data
0) Sair
''')

opcao = int(input('Digite a opção desejada: '))
data = datetime.datetime.now()

while True:
    if opcao == 1:
        for c in range(10, 0, -1):
            print(c)
            sleep(0.1)  # Timer para execução do laço
        print('\033[1;31m\nACABOU!!!\033[m')
        break

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
        break

    elif opcao == 3:
        print(data)
        break

    elif opcao == 0:
        break

    else:
        print('\033[1;31m\nOpção inválida!\033[m')
        print('*' * 20)
        opcao = int(input('Digite a opção desejada: '))

'''novaOpcao = str(input('Deseja retornar ao menu? [S/N] '))
if novaOpcao in 'sS':
    return '''

print('\nAté logo!')