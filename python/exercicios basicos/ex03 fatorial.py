numero = int(input("digite um numero para ver seu fatorial: "))
fatorial = 1
contador = 1
while (contador <= numero):
    fatorial *= contador
    contador += 1
print(f"o fatorial de {numero} é {fatorial}")