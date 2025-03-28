frase = input("digite uma frase ou palavra e verifique se é um palindromo")
fraseModificada = frase.replace(" ", "").lower()
if fraseModificada == fraseModificada[::-1]:
    print(f"a frase {frase} é um palindromo")
else:
    print(f"a frase {frase} não é um palindromo")

