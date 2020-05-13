#!/usr/bin/python3

'''
1) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios, guardados em um dicionário e exiba em ordem de ganhadores.
'''

#1)

from random import randrange
from time import sleep

jogadores = {}
listaJogador = []

quantJogador = int(input('Quantos jogadores participarão? '))

for j in range(0,quantJogador):
    jogadores['nome'] = (str(input('Digite o nome do jogador: ')))
    jogadores['dado'] = randrange(1,7,1, int)
    listaJogador.append(jogadores.copy())
    jogadores.clear()

for c in listaJogador:
    for v in c.values():
        print(f'{c["nome"]} tirou ', end=' ')
        print(c['dado'])
