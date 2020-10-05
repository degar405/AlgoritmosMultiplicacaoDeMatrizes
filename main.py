import multiplicacaoDeMatrizes as m
import helpers as h
import matplotlib.pyplot as plt
import numpy as np
import statistics as s

def realiza_experimento(n_max):
    n = 1
    
    x = []
    y_simples = []
    y_strassen = []
    while (n <= n_max):
        matriz_um = h.cria_matriz(n)
        matriz_dois = h.cria_matriz(n)

        (resultado_simples, tempo_simples) = m.multiplicacao_algoritmo_simples(matriz_um, matriz_dois)
        (resultado_strassen, tempo_strassen) = m.multiplicacao_algoritmo_strassen(matriz_um, matriz_dois)

        x.append(n)
        y_simples.append(tempo_simples)
        y_strassen.append(tempo_strassen)

        n *= 2

    print(str(x))
    print(str(y_simples))
    print(str(y_strassen))
    plt.title('Gráfico de tempo de execução dos algoritmos de multiplicação de matrizes quadradas')
    plt.xlabel("n (número de linhas e de colunas das matrizes)")
    plt.ylabel("segundos")
    plt.plot(x, y_simples)
    plt.plot(x, y_strassen)
    plt.legend(('Algoritmo Simples','Algoritmo de Strassen'),loc='upper left')
    plt.show()

def gera_grafico_media():
    x = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    tempos_simples = np.matrix([[0.0, 0.0, 0.0, 0.0, 0.001999378204345703, 0.020987510681152344, 0.11695480346679688, 0.9404604434967041, 8.523097038269043, 65.22247409820557],
                                [0.0, 0.0, 0.0, 0.0, 0.003002166748046875, 0.021988868713378906, 0.13118696212768555, 1.0103869438171387, 7.893006801605225, 75.60870599746704],
                                [0.0, 0.0, 0.0, 0.0, 0.0029976367950439453, 0.01698923110961914, 0.11995244026184082, 1.2993988990783691, 8.918286800384521, 64.40157437324524],
                                [0.0, 0.0, 0.0, 0.0, 0.0019974708557128906, 0.015968799591064453, 0.11995267868041992, 0.9314665794372559, 9.143866062164307, 83.93840074539185],
                                [0.0, 0.0, 0.0, 0.0, 0.003020763397216797, 0.019011259078979492, 0.12093091011047363, 0.9368095397949219, 8.923126220703125, 74.60563397407532],
                                [0.0, 0.0, 0.0, 0.0, 0.0029816627502441406, 0.022984743118286133, 0.12892436981201172, 1.0133988857269287, 8.524497270584106, 85.13704705238342],
                                [0.0, 0.0, 0.0, 0.0, 0.0029795169830322266, 0.02100682258605957, 0.12590742111206055, 1.016418218612671, 7.951632022857666, 66.53351521492004],
                                [0.0, 0.0, 0.0, 0.0, 0.019989728927612305, 0.02398395538330078, 0.12494874000549316, 1.0454013347625732, 8.070411443710327, 69.555246591568],
                                [0.0, 0.0, 0.0009965896606445312, 0.0, 0.0020003318786621094, 0.022009849548339844, 0.13692140579223633, 1.182344675064087, 9.142295598983765, 75.11450672149658],
                                [0.0, 0.0, 0.0, 0.0010006427764892578, 0.0019986629486083984, 0.0230104923248291, 0.13292455673217773, 1.0513968467712402, 8.200520753860474, 70.02826428413391]])

    tempos_strassen = np.matrix([[0.0, 0.0, 0.0, 0.0, 0.0039975643157958984, 0.021008968353271484, 0.1259293556213379, 1.639566421508789, 7.531590223312378, 49.63233804702759],
                                 [0.0, 0.0, 0.0, 0.0009965896606445312, 0.0039942264556884766, 0.024236440658569336, 0.1519324779510498, 1.0214979648590088, 7.408304452896118, 55.156492710113525],
                                 [0.0, 0.0, 0.0009980201721191406, 0.0, 0.0039975643157958984, 0.020010948181152344, 0.14194345474243164, 1.108823299407959, 7.912362098693848, 51.54021620750427],
                                 [0.0, 0.0, 0.0, 0.0, 0.003998517990112305, 0.02498769760131836, 0.13989949226379395, 1.025331735610962, 8.308417797088623, 57.72379732131958],
                                 [0.0, 0.0, 0.0, 0.0, 0.0029747486114501953, 0.018969058990478516, 0.13092494010925293, 0.9986171722412109, 8.85186505317688, 76.77455973625183],
                                 [0.0, 0.0, 0.0, 0.0, 0.004000186920166016, 0.02298736572265625, 0.1579122543334961, 1.3632190227508545, 7.907138109207153, 68.0630373954773],
                                 [0.0, 0.0, 0.0, 0.0, 0.0029969215393066406, 0.019967079162597656, 0.14191937446594238, 1.028430461883545, 7.54304313659668, 57.4434769153595],
                                 [0.0, 0.0, 0.0, 0.0, 0.011992692947387695, 0.019988536834716797, 0.14589476585388184, 1.056394100189209, 7.953838348388672, 57.66152310371399],
                                 [0.0, 0.0, 0.0, 0.0, 0.001997232437133789, 0.023963212966918945, 0.2768223285675049, 1.4121687412261963, 8.209787368774414, 61.33368635177612],
                                 [0.0, 0.0, 0.0, 0.0, 0.002996683120727539, 0.02696061134338379, 0.14491629600524902, 1.097374439239502, 7.819569826126099, 58.162357330322266]])

    tempos_simples = np.transpose(tempos_simples)
    tempos_strassen = np.transpose(tempos_strassen)

    medias_simples = []
    desvios_padroes_simples = []
    medias_strassen = []
    desvios_padroes_strassen = []
    for i in range(0, len(x)):
        medias_simples.append(s.mean(tempos_simples[i].tolist()[0]))
        medias_strassen.append(s.mean(tempos_strassen[i].tolist()[0]))
        desvios_padroes_simples.append(s.stdev(tempos_simples[i].tolist()[0]))
        desvios_padroes_strassen.append(s.stdev(tempos_strassen[i].tolist()[0]))
    
    print(medias_simples)
    print(medias_strassen)
    print(desvios_padroes_simples)
    print(desvios_padroes_strassen)

    plt.title('Gráfico de média dos tempos de execução dos algoritmos de multiplicação de matrizes quadradas')
    plt.xlabel("n (número de linhas e de colunas das matrizes)")
    plt.ylabel("segundos")
    plt.plot(x, medias_simples)
    plt.plot(x, medias_strassen)
    plt.legend(('Algoritmo Simples','Algoritmo de Strassen'),loc='upper left')
    plt.show()