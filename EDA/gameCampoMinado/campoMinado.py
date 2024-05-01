import random
import os

campo = "🟥"
campoVazio = "🟩"
bomba = "💣"
campoMinado = []
campoJogo = [] 
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
    print("   1   2   3   4   5   6   7   8   9   10")
    
    for i in range(10):
        print(f"{i+1:2d}", end="")
        
        for j in range(10):
            print(f"|{campoJogo[i][j]:2s}", end="")
            
        print("|")

def verificaVizinhos(campoMinado, x, y):
    z = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if campoMinado[x + (1-i)][y + (1-j)] == bomba:
                i += 1
    return int(z)
    
def fazJogada(campoJogo, campoMinado):
    jogadas = 0

    while True:
        mostraCampo(campoJogo)
        while True:
            try:
                jogadaLinha = int(input("Informe a linha: "))
            except ValueError:
                print("Linha inválida! Digite um valor entre 1 e 10.")
                continue

            if jogadaLinha < 1 or jogadaLinha > 10:
                print("Linha inválida! Digite um valor entre 1 e 10.")
            else:
                break
        while True:
            try:
                jogadaColuna = int(input("Informe a coluna: "))
            except ValueError:
                print("Coluna inválida! Digite um valor entre 1 e 10.")
                continue

            if jogadaColuna < 1 or jogadaColuna > 10:
                print("Coluna inválida! Digite um valor entre 1 e 10.")
            else:
                break
     
        x = int(jogadaLinha) - 1
        y = int(jogadaColuna) - 1
        jogadas += 1

        if campoMinado[x][y] == bomba:
            campoJogo[x][y] = bomba
            mostraCampo(campoMinado)
            print("Você perdeu!")
            gravaJogada(nome, jogadas)
            break
        else:
            campoJogo[x][y] = str(vizinhos[verificaVizinhos(campoMinado, x, y)])
            if campoJogo == campoMinado:
                mostraCampo(campoJogo)
                print("Você ganhou!")
                break



while True:
    print('|--------------------------------------------|')
    print('| 1. Jogar                                   |')
    print('| 2. Ver Ranking                             |')
    print('| 3. Sair                                    |')
    print('|--------------------------------------------|')    
    opcao = input("Escolha..: ")
    
    if opcao == '1':
        nome = input("Informe o seu nome: ")
        campoJogo, campoMinado = criaCampo(campoJogo, campoMinado)
        campoMinado = preencheCampo(campoMinado)
        fazJogada(campoJogo, campoMinado)
    if opcao == '2':
        jogadas = carregaJogadas()
        jogadas.sort(key=lambda x: x[-1])
        print("Ranking")
        print("========")
        for i, j in enumerate(jogadas):
            print(f"{i+1}º - {j[0]} - {j[1]} jogadas")
        input("Pressione ENTER para continuar...")

    if opcao == '3':
        break
    
