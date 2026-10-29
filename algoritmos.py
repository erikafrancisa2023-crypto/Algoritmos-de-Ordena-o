
import random

def insercao(v):
    lista = v[:]
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = atual
    return lista

def intercala(esquerda, direita):
    resultado = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado

def intercala_sort(v):
    if len(v) <= 1:
        return v[:]
    meio = len(v) // 2
    esquerda = intercala_sort(v[:meio])
    direita = intercala_sort(v[meio:])
    return intercala(esquerda, direita)

def rapida(v):
    if len(v) <= 1:
        return v[:]
    pivo = random.choice(v)
    menores = []
    iguais = []
    maiores = []
    for valor in v:
        if valor < pivo:
            menores.append(valor)
        elif valor == pivo:
            iguais.append(valor)
        else:
            maiores.append(valor)
    return rapida(menores) + iguais + rapida(maiores)


def hibrida(v, corte=16):
    if len(v) <= corte:
        return insercao(v)
    pivo = random.choice(v)
    menores = []
    iguais = []
    maiores = []
    for valor in v:
        if valor < pivo:
            menores.append(valor)
        elif valor == pivo:
            iguais.append(valor)
        else:
            maiores.append(valor)
    return (
        hibrida(menores, corte)
        + iguais
        + hibrida(maiores, corte)
    )

def contagem(v):
    if len(v) <= 1:
        return v[:]
    menor = min(v)
    maior = max(v)
    faixa = maior - menor + 1
    contadores = [0] * faixa
    for valor in v:
        contadores[valor - menor] += 1
    resultado = []
    for i in range(faixa):
        quantidade = contadores[i]
        for j in range(quantidade):
            resultado.append(i + menor)
    return resultado

def base(v):
    if len(v) <= 1:
        return v[:]
    negativos = []
    positivos = []
    for valor in v:
        if valor < 0:
            negativos.append(-valor)
        else:
            positivos.append(valor)
    negativos = radix_positivo(negativos)
    positivos = radix_positivo(positivos)
    negativos.reverse()
    resultado_negativos = []
    for valor in negativos:
        resultado_negativos.append(-valor)
    return resultado_negativos + positivos

def radix_positivo(v):
    if len(v) <= 1:
        return v[:]
    lista = v[:]
    maior = max(lista)
    posicao = 1
    while maior // posicao > 0:
        baldes = [0] * 10
        for valor in lista:
            digito = (valor // posicao) % 10
            baldes[digito] += 1
        for i in range(1, 10):
            baldes[i] += baldes[i - 1]
        resultado = [0] * len(lista)
        i = len(lista) - 1
        while i >= 0:
            digito = (lista[i] // posicao) % 10
            baldes[digito] -= 1
            resultado[baldes[digito]] = lista[i]
            i -= 1
        lista = resultado
        posicao *= 10
    return lista
