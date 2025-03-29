escolha = int(input("digite um numero para ver a sequencia de fibonacci até o termo: "))
a, b = 0, 1
for _ in range(escolha):
    print(a, end=" ")  
    a, b = b, a + b    
print()
