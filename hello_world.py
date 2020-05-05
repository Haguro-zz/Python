#!/usr/bin/python3


print("""\033[1;35m
 __ __    ___  _      _       ___          __    __   ___   ____   _      ___    __ 
|  |  |  /  _]| |    | |     /   \        |  |__|  | /   \ |    \ | |    |   \  |  |
|  |  | /  [_ | |    | |    |     | _____ |  |  |  ||     ||  D  )| |    |    \ |  |
|  _  ||    _]| |___ | |___ |  O  ||     ||  |  |  ||  O  ||    / | |___ |  D  ||__|
|  |  ||   [_ |     ||     ||     ||_____||  `  '  ||     ||    \ |     ||     | __ 
|  |  ||     ||     ||     ||     |        \      / |     ||  .  \|     ||     ||  |
|__|__||_____||_____||_____| \___/          \_/\_/   \___/ |__|\_||_____||_____||__|
\033[m""")
print('-' * 85)

#Formatação de string dentro de uma mensagem utilizando Chaves
nome = input('Olá, digite o seu nome: ')
capitalizado = nome.title()

primeiroNome = capitalizado.split() #Divide o texto em uma lista, separando cada palavra, identificada pelo espaço.
nomeCompleto = ' '.join(primeiroNome) #Junta as palavras novamente, adicionando espaços entre as palavras separadas pelo split().

print('Seja bem vindo, {}{}{}'.format('\033[0;34m', primeiroNome[0], '\033[m'))
print('Seu nome completo é\033[1;36m', nomeCompleto)

#Informações possíveis sobre a digitação
#print('Algumas informações técnicas sobre a frase:')
#print('O tipo primitivo digitado é: ', type(nome))
#print('Contém somente espaços? ', nome.isspace())
#print('É um número? ', nome.isnumeric())
#print('É alfabético? ', nome.isalpha())
#print('É alfanúmerico? ', nome.isalnum())
#print('Todos os caracteres são maiúsculos? ', nome.isupper())
#print('Todos os caracteres são minúsculos?', nome.islower())
#print('O texto está capitalizado (inicial maiúscula)? ', nome.istitle())