'''
# indice   0   1   2     3    4    5     6
lista = ['V', 'I', 'C', 'T', 'O', 'R', 29, 19]
# indice   -7     -6   -5   -4   -3   -2    -1
String = 'VICTOR
print(String[3])
print(lista[-2])
print(lista[:6])
'''
'''
# concatenando listas
l1 = [1, '2', 3]
l2 = [4, '5', 6]
l3 = l1 + l2
l1.extend('V')
print(l1, l2, l3)
# lista e for ,comando range
lista3 = list(range(1, 11))
print(lista3)
soma = 0
for valor in lista3:
    soma += valor
    print(soma)
'''
'''
# elem
l4 = ['Stirng', True, 19, -29.3]
for elem in l4:
    print(f'o tipo de cada uma é:{type(elem)}e seu valor é {elem}')
'''
