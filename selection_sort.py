import random

# Função genérica para retornar uma lista com tamanho que varia de 5 a 15 e valores que variam de 1 a 50
def novaLista():
    n = random.randint(5, 15)

    lista = []

    for i in range(0, n):
        lista.append(random.randint(1, 50))

    return lista

def selection_sort(lista):
    for i in range(0, len(lista)):
        # Assume-se que o indice do menor valor seja o i
        menor_indice = i

        for j in range(i+1, len(lista)):
            # Se verifica se algum valor na lista é menor do que o da posição i e caso seja, se armazena esse indice
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        
        # O menor valor é trocado com o do indice atual do laço i
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista

lista = novaLista()

print('LISTA NÃO ORDENADA')
print(lista)

print('LISTA ORDENADA')
print(selection_sort(lista))