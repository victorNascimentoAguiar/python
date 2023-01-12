# interando string com while em python
# 0123456789.............22
# exemplo simples
"""
frase = 'sinta o peso do martelo'
tamanhoFrase = len(frase)
contador = 0
while contador <= 22:
    print(frase[contador], contador)
    contador = contador + 1  # maneira mais simples: contador += 1
"""
# trasferinfo um frase para uma string vazia
# 0123456789........19
frase1 = 'pede pra nerfar noob'
tamanhoFrase1 = len(frase1)
contador = 0
fraseVazia = ''
inputDoUsuario = input('coloque a letra que voce quer que vire maiuscula: ')
while contador < tamanhoFrase1:
    letra = frase1[contador]
    if letra == inputDoUsuario:
        fraseVazia += inputDoUsuario.upper()
    elif letra == 'p':
        fraseVazia += 'P'
    else:
        fraseVazia += letra
    contador += 1

    print(fraseVazia)

    # contador += 1  # maneira mais longa : contador = contador + 1
