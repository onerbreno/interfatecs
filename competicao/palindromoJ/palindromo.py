import sys
from unicodedata import normalize

entradas = []
accents = ['á','é', 'í','ó', 'ú', 'â','ê', 'ô', 'ã', 'à', 'í', 'ó']
accentsOff = ['a','e', 'i','o', 'u', 'a','e', 'o', 'a', 'a', 'i', 'o']

for linha in sys.stdin:
    entradas.append(linha.replace('\n', '').strip('.'))

resultados = []
for entrada in entradas:
    for char in entrada:
        if char in accents:
            teste = accentsOff[accents.find(char)]
            
    stringLimpa = normalize('NFKD', entrada).encode('ASCII', 'ignore').decode('ASCII')
    print(stringLimpa)
    string = stringLimpa.split(" ")
    stringLimpa = ''.join(string)

    stringReversa = ''
    for i in stringLimpa:
        stringReversa = i + stringReversa

    # print(stringReversa)
    # print(stringLimpa)
    if stringReversa.lower() == stringLimpa.lower():
        resultados.append("Parabens, voce encontrou o Palindromo Perdido!")
    else:
        resultados.append("A busca continua, o Palindromo Perdido ainda nao foi encontrado.")
        
# print('\n'.join(resultados))