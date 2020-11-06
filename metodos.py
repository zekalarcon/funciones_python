import random


def ordenar(numeros):
    numeros.sort()
    num_ordenados = numeros
    return num_ordenados


def lista_aleatoria(inicio, fin, cantidad):

    lista_numeros = []

    while cantidad > 0:
        cantidad -= 1
        numero = random.randrange(inicio, fin + 1)
        lista_numeros.append(numero)
    
    return lista_numeros


def contar(lista_numeros, numero):
    contador = lista_numeros.count(numero)
    return contador


    