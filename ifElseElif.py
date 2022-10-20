# exemplo simples utilizando o input ,if e elif.
"""
nome = input(' digite seu nome: ')
idade = input("digite sua idade: ")
idade = int(idade)
# idade limite
idadeLimite = 18

if idade >= idadeLimite:
    print(f'{nome} tem uma idade aceita. ')
else:
    print(f'{nome} não tem a idade aceita')
    """
# explo um pouco mais complexo usando input,if,elif e and.
"""
 nome = input(' digite seu nome: ')
 idade = input("digite sua idade: ")
 idade = int(idade)
 # idade limite
 muitoJovem = 20
 muitoVelho = 30
 if idade >= muitoJovem and idade <= muitoVelho:
     print(f'{nome} tem uma idade aceita. ')
 else:
     print(f'{nome} não tem a idade aceita')
 """
# conta de login bem basica não utilizada.
usuario = input('digite usuario:')
senha = input('digite senha: ')

usuarioBD = 'Arceus'
senhaBD = 'vitito'
if usuario == usuarioBD and senha == senhaBD:
    print('usuario logado ;)')
else:
    print('usuario ou senha incorreto :(')
