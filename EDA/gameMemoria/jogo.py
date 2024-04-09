import random
import time
import os

jogo = []
apostas = []
temp = "🤡🤡💀💀👺👺🥶🥶🤯🤯😬😬🙄🙄🤠🤠"
figuras = list(temp)

def preenchendoJogo():
    for i in range(4):
        jogo.append([])
        apostas.append([])
        
        for _ in range(4):
            num = random.randint(0, len(figuras) - 1)
            jogo[i].append(figuras[num])
            apostas[i].append("🈹")
            figuras.pop(num)
            
def mostra_tabuleiro():
    os.system("cls")
    print("Jogo da Memória")
    print("==============")
    print("     1    2    3    4")
    
    for i in range(4):
        print(f"{i} ", end="")
        
        for j in range(4):
            print(f"| {jogo[i][j]} ", end="")
            
        print("|")
    
    print("Memorize a posição dos bichos...")
    time.sleep(2)
    
def mostra_apostas():
    os.system("cls")
    print("Jogo da Memória")
    print("==============")
    print("     1    2    3    4")
    
    for i in range(4):
        print(f"{i+1} ", end="")
        
        for j in range(4):
            print(f"| {apostas[i][j]} ", end="")
            
        print("|")
        
def faz_aposta(num):
    while True:
        mostra_apostas()
        aposta = input(f"{num}* cordenada(2 numeros: linha e coluna): ")
        if len(aposta) != 2:
            print("Informe 2 números!")
            time.sleep(2)
            continue
        x = int(aposta[0])-1
        y = int(aposta[1])-1
        try:
            if apostas[x][y] != "🈹":
                print("Posição já escolhida!")
                time.sleep(2)
                continue
            
            if apostas[x][y] == "🈹":
                apostas[x][y] = jogo[x][y]
                break
            
            
        except IndexError:
            print("Informe números válidos!")
            time.sleep(2)
            continue
    return (x, y)

def verifica_ganhador():
    for i in range(4):
        for j in range(4):
            if apostas[i][j] == "🈹":
                return False
    return True

preenchendoJogo()
mostra_tabuleiro()

while True:

    if verifica_ganhador():
        print("Parabéns! Você ganhou!")
        break
    
    x1, y1 = faz_aposta(1)
    x2, y2 = faz_aposta(2)
    mostra_apostas()
    
    
    
    if apostas[x1][y1] == apostas[x2][y2]:
        print("Acertou!")
        time.sleep(2)
    else:
        print("Você errou!")
        apostas[x1][y1] = "🈹"
        apostas[x2][y2] = "🈹"
        sair = input("Deseja sair? (s/n): ").upper()
        if sair == "S":
            break