import helpers as h
import time

def multiplicacao_algoritmo_simples(matriz_um, matriz_dois):
    tempoInicio = time.time()

    matriz_resultado = multiplicacao_simples(matriz_um, matriz_dois)

    tempoFinal = time.time()
    return (matriz_resultado, tempoFinal - tempoInicio)

def multiplicacao_simples(matriz_um, matriz_dois):
    #Qtd Linhas da Primeira
    n = len(matriz_um)

    #Qtd Colunas da Primeira
    m = len(matriz_um[0])

    #Qtd Colunas da Segunda
    p = len(matriz_dois[0])

    matriz_resultado = h.cria_matriz_zerada(m)
    
    for i in range(0,n):
        for j in range(0,p):
            for k in range(0,m):
                matriz_resultado[i][j] = matriz_resultado[i][j] + (matriz_um[i][k] * matriz_dois[k][j])
    return matriz_resultado


def multiplicacao_algoritmo_strassen(matriz_um, matriz_dois):
    tempoInicio = time.time()

    matriz_resultado = multiplicacao_strassen(matriz_um, matriz_dois)

    tempoFinal = time.time()
    return (matriz_resultado, tempoFinal - tempoInicio)

def multiplicacao_strassen(matriz_um, matriz_dois):
    n = len(matriz_um)

    if(n <= 8):
        return multiplicacao_simples(matriz_um, matriz_dois)

    x = int(n/2)
    (A, B, C, D, E, F, G, H) = h.obtem_submatrizes(matriz_um, matriz_dois, n)

    P1 = multiplicacao_strassen(A, h.subtrai_matrizes(F, H, x))
    P2 = multiplicacao_strassen(h.soma_matrizes(A, B, x), H)
    P3 = multiplicacao_strassen(h.soma_matrizes(C, D, x), E)
    P4 = multiplicacao_strassen(D, h.subtrai_matrizes(G, E, x))
    P5 = multiplicacao_strassen(h.soma_matrizes(A, D, x), h.soma_matrizes(E, H, x))
    P6 = multiplicacao_strassen(h.subtrai_matrizes(B, D, x), h.soma_matrizes(G, H, x))
    P7 = multiplicacao_strassen(h.subtrai_matrizes(A, C, x), h.soma_matrizes(E, F, x))

    M1 = h.soma_matrizes(h.subtrai_matrizes(h.soma_matrizes(P5, P4, x), P2, x), P6, x)
    M2 = h.soma_matrizes(P1, P2, x)
    M3 = h.soma_matrizes(P3, P4, x)
    M4 = h.subtrai_matrizes(h.subtrai_matrizes(h.soma_matrizes(P1, P5, x), P3, x), P7, x)

    matriz_resultado = h.cria_matriz_zerada(n)

    for i in range(0, x):
        matriz_resultado[i] = M1[i] + M2[i]
        matriz_resultado[i + x] = M3[i] + M4[i]

    return matriz_resultado