#!/usr/bin/python3

'''
1) Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios, guardados em um dicionário e exiba em ordem de ganhadores.
'''

#1)

from random import randrange
from time import sleep

jogadores = {} # Inicia o dicionário
listaJogador = [] # Inicia a lista que conterá o dicionário

quantJogador = int(input('Quantos jogadores participarão? '))

for j in range(0,quantJogador):
    jogadores['nome'] = (str(input('Digite o nome do jogador: ')).capitalize())
    jogadores['dado'] = randrange(1,7,1, int)
    listaJogador.append(jogadores.copy()) # Adiciona os valores recebidos no dicionário à lista

for c in listaJogador:
    for v in c.values():
        print(f'{c["nome"]} tirou {c["dado"]}!')
        sleep(0.5)
        break

listaJogador.sort(key=lambda item: item.get("dado"), reverse=True) # Organiza a lista pelo valor do dado

print(f'\n{" RANKING ":=^20}\n')

for c in listaJogador:
    for v in c.values():
        print(f'{c["nome"]} com {c["dado"]} no dado!')
        sleep(0.5)
        break