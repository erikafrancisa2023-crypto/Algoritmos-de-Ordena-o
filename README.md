# Relatório — Algoritmos de Ordenação

# Tabela dos quatro cenários contra os seis métodos
Os tempos estão em segundos e correspondem às medições realizadas no programa.
| Cenário | Inserção | Intercalação | Quicksort | Híbrida | Contagem | Base |

|---|---:|---:|---:|---:|---:|---:|
| Chaves grandes | 5,381858 | 0,031036 | 0,020395 | **0,016492** | N/E | 0,028316 |
| Faixa estreita | 5,053042 | 0,031997 | 0,005324 | 0,006028 | **0,001767** | 0,007771 |
| Quase ordenada | 0,060398 | 0,025869 | 0,018223 | 0,012230 | **0,002556** | 0,016039 |
| Lista minúscula | **0,000004** | 0,000009 | 0,000008 | **0,000004** | 0,000014 | 0,000012 |

## Vencedores de cada cenário

 **Chaves grandes:** Quicksort Híbrida, com 0,016492 segundo. Foi o algoritmo mais rápido nesse cenário.
 **Faixa estreita:** Contagem, com 0,001767 segundo. Esse algoritmo foi eficiente porque os valores estavam concentrados em uma faixa pequena.
 **Quase ordenada:** Contagem, com 0,002556 segundo. A faixa pequena de valores favoreceu seu desempenho.
 **Lista minúscula:** Inserção e Quicksort Híbrida empataram no tempo exibido, com 0,000004 segundo.

## Regras da função `escolher`

A função `escolher` analisa as características da lista para selecionar um algoritmo.
As regras utilizadas são:
1. Listas com até 32 elementos: **Inserção**.
2. Faixa de valores de até 100.000 e não superior a quatro vezes o tamanho da lista: **Contagem**.
3. Listas com pelo menos 1.000 elementos e valores não negativos: **Base**.
4. Listas com até 5% de descidas entre elementos vizinhos: **Inserção**.
5. Listas com pelo menos 100 elementos: **Quicksort Híbrida**.
6. Nos demais casos: **Quicksort**.

## Quanto custa rodar o escolher — ele compensa?

O custo da escolha foi medido separadamente da ordenação.
**Cenário**  **Custo da escolha** 
- **Chaves grandes:**  0,001383 
- **Faixa estreita:** 0,001524 
- **Quase ordenada:** 0,001172 
- **Lista minúscula:** 0,000002 

A função percorre a lista para identificar o menor e o maior valor e contar as descidas entre elementos vizinhos. Essa análise acrescenta um custo antes da ordenação.
O custo é pequeno nas listas grandes, mas pode representar uma parte significativa do tempo em listas minúsculas. Portanto, a escolha inteligente pode compensar quando identifica um algoritmo adequado, mas não garante um ganho em todos os casos.

## Um cenário em que ele erra a decisão

No cenário de chaves grandes aleatórias, a função `escolher` selecionou o algoritmo Base. Entretanto, a Quicksort Híbrida apresentou um tempo menor.
| Medição | Tempo (segundos) |
|---|---:|
| Algoritmo Base | 0,028316 |
| Quicksort Híbrida | **0,016492** |
| Ordenação inteligente | 0,030954 |

Nesse cenário, o seletor não escolheu o algoritmo mais rápido. A ordenação inteligente levou 0,030954 segundo, enquanto a Quicksort Híbrida levou 0,016492 segundo.
Esse resultado demonstra que as regras do seletor podem ser melhoradas para considerar melhor as características dos dados.


