'''Programa que simula o funcionamento de um caixa eletrônico

Lê o valor de saque (int) e informa quantas cédulas e de quais valores
serão emitidas.

Cédulas possíveis: R$50, R$20, R$10 e R$1.

'''

import random

corLetra = random.randrange(30,37)

print(f'''\033[1;{corLetra}m
      _        _________   ____    ____  
     / \      |  _   _  | |_   \  /   _| 
    / _ \     |_/ | | \_|   |   \/   |   
   / ___ \        | |       | |\  /| |   
 _/ /   \ \_     _| |_     _| |_\/_| |_  
|____| |____|   |_____|   |_____||_____|
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[m
''')



while True:
    valor = int(input('Digite o valor que deseja sacar: R$'))

    if valor == 0:
        print('Não se pode sacar R$0,00. Tente outro valor.')

    elif valor < 0:
        print('Valor negativo não suportado na operação! Tente outro valor.')

    else:
        total = valor
        cedula = 50 # Maior cédula
        totalCedula = 0 # inicialização de variável

        while True:
            if total >= cedula:
                total -= cedula
                totalCedula += 1
            else:
                if totalCedula > 0:
                    print(f'{totalCedula} de R${cedula}')
                if cedula == 50:
                    cedula = 20
                elif cedula == 20:
                    cedula = 10
                elif cedula == 10:
                    cedula = 1
                totalCedula = 0

                if total == 0:
                    break
        print('\nObrigado, volte sempre!')
        break
