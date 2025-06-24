import tkinter as tk

# Função chamada ao clicar no botão
def mostrar_mensagem():
    mensagem_label.config(text="Bem-vindo")
    entrada_label.pack()
    entrada.pack()
    entrada.bind("<Return>", capturar_texto)  # Quando apertar Enter, chama a função

# Função para capturar o texto digitado
def capturar_texto(event):
    nome = entrada.get()
    resultado_label.config(text=f"Olá, {nome}!")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora mais que demais")
janela.geometry("300x500")
janela.resizable(True, True)

# Botão
botao = tk.Button(janela, text="Clique aqui e receba uma surpresa", command=mostrar_mensagem)
botao.pack(pady=100)

# Labels e Entry
mensagem_label = tk.Label(janela, text="")
mensagem_label.pack()

entrada_label = tk.Label(janela, text="Digite seu nome:")
entrada = tk.Entry(janela)

# Label para mostrar o resultado (ex: "Olá, Vinícius!")
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Loop principal
janela.mainloop()
