import random
import os

campo = "🟥"
campoVazio = "🟩"
bomba = "💣"
vizinhos = ["0️⃣  ","1️⃣  ","2️⃣  ","3️⃣  ","4️⃣  ","5️⃣  ","6️⃣  ","7️⃣  ","8️⃣  "]

def gravaJogada(nome, jogadas):
    with open("jogadas.txt", 'a') as arq:
        arq.write(f"{nome};{jogadas}\n")

def carregaJogadas():
    jogadas = []
    try:
        with open("jogadas.txt") as arq:
            for linha in arq:
                nome, jogada = linha.strip().split(";")
                jogadas.append((nome, int(jogada)))
    except FileNotFoundError:
        pass
    return jogadas

def criaCampo():
    campoMinado = []
    campoJogo = []
    for i in range(tam):
        campoMinado.append([campo] * tam)
        campoJogo.append([campo] * tam)
    return campoJogo, campoMinado

def preencheCampo(campoMinado):
    bombasColocadas = 0
    while bombasColocadas < bomb:
        x = random.randint(0,tam-1)
        y = random.randint(0,tam-1)
        if campoMinado[x][y] != bomba:
            campoMinado[x][y] = bomba
            bombasColocadas += 1
    return campoMinado

def mostraCampo(campoJogo):
    os.system("cls" if os.name == "nt" else "clear")
    print("Campo Minado")
    print("============")
    print("   1   2   3   4   5   6   7   8   9   tam")
    for i in range(tam):
        print(f"{i+1:2d}", end="")
        for j in range(tam):
            print(f"|{campoJogo[i][j]:2s}", end="")            
        print("|")

def verificaVizinhos(campoMinado, x, y):
    z = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            xi, yj = x + i, y + j
            if 0 <= xi < tam and 0 <= yj < tam and campoMinado[xi][yj] == bomba:
                z += 1
    return z   
    
def procuraZeros(campoJogo, campoMinado, x, y):
    fila = [(x, y)]
    visitados = set((x, y))

    while fila:
        fx, fy = fila.pop(0)
        numVizinhos = verificaVizinhos(campoMinado, fx, fy)
        campoJogo[fx][fy] = vizinhos[numVizinhos]

        if numVizinhos == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    fxi, fyj = fx + i, fy + j
                    if 0 <= fxi < tam and 0 <= fyj < tam and (fxi, fyj) not in visitados:
                        fila.append((fxi, fyj))
                        visitados.add((fxi, fyj))

def fazJogada(campoJogo, campoMinado, nome):
    jogadas = 0
    while True:
        mostraCampo(campoJogo)
        while True:
            try:
                jogadaLinha = int(input("Informe a linha: "))
                if jogadaLinha < 1 or jogadaLinha > tam:
                    raise ValueError
                break
            except ValueError:
                print("Linha inválida! Digite um valor entre 1 e tam.")
        while True:
            try:
                jogadaColuna = int(input("Informe a coluna: "))
                if jogadaColuna < 1 or jogadaColuna > tam:
                    raise ValueError
                break
            except ValueError:
                print("Coluna inválida! Digite um valor entre 1 e tam.")

        x = jogadaLinha - 1
        y = jogadaColuna - 1
        jogadas += 1

        if campoMinado[x][y] == bomba:
            campoJogo[x][y] = bomba
            mostraCampo(campoMinado)
            print("Você perdeu!")
            gravaJogada(nome, jogadas)
            break
        else:
            numVizinhos = verificaVizinhos(campoMinado, x, y)
            if numVizinhos == 0:
                procuraZeros(campoJogo, campoMinado, x, y)
            else:
                campoJogo[x][y] = vizinhos[numVizinhos]
            
            if all(campoJogo[i][j] != campo for i in range(tam) for j in range(tam) if campoMinado[i][j] != bomba):
                mostraCampo(campoJogo)
                print("Você ganhou!")
                gravaJogada(nome, jogadas)
                break

while True:
    print('|--------------------------------------------|')
    print('| 1. Jogar                                   |')
    print('| 2. Ver Ranking                             |')
    print('| 3. Sair                                    |')
    print('|--------------------------------------------|')    
    opcao = input("Escolha..: ")
    
    if opcao == '1':
        print('|----------Selecione a dificuldade-----------|')
        print('| 1. Fácil (9x9 - tam Bombas)                 |')
        print('| 2. Médio (16x16 - 40 Bombas)               |')
        print('| 3. Difícil (30x16 - 99 Bombas)             |')
        print('|--------------------------------------------|')
        dificuldade = input("Escolha..: ")
        
        if dificuldade == '1':
            tam = 9
            bomb = tam
        
        if dificuldade == '2':
            tam = 16
            bomb = 40
        
        if dificuldade == '3':
            tam = 30
            bomb = 99

        nome = input("Informe o seu nome: ")
        campoJogo, campoMinado = criaCampo()
        campoMinado = preencheCampo(campoMinado)
        fazJogada(campoJogo, campoMinado, nome)
    if opcao == '2':
        jogadas = carregaJogadas()
        jogadas.sort(key=lambda x: x[-1], reverse=True)
        print("Ranking")
        print("========")
        for i, j in enumerate(jogadas):
            print(f"{i+1}º - {j[0]} - {j[1]} jogadas")
        input("Pressione ENTER para continuar...")
    if opcao == '3':
        break
    
