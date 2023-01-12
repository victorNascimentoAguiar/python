lista = ['Julio', 'Victor', 'Vitoria', 'Brenda',
         'Valter']
print(lista)
começaComV = False
for valor in lista:
    if valor.lower().startswith('v'):
        começaComV = True
        print(valor)
if começaComV:
    print('contem três palavras com a letra V')
else:
    print('não tem palavra que começa com a letra V')
