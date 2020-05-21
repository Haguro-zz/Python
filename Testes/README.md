# TESTES E TEORIAS EM PYTHON

------------------------
**Esquema de cores ANSI - \033[STYLE;TEXT;BACKm**

|STYLE          | TEXT |            | BACK 
|:--------------|:-----|:----------:|-----:
|0 - normal     | 30   |   branco   | 40  
|1 - negrito    | 31   |   vermelho | 41  
|4 - sublinhado | 32   |     verde  | 42  
|7 - inverter   | 33   |   amarelo  | 43  
|               | 34   |    azul    | 44  
|               | 35   |    roxo    | 45  
|               | 36   | azul claro | 46  
|               | 37   |   cinza    | 47  

Exemplo:
```
print('\033[1,31mOlá Mundo!\033[m
```
------------------------

**Laço - FOR**

_for c in range(INÍCIO, FIM, SALTOS):
	execução_

Exemplo:
```	
for c in range(10, 0, -1)
	print(c)
```
	
O programa irá imprimir os números de 10 à 0, contando sempre -1.

------------------------

**Tuplas, listas e dicionários**

_tupla = ('x', 'b', 'c')_

Tuplas são imutáveis, não podendo ter seus valores alterados.

_lista = ['x', 'y', 'z']_

Listas iniciam no índice [0], e podem ser alteradas:

```
lista.append('novo_valor')_ - Adiciona um valor no final da lista

lista.remove('valor')_ - Remove a primeira aparição do valor

lista.insert(0, 'novo_valor')_ - Substitui o valor do índice [0]
```
_dicionario = {'nome':'Hugo, 'idade':'22'}_

Dicionários colocam valores ligados à chaves, ao invés de número de índices:

```buildoutcfg
print(dicionario.values()) # Exibe os valores contidos no dicionário
print(dicionario.keys()) # Exibe as chaves dos índices
print(dicionario.items()) # Exibe o conjunto completo

dicionario['nome'] = 'Maria' # Adiciona 'Maria' ao dicionário

```

