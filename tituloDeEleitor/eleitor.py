import sys
import platform

def formatar_titulo(linha):
    tituloFormatado = linha.replace('-', '')
    if len(linha) < 12:
        tituloFormatado = tituloFormatado.zfill(12)
    return tituloFormatado

def calcular_digitos_verificadores(titulo):
    # Multiplica-se cada dígito pelo peso correspondente
    soma = 0
    resto = 0
    dv1 = 0
    dv2 = 0
    
    for i in range(8):
        soma += int(titulo[i]) * (9 - i)
        # python não tem ++ ou --
    
    resto = soma % 11
    
    # Verifica o valor do primeiro dígito verificador
    if resto in (0, 1): # verifica se a variável resto tem um dos valores especificados na tupla (0, 1)
        if titulo[8:10] == '01' or titulo[9] == '2':
            # titulo[8:10] faz um slice 
            # e verifica se esse "trecho" (8ª e 9ª posição, 10 é desconsiderado seguindo o conceito de intervalo semiaberto) 
            # da string é igual a '01'
            dv1 = 1 - resto
    else:
        dv1 = 11 - resto
        
    # Calcula o segundo dígito verificador
    soma = (int(titulo[8]) * 4) + (int(titulo[9]) * 3) + (dv1 * 2)
    resto = soma % 11

    if resto in (0, 1):
        if titulo[8:10] == '01' or titulo[9] == '2':
            dv2 = 1 - resto
    else:
        dv2 = 11 - resto

    return str(dv1) + str(dv2)

def verificar_titulo(linha):
    titulo = formatar_titulo(linha)

    resultado = calcular_digitos_verificadores(titulo)
    if titulo[10:12] == resultado:
        return 'correto'
    else:
        return resultado

resultados = []

while True:
    linha = input()
    if linha == "0000000000-00":
        break
    resultados.append(verificar_titulo(linha))

if (platform.system() == 'Windows'): # os.linesep usado como "quebra de linha universal" quebra duas linhas no Windows
    print('\n'.join(resultados), end='')
    # Une todos os elementos da lista em uma única string, separando cada elemento por uma nova linha (\n).
    # (end=''), garante que não haja uma linha em branco adicionada no final da saída
else:
    import os
    print(os.linesep.join(resultados), end='')

sys.exit()