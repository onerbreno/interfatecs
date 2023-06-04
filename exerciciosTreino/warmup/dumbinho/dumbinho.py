numeros = input()
soma = 0

for numero in numeros:
    soma += int(numero)
    
if soma % 2 == 0:
    empresa = "dumbinho"
else:
    empresa = "8-bonito"

print(empresa)