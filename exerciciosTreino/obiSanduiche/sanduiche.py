import sys

entradas = []

for linha in sys.stdin:
    entradas.append(linha.replace('\n', ''))

qtd_ingredientes = entradas[0].split(' ')[0]
# qtd_pares = entradas[0].split(' ')[1]
# print(entradas)
# print(qtd_ingredientes)
# print(qtd_pares)

ingredientes = [ingrediente + 1 for ingrediente in range(int(qtd_ingredientes))]

restricoes = [entrada for entrada in entradas[1:]]

# print(restricoes)
# print(ingredientes)

possibilidades = 0

for ing1 in ingredientes:
    for ing2 in ingredientes:
        if str(ing1) != str(ing2):
            combinacao = ' '.join([str(ing1), str(ing2)])
            if combinacao not in restricoes:
                # print(combinacao)
                possibilidades += 1
            
print(possibilidades, end=' ')
