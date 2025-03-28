frase = input("Digite uma frase: ")
contador = 0
frase = frase.lower()
for char in frase:
    if char in 'aeiou':
        contador += 1
print(f"A frase contém {contador} vogais.")