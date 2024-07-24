import tkinter as tk

# Função para calcular o resultado
def calcular(operacao):
    try:
        resultado = eval(operacao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para adicionar caracteres na entrada
def adicionar_caractere(caractere):
    entrada.insert(tk.END, caractere)

# Função para limpar a entrada
def limpar_entrada():
    entrada.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criar o campo de entrada
entrada = tk.Entry(janela, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
entrada.grid(row=0, column=0, columnspan=4)

# Definir os botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2)
]

# Adicionar os botões à janela
for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, padx=20, pady=20, command=lambda: calcular(entrada.get()))
    elif texto == 'C':
        botao = tk.Button(janela, text=texto, padx=20, pady=20, command=limpar_entrada)
    else:
        botao = tk.Button(janela, text=texto, padx=20, pady=20, command=lambda t=texto: adicionar_caractere(t))
    
    botao.grid(row=linha, column=coluna, sticky="nsew")

# Configurar o layout da grade
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
