num1 = 10
num2 = 3
divisão = num1/num2
print('{:.2f}'.format(divisão))
nome = 'victor'
sobrenome = 'nascimento'
nome_formatado = '{0:@^20}''{1:#^20}'.format(nome, sobrenome)
print(nome_formatado)
print(nome.lower(), sobrenome.lower())
print(nome.upper(), sobrenome.upper())
print(nome.title(), sobrenome.title())
