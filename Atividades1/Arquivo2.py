#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la


lista=[2,3,7,12,2]
print("Números da lista: ", ", ".join([str(i) for i in lista]))
print("Números da lista multiplicados por 2: ", ", ".join([str(i*2) for i in lista]))