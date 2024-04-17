import random
import time
import os

campo = "🟥"
campoVazio = "⬜"
bomba = "💣"
campoMinado = []
campoJogo = []
vizinhos = ["1", "2", "3", "4", "5", "6", "7", "8"]

def criaCampo(campoJogo, campoMinado):
    for i in range(10):
        campoMinado.append([])
        campoJogo.append([])
        
        for _ in range(10):
            campoMinado[i].append(campo)
            campoJogo[i].append(campo)
    return campoJogo, campoMinado

def preencheCampo(campoMinado):
    for _ in range(20):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        campoMinado[x][y] = bomba
    return campoMinado

def mostraCampo(campoJogo):
    os.system("cls")
    print("Campo Minado")
    print("============")
    print("    1  2  3  4  5  6  7  8  9 10")
    
    for i in range(10):
        print(f"{i+1} ", end="")
        
        for j in range(10):
            print(f"| {campoJogo[i][j]} ", end="")
            
        print("|")

def verificaVizinhos(campoMinado, x, y):
    if campoMinado[x][y] == bomba:
        return bomba
    else:
        vizinhos = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= 0 and x + i < 10 and y + j >= 0 and y + j < 10:
                    if campoMinado[x + i][y + j] == bomba:
                        vizinhos += 1
        return str(vizinhos)
    
def fazJogada(campoJogo, campoMinado):
    while True:
        mostraCampo(campoJogo)
        jogada = input("Informe a jogada(2 números: linha e coluna): ")
        if len(jogada) != 2:
            print("Informe 2 números!")
            time.sleep(2)
            continue
        x = int(jogada[0])-1
        y = int(jogada[1])-1
        if campoMinado[x][y] == bomba:
            campoJogo[x][y] = bomba
            mostraCampo(campoJogo)
            print("Você perdeu!")
            break
        else:
            campoJogo[x][y] = verificaVizinhos(campoMinado, x, y)
            if campoJogo[x][y] == campoVazio:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if x + i >= 0 and x + i < 10 and y + j >= 0 and y + j < 10:
                            if campoJogo[x + i][y + j] == campoVazio:
                                campoJogo[x + i][y + j] = verificaVizinhos(campoMinado, x + i, y + j)
            if campoJogo == campoMinado:
                mostraCampo(campoJogo)
                print("Você ganhou!")
                break

campoJogo, campoMinado = criaCampo(campoJogo, campoMinado)
campoMinado = preencheCampo(campoMinado)
fazJogada(campoJogo, campoMinado)
