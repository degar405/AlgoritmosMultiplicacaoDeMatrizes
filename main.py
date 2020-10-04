import multiplicaoDeMatrizes as m
import helpers as h

def main():
    n = 10
    matriz_um = h.cria_matriz(n)
    matriz_dois = h.cria_matriz(n)
    matriz_resultado_simples = m.multiplicacao_simples(matriz_um, matriz_dois)
    
    