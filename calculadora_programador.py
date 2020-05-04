#!/usr/bin/python3

''' Programa que lê um número inteiro e converte para base decimal, hexadecimal ou octal,
e calcula de acordo com a opção escolhida.'''

print('\033[7mCalculadora de Programação\033[m')
print('-' * 20)
print("""\033[1;1m1) Base Binária
2) Base Hexadecimal
3) Base octal\n\033[m""")
opcao = int(input('Digite a opção de conversão: '))

if opcao == 1:
    valorDecimal = int(input('\nDigite o valor decimal a ser convertido: '))
    valorInicial = valorDecimal
    valorBinario = []
    while valorDecimal >= 1:
        valorBinario.append(str(valorDecimal % 2))
        valorDecimal = valorDecimal // 2
    resultadoBinario = ''.join(reversed(valorBinario))
    print('\nO número decimal \033[1;33m{}\033[m equivale a \033[1;35m{}\033[m em binário!'.format(valorInicial, resultadoBinario))

elif opcao == 2:
    valorDecimal = int(input('\nDigite o valor decimal a ser convertido: '))
    valorInicial = valorDecimal
    valorHex = [] # Inicia a lista para inserir os valores obtidos dos restos
    while valorDecimal >= 1:
        valorHex.append(str(valorDecimal % 16)) # Calcula o resto, que entrará na lista, resultando no hexadecimal
        valorDecimal = valorDecimal // 16

    if '10' in valorHex:
        i = valorHex.index('10')
        valorHex[i] = 'A'
    if '11' in valorHex:
        i = valorHex.index('11')
        valorHex[i] = 'B'
    if '12' in valorHex:
        i = valorHex.index('12')
        valorHex[i] = 'C'
    if '13' in valorHex:
        i = valorHex.index('13')
        valorHex[i] = 'D'
    if '14' in valorHex:
        i = valorHex.index('14')
        valorHex[i] = 'E'
    if '15' in valorHex:
        i = valorHex.index('15')
        valorHex[i] = 'F'

    resultadoHex = ''.join(reversed(valorHex)) # Inverte a ordem da string, para apresentar o resultado corretamente
    print('\nO número decimal \033[1;33m{}\033[m equivale a \033[1;35m{}\033[m em hexadecimal!'.format(valorInicial, resultadoHex))

elif opcao == 3:
    valorDecimal = int(input('\nDigite o valor decimal a ser convertido: '))
    valorInicial = valorDecimal
    valorOctal = []
    while valorDecimal >= 1:
        valorOctal.append(str(valorDecimal % 8))
        valorDecimal = valorDecimal // 8
    resultadoOctal = ''.join(reversed(valorOctal))
    print('\nO número decimal \033[1;33m{}\033[m equivale a \033[1;35m{}\033[m em octal!'.format(valorInicial, resultadoOctal))

else:
    print('\033[1;31m\nOpção inválida!\033[m')
    print('*' * 20)


