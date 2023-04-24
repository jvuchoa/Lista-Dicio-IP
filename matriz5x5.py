matriz5x5=[[1,2,3,4,5],[5,6,7,8,9],[2,3,4,5,1],[1,23,24,12,90],[2,33,66,90,11]]
# print(matriz5x5[0])
# print(matriz5x5[1])
# print(matriz5x5[2])
# print(matriz5x5[3])
# print(matriz5x5[4])
for lista in matriz5x5:
    for item in lista:
        if (item%2==0):
            print(item)
        elif(item==5):
            print(f'Esse número é cinco:\n{item}')
        elif(item%2!=0):
            print(f'Todos os números ímpares menos o cinco:\n{item}')
    