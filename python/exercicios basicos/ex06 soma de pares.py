escolha = int(input("digite um numero e ao final veja a soma dos pares. [0] para cancelar "))
soma = 0
while escolha != 0:
    if escolha % 2 ==0:
        soma += escolha
    escolha = int(input("digite um numero e ao final veja a soma dos pares. [0] para cancelar"))
print(f"a soma dos numeros é {soma}")