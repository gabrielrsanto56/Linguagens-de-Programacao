import tkinter as tk #importa a biblioteca para interface gráfica
janela = tk.Tk() #atribuindo o método da janela a variavel janela
janela.title('ola mundo') #título da janela
rotulo = tk.Label(janela, text='ola mundo', font=('arial', 24)) #escrevendo uma mensagem
rotulo.grid(column=0, row=0) #local onde a mensagem ficará
rotulo.pack(pady=25)
janela.mainloop() #faz com que a janela permaneça aberta
