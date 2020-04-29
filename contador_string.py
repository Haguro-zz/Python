#!/usr/bin/python3

#Este programa lê um texto digitado, e mostra:

texto = input('Digite um texto qualquer: ')

print(texto.upper()) #O texto com todas as letras maiúsculas
print(texto.lower()) #O texto com todas as letras minúsculas

splitTexto = texto.split()
joinTexto = ''.join(splitTexto)

print('A frase possui {} caracteres!'.format(len(joinTexto))) #A quantidade de caracteres, exceto os espaços
print('A primeira palavra da frase, possui {} caracteres!'.format(len(splitTexto[0]))) #A quantidade de caracteres da primeira palavra

