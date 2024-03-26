import random
import time

naipes = "♠ ♡ ♢ ♣".split()
extras = 'J Q K A'.split()
baralho = []
jogador = []
oponent = []
mao = []
mao_oponent = []
total = 0
totalOponent = 0


def monta_baralho():
    for i in range(2,11):
        for n in naipes:
            baralho.append(str(i) + n)
    for e in extras:
        for n in naipes:
            baralho.append(e + n)

def valor_carta(carta):
    if carta[0] in 'JQK':
        return 10
    if carta[0] == 'A':
        return 11
    return int(carta[:-1])

def compra_carta(jogador, mao):
    carta = baralho.pop()
    jogador.append(carta)
    mao.append(valor_carta(carta))
    time.sleep(1)
    return

monta_baralho()
random.shuffle(baralho)

contador  = 0
while True:
    contador += 1
    
    compra_carta(jogador, mao)
    compra_carta(oponent, mao_oponent)
   
    print(f"Carta {contador} do jogador: {jogador[-1]}")
    time.sleep(1)
    print(f"Carta {contador} do oponente: {oponent[-1]}")
    
    total = sum(mao)
    totalOponent = sum(mao_oponent)
    
    print(f"Total do jogador: {total}")
    print(f"Total do oponente: {totalOponent}")
    
    
    if contador == 2:
        break
    

while True:
    if total < 21:
        escolha = input("Deseja comprar mais uma carta? (s/n)").upper()
        if escolha == 'S':
            compra_carta(jogador, mao)
            print(f"Carta {contador} do jogador: {jogador[-1]}")
            total = sum(mao)
            print(f"Total do jogador: {total}")
        else:
            break
    else:
        break
    
while True:
    if totalOponent < 17:
        compra_carta(oponent, mao_oponent)
        print(f"Carta {contador} do oponente: {oponent[-1]}")
        totalOponent = sum(mao_oponent)
        print(f"Total do oponente: {totalOponent}")
    else:
        break
    
    
while True:
    if total > 21:
        print("O jogador estourou!")
        break
    if totalOponent > 21:
        print("O oponente estourou!")
        break
    if total == 21:
        print("O jogador fez 21!")
        break
    if totalOponent == 21:
        print("O oponente fez 21!")
        break
    if total > totalOponent:
        print("O jogador venceu!")
        break
    if total < totalOponent:
        print("O oponente venceu!")
        break
    if total == totalOponent:
        print("Empate!")
        break     
    