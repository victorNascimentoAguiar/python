secreto = 'abominavel'
digitados = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('digite uma letra: ')
    if len(letra) > 1:
        print('so vale digitar uma letra :)')
        continue
    digitados.append(letra)

    if letra in secreto:
        print(f'uhuu, a letra "{letra}"existe na palavra secreta.')
    else:
        print(f'ops, a letra "{letra}" não esta na palavra secreto.')
        digitados.pop()

    secretoTemporario = ''
    for letraSecreta in secreto:
        if letraSecreta in digitados:
            secretoTemporario += letraSecreta
        else:
            secretoTemporario += '*'
    if secretoTemporario == secreto:
        print(f'PARABENS VOCÉ GANHOU, A PALAVRA ERA "{secretoTemporario}"')
        break
    else:
        print(f'a palavra secrata é essa"{secretoTemporario}" ')
    if letra not in secreto:
        chances -= 1
        print(f'voce ainda tem "{chances} chances')
