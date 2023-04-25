import random
n=int(input('digite a dimnesão n da matriz: '))
m=int(input('digite a dimensão m da matriz: '))
matriz=[]
for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(random.randint(0,100))
    matriz.append(linha)
print(matriz)
    