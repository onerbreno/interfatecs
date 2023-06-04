forca_silas = int(input())
posicao = input().split(" ")

    
cenario = [[0 for i in range(int(posicao[0]))] for j in range(int(posicao[1]))]

for i in range(int(posicao[0])):
    teste = input().split(" ")
    for j in range(int(posicao[1])):
        cenario[i][j] = teste[j]

for i in range(int(posicao[0])):
    for j in range(int(posicao[1])):
        if cenario[i][j] == "K":
            posicao_chave = [i, j]

posicao_silas = [1, 1] 

for i in range(int(posicao[0]) - 1):
    for j in range(int(posicao[1]) - 1):
        if(cenario[i + 1][j] == '#' or cenario[i][j + 1] == '#'):
            continue
        if cenario[i + 1][j] == '.' or cenario[i + 1][j] == 'K':
            posicao_silas[0] += 1
        if cenario[i][j + 1] == '.' or cenario[i][j + 1] == 'K':
            posicao_silas[0] += 1

print(posicao_silas)