# desafio : duas colunas uma almenta e a outra diminui
coluna1 = 0
coluna2 = 10

while coluna1 <= 10:
    coluna2 = 10

    while coluna2 >= 0:
        print(f"({coluna1},{coluna2})")
        coluna1 += 1
        coluna2 -= 1
