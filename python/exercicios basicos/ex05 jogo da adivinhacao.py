import random
escolha = int(input("tente adivinhar o numero de 1 a 10: "))
escolhaComputador = random.randint(1, 10)
print(f"o computador escolheu {escolhaComputador}")
if escolhaComputador == escolha:
    print("parabens você acertou!")
else:
    print("infelizmente você errou")
