import locale
import random
import time

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("Jogo do Caça-Níquel")
print("-"*30)

nome = input("Nome do Apostador: ")
valor = int(input("Valor da aposta R$: "))
valor3 = valor * 3
valor3 = locale.currency(valor3, grouping=True, symbol=None)

input("Pressione Enter para Girar a Roleta... ")

figuras = "🤡🥵🥶"
jogo = ""

print("Rolando..:", end="")

for _ in range(3):
    num = random.randint(0, 2)
    print(figuras[num], end="", flush=True)
    jogo = jogo + figuras[num]
    time.sleep(1)

if jogo[0] == jogo[1] and jogo[0] == jogo[2]:
    print(f"\nParabéns {nome}! Você ganhou R${valor3}")
elif jogo[0] == jogo[1] or jogo[0] == jogo[2] or jogo[1] == jogo[2]:
    print(f"\nQuase {nome}, continue apostando! Na proxima vem!")
else:
    print(f"\nBah {nome}, tu é muito ruim jogando, gasta mais vai")

