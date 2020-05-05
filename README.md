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

for c in (INÍCIO, FIM, SALTOS):
	execução

Exemplo:
```	
for c in (10, 0, -1)
	print(c)
	
O programa irá imprimir os números de 10 à 0, contando sempre -1.
```	
------------------------


