import random
import time
import statistics
import csv

from algoritmos import (
    insercao,
    intercala_sort,
    rapida,
    hibrida,
    contagem,
    base)
from escolher import escolher, ordenar
random.seed(42)

metodos = [
    ("insercao", insercao),
    ("intercalacao", intercala_sort),
    ("rapida", rapida),
    ("hibrida", hibrida),
    ("contagem", contagem),
    ("base", base)]

def criar_cenarios():
    aleatoria = []
    for i in range(20000):
        aleatoria.append(random.randint(0, 1000000000))
    faixa_estreita = []
    for i in range(20000):
        faixa_estreita.append(random.randint(-50, 50))
    quase_ordenada = list(range(20000))
    for i in range(100):
        a = random.randint(0, 19999)
        b = random.randint(0, 19999)
        quase_ordenada[a], quase_ordenada[b] = (
            quase_ordenada[b],
            quase_ordenada[a])
    pequena = []
    for i in range(15):
        pequena.append(random.randint(-100, 100))
    return [
        ("aleatoria_chaves_grandes", aleatoria),
        ("faixa_estreita", faixa_estreita),
        ("quase_ordenada", quase_ordenada),
        ("minuscula", pequena)]

def medir_tempo(funcao, lista):
    tempos = []
    for repeticao in range(4):
        inicio = time.perf_counter()
        resultado = funcao(lista)
        fim = time.perf_counter()
        if resultado != sorted(lista):
            raise ValueError("O método produziu resultado incorreto.")
        if repeticao > 0:
            tempos.append(fim - inicio)
    return statistics.median(tempos)

def medir_escolha(funcao, lista):
    tempos = []
    metodo_escolhido = ""
    for repeticao in range(4):
        inicio = time.perf_counter()
        metodo_escolhido = funcao(lista)
        fim = time.perf_counter()
        if repeticao > 0:
            tempos.append(fim - inicio)
    tempo_mediano = statistics.median(tempos)
    return tempo_mediano, metodo_escolhido

resultados = []

for nome_cenario, lista in criar_cenarios():
    print("\nCenário:", nome_cenario)
    faixa = max(lista) - min(lista) + 1 if lista else 0
    for nome_metodo, metodo in metodos:
        if nome_metodo == "contagem" and faixa > 100000:
            print(nome_metodo,"não executado: faixa insegura")
            resultados.append([
                nome_cenario,
                nome_metodo,
                "N/A" ])
            
            continue
        tempo = medir_tempo(metodo, lista)
        resultados.append([
            nome_cenario,
            nome_metodo,
            tempo ])        
        print(nome_metodo,round(tempo, 6), "segundos")
    tempo_inteligente = medir_tempo(ordenar, lista)
    resultados.append([
        nome_cenario,
        "inteligente",
        tempo_inteligente])
    tempo_escolha, metodo_escolhido = medir_escolha( escolher,lista)
    print("Método escolhido:", metodo_escolhido)
    print("Inteligente:",round(tempo_inteligente, 6),"segundos")
    print("Custo da escolha:",round(tempo_escolha, 6),"segundos")

arquivo = open(
    "tempos.csv",
    "w",
    newline="",
    encoding="utf-8")

escritor = csv.writer(arquivo)
escritor.writerow([
    "cenario",
    "metodo",
    "tempo_segundos"])

escritor.writerows(resultados)
arquivo.close()
print("\nResultados salvos em tempos.csv")
