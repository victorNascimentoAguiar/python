# loop infinito!
"""
while True:
    nome = input("qual seu nome:")
    print(f'{nome}!')
"""
# de 0 a 100
"""
x = 0
while x <= 100:
    print(x)
    x = x+1
print('chegou no limite!')
"""
# X e Y (colunas e linhas)
x = 0
while x <= 10:
    y = 0
    while y <= 5:
        print(f"({x},{y})")
        y = y + 1  # maneira simplificada y += 1
    x = x + 1  # maneira simplificada x += 1

print('acabou')
