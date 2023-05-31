#Objetivo do arquivo: printar qual a posição de um valor da lista

lista=[2,6,1,23,6,8,1]
x=len(lista)


# Maneira 1:
for i in range(x): 
    print(f"O {i+1}º valor da lista é {lista[i]}")


# Maneira 2:
for index, valor in enumerate(lista):
    print(f"O {index+1}º valor da lista é {valor}")