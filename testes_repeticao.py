'''
1) Programa que mostra na tela uma contagem regressiva para o estoure de fogos de artifício, indo de 0 a 10.
2) Programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
3) Programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
4) Tabuada
5) Programa que leia o nome, idade e sexo de 4 pessoas e mostre: a média de idade, o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
'''
#1)
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(0.1) # Timer para execução do laço
    
print('\033[1;31m🎆🎆🎆🎆 FELIZ ANO NOVO 🎆🎆🎆🎆\033[m')
'''
'''
#2)

for c in range(0, 50):
    if c % 2 == 0:
        print(c)
'''
'''
#3)
for c in range(0, 500):
    if c % 2 == 1 and c % 3 == 0:
        print(c)
'''
'''
#4)
multiplo = 0
numero = []
n = int(input('Digite o número para obter a tabuada: '))
print('A tabuada de \033[1;35m{}\033[m, é:\n'.format(n))
for c in range (0,10):
    multiplo +=1
    numero.append(n * multiplo)
    print('{} x {} = {}'.format(n, multiplo, numero[c]))
'''
#5)
somaIdade = 0
mdIdade = 0
maiorIdade = 0
nomeHomem = ''
menorIdade = 0
quantMulher = 0
for c in range(1,5):
    print('=====\033[2;32m {}ª PESSOA\033[m ===='.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()

    somaIdade += idade

    #Inicializando os comparativos da idade masculina
    if c == 1 and sexo in 'mM':
        maiorIdade = idade
        nomeHomem = nome
    #Fazendo as comparações a partir do segundo loop:
    if sexo in 'mM' and idade > maiorIdade:
        maiorIdade = idade # Recebe a nova idade
        nomeHomem = nome # Recebe o novo nome

    if sexo in 'fF' and idade < 20:
        quantMulher += 1

# Imprimindo os resultados:

mdIdade = somaIdade / 4
print('\nA média de idade do grupo é de \033[2;36m{}\033[m anos'.format(mdIdade))

print('\nO homem mais velho se chama \033[1;31m{}\033[m e tem \033[1;31m{}\033[m anos'.format(nomeHomem, maiorIdade))

if quantMulher == 1:
    print('\nHá {} garota abaixo dos 20 anos no grupo!'.format(quantMulher))
elif quantMulher > 1:
    print('\nHá {} garotas abaixo dos 20 anos no grupo!'.format(quantMulher))
else:
    print('\nNão há mulheres abaixo dos 20 anos no grupo!')