import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

pessoas = int(input("Nº de pessoas: "))
peixes = int(input("Nº de peixes: "))

total = pessoas * 20

if peixes > pessoas:
    extras = peixes - pessoas
    total = total + (extras * 12)
    total = locale.currency(total, grouping=True, symbol=None)

print(f"Pagar R${total}")