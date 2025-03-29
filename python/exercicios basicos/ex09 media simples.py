n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
media = (n1+n2+n3)/3
print(f"a media das notas foi {media}")
if media >= 7:
    print("aluno aprovado!")
elif media >=4:
    print("aluno em recuperação!")
else:
    print("aluno reprovado!")