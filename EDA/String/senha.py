print("Para criar uma senha é necessário que ela tenha pelo menos, um número e uma letra maiscula, também deve conter entre 8 a 12 caracteres")
senha = input("Informe a senha: ")

num = False
Mais = False
tam = False

if len(senha) > 7 and len(senha) < 13:
    tam = True

for letra in senha:
    if letra.isdigit() == True:
        num = True
    if letra.isupper() == True:
        Mais = True

if num == True and Mais == True and tam == True:
    print("Válido")
else:
    print("Invalido") 