n1 = float(input("digite a primeira nota: "))
p1 = float(input("digite o peso da nota: "))
n2 = float(input("digite a segunda nota: "))
p2 = float(input("digite o peso da nota: "))
n3 = float(input("digite a terceira nota: "))
p3 = float(input("digite o peso da nota: "))
pesos = p1+p2+p3
print(pesos)
media = ((n1*p1)+(n2*p2)+(n3*p3))/pesos
print(f"a media das notas foi {media}")
if media >= 7:
    print("aluno aprovado!")
elif media >=4:
    print("aluno em recuperação!")
else:
    print("aluno reprovado!")