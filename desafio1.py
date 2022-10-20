"""
Criar variaveis para nome (str), idade (int),
altura(float)e peso (float) de uma pessoa.
criar variaveis com o ano atual (int)
obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
obter o imc da pessoa com 2 casas decimais (peso altura da pessoa).
Exibir um texto com todos os valores na tela usando F-string (com as chaves)
"""
nome = input(" ")
idade = 35
altura = 1.8
peso = 80
ano_atual = 2022
nascimento = ano_atual-idade
imc = peso/(altura**2)
print(f'{nome} tem {idade} anos,{altura} de altura e seu peso é {peso}kg.')
print(f'o imc de {nome} é de {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
