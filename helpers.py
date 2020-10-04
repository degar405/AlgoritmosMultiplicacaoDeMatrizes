from random import randint

def cria_matriz(n):
    matriz = []
    for i in range(0,n):
        linha = []
        for j in range(0,n):
            num = randint(0,100)
            linha.append(num)
        matriz.append(linha)
    return matriz


def printa_matriz(matriz):
    for linha in matriz:
        print(linha)


def cria_matriz_zerada(n):
    linha = []
    matriz = []
    for i in range(0,n):
        linha.append(0)
    for i in range(0,n):
        matriz.append(linha.copy())
    return matriz

def soma_matrizes(matriz_um, matriz_dois, n):
    matriz_resultado = cria_matriz_zerada(n)
    for i in range(0, n):
        for j in range(0, n):
            matriz_resultado[i][j] = matriz_um[i][j] + matriz_dois[i][j]
    return matriz_resultado

def subtrai_matrizes(matriz_um, matriz_dois, n):
    matriz_resultado = cria_matriz_zerada(n)
    for i in range(0, n):
        for j in range(0, n):
            matriz_resultado[i][j] = matriz_um[i][j] - matriz_dois[i][j]
    return matriz_resultado

def obtem_submatrizes(matriz_um, matriz_dois, n):
    x = int(n/2)
    
    A = []
    B = []
    C = []
    D = []
    E = []
    F = []
    G = []
    H = []
    for i in range(0, x):
        A.append(matriz_um[i][0:x])
        B.append(matriz_um[i][x:n])
        E.append(matriz_dois[i][0:x])
        F.append(matriz_dois[i][x:n])
        C.append(matriz_um[i + x][0:x])
        D.append(matriz_um[i + x][x:n])
        G.append(matriz_dois[i + x][0:x])
        H.append(matriz_dois[i + x][x:n])
    
    return (A, B, C, D, E, F, G, H)