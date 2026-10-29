from algoritmos import (
    insercao,
    intercala_sort,
    rapida,
    hibrida,
    contagem,
    base
)

def escolher(v):
    n = len(v)
    if n <= 32:
        return "insercao"

    menor = v[0]
    maior = v[0]
    fora_de_ordem = 0
    for i in range(1, n):
        if v[i] < menor:
            menor = v[i]
        if v[i] > maior:
            maior = v[i]
        if v[i] < v[i - 1]:
            fora_de_ordem += 1

    faixa = maior - menor + 1
    proporcao = fora_de_ordem / (n - 1)

    if faixa <= 100000 and faixa <= 4 * n:
        return "contagem"
    if n >= 1000 and menor >= 0:
        return "base"
    if proporcao <= 0.05:
        return "insercao"
    if n >= 100:
        return "hibrida"
    return "rapida"

def ordenar(v):
    metodo = escolher(v)
    if metodo == "insercao":
        resultado = insercao(v)
    elif metodo == "intercala":
        resultado = intercala_sort(v)
    elif metodo == "rapida":
        resultado = rapida(v)
    elif metodo == "hibrida":
        resultado = hibrida(v)
    elif metodo == "contagem":
        resultado = contagem(v)
    else:
        resultado = base(v)
    return resultado
