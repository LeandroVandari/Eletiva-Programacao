#Objetivo: Criar um programa que organize uma lista de nomes em ordem alfabetica
#Bonus: Organizar por ordem alfabetica da ultima letra do nome

lista_de_nomes: [str] = ["Alexandre","Alice","André","Arthur","Arthur","Artur","Augusto","Bernardo","Bernardo","Bruno","Davi","Diego","Eduardo","Fabrício","Felipe","Fernando","Francisco","Francisco","Gabriel","Gabriel","Giovanna","Giovanni","Guilherme","Guilherme","Hector","Henrique","Inácio","João","João","Joaquim","Júlia","Lauren","Leonardo","Leonardo","Lucas","Marina","Matheus","Matheus","Paula","Pedro","Pedro","Pedro","Pedro","Rafael","Regis","Sofia","Stella","Thiago","Valentina","Vicente","Lucas"]
# Jeito fácil (🤢)
#print(sorted(lista_de_nomes))



# Jeito legal
ordem_alfabetica = "aãáàbcdeéfghiíjklmnoópqrstuúvwxyz"

def is_sorted(lista: [str]) -> bool:
    tamanho = len(lista)
    for index, nome in enumerate(lista):
        if index == tamanho - 1:
            return True
        
        if not vem_antes(nome, lista[index + 1]):
            return False
    return True

def vem_antes(nome1: str, nome2: str) -> bool:
    for index, letra in enumerate(nome1):
        if ordem_alfabetica.index(letra.lower()) > ordem_alfabetica.index(nome2[index].lower()):
            return False
        elif ordem_alfabetica.index(letra.lower()) < ordem_alfabetica.index(nome2[index].lower()):
            return True
        else:
            return True


while not is_sorted(lista_de_nomes):
    tamanho: int = len(lista_de_nomes)
    for index, nome in enumerate(lista_de_nomes):
        if index == tamanho - 1:
            continue
        if not vem_antes(nome, lista_de_nomes[index + 1]):
            lista_de_nomes[index] = lista_de_nomes[index + 1]
            lista_de_nomes[index + 1] = nome
print(lista_de_nomes)




        





