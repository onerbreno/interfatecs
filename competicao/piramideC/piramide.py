import string

entrada = input()
qtd_letras = entrada.split(" ")[0]


if entrada.split(" ")[1] == 'minusculas':
    is_lower = True
elif entrada.split(" ")[1] == 'maiusculas':
    is_lower = False

if is_lower:
    alfabeto = list(string.ascii_lowercase)
else:
    alfabeto = list(string.ascii_uppercase)
    
resultado = []

for i in range(1, int(qtd_letras) + 1):
    teste = ''.join(alfabeto[0:i])
    if len(teste) < 26:
        teste = teste.zfill(26)
        teste = teste.replace('0', '.')
    resultado.append(teste)

print('\n'.join(resultado))



    
# print(qtd_letras)
# if len(titulo_formatado) < 12:
#     titulo_formatado = titulo_formatado.zfill(12)