import random
import time

naipes = "♠ ♡ ♢ ♣".split()
extras = 'J Q K A'.split()
baralho = []

def monta_baralho():
    for i in range(2,11):
        for n in naipes:
            baralho.append(str(i) + n)
    for e in extras:
        for n in naipes:
            baralho.append(e + n)

monta_baralho()

def valor_carta(carta):
    if carta[0] in 'JQK':
        return 10
    if carta[0] == 'A':
        return 11
    return int(carta[:-1])


random.shuffle(baralho)

jogador = []
mao = []
contador = 0

while True:
    carta = baralho.pop()
    jogador.append(carta)
    contador += 1
   
    print(f"Carta {contador}: {carta}")
    
    mao.append(valor_carta(carta))
    total = sum(mao)
    print(f"Total: {total}")
    
    time.sleep(1)
    if contador >= 2:
        
        if total == 21:
            print("Blackjack!")
            break
        if total >= 22:
            print("Estourou!")
            break
        
        continua = input("Deseja continuar? (S/N) ").upper()
        
        if continua == 'N':
            break
        if continua == 'S':
            pass