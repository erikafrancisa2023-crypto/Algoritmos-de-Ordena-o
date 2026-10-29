
from algoritmos import (
    insercao,
    intercala_sort,
    rapida,
    hibrida,
    contagem,
    base
)
from escolher import escolher, ordenar
metodos = [
    ("Inserção", insercao),
    ("Intercalação", intercala_sort),
    ("Rápida", rapida),
    ("Híbrida", hibrida),
    ("Contagem", contagem),
    ("Base", base)
]

testes = [
    [],
    [5],
    [7, 7, 7, 7],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-5, 3, -1, 0, 2, -10]
]

for lista in testes:
    esperado = sorted(lista)
    for nome, metodo in metodos:
        resultado = metodo(lista)
        if resultado != esperado:
            print("ERRO:", nome, lista, resultado)
        else:
            print("OK:", nome, lista)
    resultado_inteligente = ordenar(lista)
    if resultado_inteligente == esperado:
        print("OK: Seletor inteligente", escolher(lista))
    else:
        print("ERRO: Seletor inteligente")
    print("--------------------------")
