# uma simples caculadora que não tem tratamento de exeções
num1 = int(input('digite um numero: '))
operador = input('digite um operador (+,-,*,/): ')
num2 = int(input('digite outro numero: '))

if operador == '+':
    print(num1 + num2)
elif operador == '-':
    print(num1 - num2)
elif operador == '*':
    print(num1 * num2)
elif operador == '/':
    print(num1 / num2)
else:
    print('operador invalido')
