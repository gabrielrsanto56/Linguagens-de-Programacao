def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio  
        elif chute < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

listaNumeros = [5, 7, 8, 9, 12, 14, 15, 17, 20, 34, 54, 55, 57, 60, 61, 80 ]
indice = busca_binaria(listaNumeros, 55)

if indice != -1:
    print(f"o numero foi encontrado no indice {indice}")
else:
    print("o numero não está na lista")