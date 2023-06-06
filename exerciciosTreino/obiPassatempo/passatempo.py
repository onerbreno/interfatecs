import sys

entradas = []

for linha in sys.stdin:
    entradas.append(linha.replace('\n', ''))

print(entradas)
# qtd_linhas = int(entradas[0].split(" ")[0])
# qtd_colunas = int(entradas[0].split(" ")[1])


# restricoes_linhas = []
# for linha in range(1, qtd_linhas + 1):
#     restricoes_linhas.append(entradas[linha].split(" ")[qtd_colunas])

# restricoes_colunas = entradas[len(entradas) - 1].split(" ")

# aux = 1
# lista_variaveis = []
# while aux < len(entradas) - 1:
#     teste = entradas[aux].split(" ")
#     teste.pop()
#     variaveis.append(teste)
#     aux += 1

# for variaveis in lista_variaveis:
#     for variavel in variaveis:
#         if ():
#             break
        
# print(variaveis)
# print(entradas)
# print(qtd_linhas)
# print(qtd_colunas)
# print(restricoes_linhas)
# print(restricoes_colunas)

