import tkinter as tk

# 1 - criando janela
window = tk.Tk()
window.geometry("300x150")
window.title("Minha primeira janela")

# 2 - Adiciona um frame
frame = tk.Frame(window)
# Um frame é um contêiner que pode conter outros widgets. Ele ajuda a organizar a 
#interface gráfica, permitindo agrupar elementos relacionados juntos.
# Você pode pensar em um frame como uma "caixa" dentro da janela principal onde você
# pode colocar botões, rótulos, campos de entrada e outros widgets.

# padx e pady são parâmetros usados em métodos de layout do Tkinter, 
# como pack(), grid e place(), para adicionar espaçamento (padding)
# ao redor dos widgets. Eles ajudam a melhorar a aparência e a 
# organização da interface gráfica.

frame.pack(padx=10, pady=10, fill='x', expand=True)

# A função pack() é um gerenciador de layout no Tkinter que organiza os widgets
# dentro de um contêiner (como uma janela ou um frame) de forma automática.
# Ela posiciona os widgets um após o outro, seja na vertical ou na horizontal, 
# dependendo das opções fornecidas.

# 3 - adicionando o label
label = tk.Label(frame, text="Olá, Mundo!")
label.pack(fill='x', expand=True)

# fill='x' faz com que o widget (neste caso, o label) se expanda horizontalmente
# para preencher todo o espaço disponível no eixo x (horizontal) 
# dentro do contêiner pai (frame).
# expand=True permite que o widget expanda para ocupar espaço extra
# disponível no contêiner pai, se houver.

# 4 - adicionando um input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())

# 6 - adicionando um botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()