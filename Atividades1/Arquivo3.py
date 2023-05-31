#Objetivo: Criar um programa que organize uma lista de nomes em ordem alfabetica
#Bonus: Organizar por ordem alfabetica da ultima letra do nome

lista_de_nomes: [str] = ["Alexandre","Alice","André","Arthur","Arthur","Artur","Augusto","Bernardo","Bernardo","Bruno","Davi","Diego","Eduardo","Fabrício","Felipe","Fernando","Francisco","Francisco","Gabriel","Gabriel","Giovanna","Giovanni","Guilherme","Guilherme","Hector","Henrique","Inácio","João","João","Joaquim","Júlia","Lauren","Leonardo","Leonardo","Lucas","Marina","Matheus","Matheus","Paula","Pedro","Pedro","Pedro","Pedro","Rafael","Regis","Sofia","Stella","Thiago","Valentina","Vicente","Lucas"]
# Jeito fácil (🤢)
print(sorted(lista_de_nomes))

# Jeito legal
ordem_alfabetica = "abcdefghijklmnopqrstuvwxyz"
while not is_sorted(lista_de_nomes):
    pass



def is_sorted(lista_de_nomes) -> bool:
    for nome in lista:
        pass


def vem_antes(nome1: str, nome2: str) -> str:
    for index, letra in enumerate(nome1):
        if ordem_alfabetica.index(letra) > ordem_alfabetica.index(nome2[index]):
            return nome2
        elif ordem_alfabetica.index(letra) < ordem_alfabetica.index(nome2[index]):
            return nome1


