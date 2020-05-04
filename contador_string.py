#!/usr/bin/python3

#Este programa lê um texto digitado, e mostra:

texto = input('Digite um texto qualquer: ').strip()

print('\033[7m', texto.upper(), '\033[m') #O texto com todas as letras maiúsculas
print('\033[7m', texto.lower(), '\033[m') #O texto com todas as letras minúsculas

splitTexto = texto.split()
joinTexto = ''.join(splitTexto)

print('A frase possui {}{}{} letras!'.format('\033[1;33m', len(joinTexto), '\033[m')) #A quantidade de caracteres, exceto os espaços
print('A primeira palavra da frase, possui {}{}{} caracteres!'.format('\033[1;36m', len(splitTexto[0]), '\033[m')) #A quantidade de caracteres da primeira palavra
print('A última palavra do texto é: \033[1;31m', splitTexto[len(splitTexto)-1]) #A última palavra contida no texto