import sys
qtd_livros = input()
livros = input()

livros_desordenados = []
livros_ordenados = []
for char in livros:
    livros_ordenados.append(char)
    livros_desordenados.append(char)

livros_ordenados.sort()

contador = -1
for char in livros_desordenados:
    index_char_des = livros_desordenados.index(char)
    index_char_ord = livros_ordenados.index(char)
    if (index_char_des != index_char_ord):
        if (index_char_ord - index_char_des) > 5:
            print('A Database Systems student read a book.')
            sys.exit()
        else:
            contador += 1
print(contador)