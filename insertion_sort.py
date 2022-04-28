import random

# Função genérica para retornar uma lista com tamanho que varia de 5 a 15 e valores que variam de 1 a 50
def novaLista():
    n = random.randint(5, 15)

    lista = []

    for i in range(0, n):
        lista.append(random.randint(1, 50))

    return lista

def insertion_sort(lista):
    for i in range(0, len(lista)):
        j = i

        # Este laço verifica se um elemento é menor que o seu anterior e caso seja, trocam os valores
        while j > 0 and lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1

    return lista

lista = novaLista()

print('LISTA NÃO ORDENADA')
print(lista)

print('LISTA ORDENADA')
print(insertion_sort(lista))