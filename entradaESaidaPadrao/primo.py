import sys

while True:
    linha = input()
    if(linha == 0):
        break

    primo = int(linha)
    isPrimo = True

    for i in range(2, primo):
        if((primo % i) == 0 & (i != primo)):
            isPrimo = False
            break
    if(primo > 1):
        if isPrimo:
            print(primo);
# sys.exit()