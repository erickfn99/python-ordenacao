import random

# Função genérica para retornar uma lista com tamanho que varia de 5 a 15 e valores que variam de 1 a 50
def novaLista():
    n = random.randint(5, 15)

    lista = []

    for i in range(0, n):
        lista.append(random.randint(1, 50))

    return lista

def bubble_sort(lista):
    troca = True

    while troca:
        # Verificador utilizado como critério de parada caso a lista já esteja ordenada
        troca = False

        # A lista é percorrida até o seu penúltimo elemento
        for i in range(0, len(lista)-1):
            # Caso o valor atual seja maior do que o próximo, a lista está desordenada e a troca é feita
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                troca = True

    return lista

lista = novaLista()

print('LISTA NÃO ORDENADA')
print(lista)

print('LISTA ORDENADA')
print(bubble_sort(lista))