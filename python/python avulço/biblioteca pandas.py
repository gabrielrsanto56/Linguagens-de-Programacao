import pandas as pd #importa a biblioteca pandas e a chama de pd

pessoas = {
    "Nome": ["Gabriel", "Alexandre", "Guilherme"],
    "idades": [19, 18, 20],
    "profissões": ["programador back-end", "monitor da escola cívica", "programador front-end"]
}#fazendo um dicionario com informações

base = pd.DataFrame(pessoas) #atribuindo o dicionario a variavel base, mas pode se ler csv, exel entre outros
ordenar_iades = base["idades"].sort_values(ascending=True) #ordena as idades


print(base) #mostrando o conteudo do dicionario
print(ordenar_iades)