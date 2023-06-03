import sys

entradas = []

while len(entradas) != 3:
    entradas.append(int(input()))

s = entradas[0]
a = entradas[1]
b = entradas[2]
saida = 0

while a <= b:
    caracteres = [caractere for caractere in str(a)]
    teste = 0
    for caractere in caracteres:
        teste += int(caractere)
    if(teste == s):
        saida += 1
    a += 1
    
print(saida, end='')