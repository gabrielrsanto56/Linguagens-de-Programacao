escolha = int(input("deseja converter de Celsius para Farenheit [1]\n deseja converter de Celsius para Farenheit [2]\n"))
if escolha == 1:
    temperaturaCelsius = float(input("digite a temperatura: "))
    temperatura = temperaturaCelsius* 1.8 + 32
    print(f"{temperaturaCelsius} graus Celsius equivale a {temperatura} Farenheit")
elif escolha ==2:
    temperaturaFarenheit = float(input("digite a temperatura: "))
    temperatura = (temperaturaFarenheit - 32) / 1.8 
    print(f"{temperaturaFarenheit} graus Farenheit equivale a {temperatura} Celsius")
else:
    print("informações incorretas")