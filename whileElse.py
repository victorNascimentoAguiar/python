contador = 0
acumulador = 0
while contador <= 100:
    if contador > 50:
        break
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('acabou :)')
