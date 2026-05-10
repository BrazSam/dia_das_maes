import tkinter as tk
from tkinter import messagebox

janela =tk.Tk() # Criação da janela principal
janela.configure(bg = "#ffd6e7") # Configuração da cor de fundo da janela
janela.geometry("600x400") # Configuração do tamanho da janela
janela.title("Dia das Mães") # Título da janela


titulo= tk.Label(
    janela, 
    text="Feliz Dia das Mães!", 
    font=("Arial", 36, 'bold'), 
    bg="#ffd6e7", 
    fg="#ff69b4") # Criação de um rótulo com a mensagem de feliz dia das mães

titulo.pack(pady=50) # Posicionamento do rótulo na janela)

texto = tk.Label(
    janela,
    text="Mãe, resgate seu presente 🎁",
    font=("Arial", 24, 'bold'),
    bg="#ffd6e7",
    fg="#ff69b4") # Criação de um rótulo com a mensagem para resgatar o presente

texto.pack(pady=20) # Posicionamento do rótulo na janela

def resgatar_presente():
    messagebox.showinfo('Resgatado!', 'Eu sabia que ' \
                        'você preferia o meu abraço! ' \
                            'Feliz Dia das Mães!') # Função para exibir uma mensagem de resgate do presente
    
btn_presente = tk.Button(janela, text="Lavo a louça " \
                         "por uma semana", font=("Arial", 14), bg="#ff69b4", fg="white", command=resgatar_presente) # Criação de um botão para resgatar o presente

btn_presente.pack(pady=20) # Posicionamento do botão na janela

def mudar_texto(event):
    btn_presente.config(text="Um abraço 😁")

def voltar_texto(event):
    btn_presente.config(text="Lavo a louça por 1 semana")

btn_presente.bind("<Enter>", mudar_texto) # Evento para mudar o texto do botão quando o mouse passar por cima
btn_presente.bind("<Leave>", voltar_texto) # Evento para voltar o texto do botão


janela.mainloop()