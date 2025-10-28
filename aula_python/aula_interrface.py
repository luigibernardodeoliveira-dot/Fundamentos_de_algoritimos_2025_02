# from tkinter import *

# # Cria a janela
# janela = Tk()

# # Título da janela
# janela.title("Algoritmos")

# # Configura o tamanho da janela
# janela.geometry('400x400')

# # Loop infinito para manter a janela aberta
# janela.mainloop()





# from tkinter import *

# # Cria a janela principal
# janela = Tk()
# janela.title("Algoritmos")
# janela.geometry("400x400")

# # Cria um rótulo (label) na janela, adiciona um texto e configura a fonte
# rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))

# # Define onde a label vai aparecer na janela
# rotulo.place(x=200, y=100, anchor="center")

# # Mantém a janela aberta
# janela.mainloop()



# from tkinter import *

# # Cria a janela principal
# window = Tk()
# window.title("Nova tela")
# window.geometry("350x200")

# # Cria o primeiro botão e posiciona no centro
# btn1 = Button(window, text="Botão 1")
# btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

# # Cria o segundo botão e posiciona em uma coordenada fixa
# btn2 = Button(window, text="Botão 2")
# btn2.place(x=100, y=50, anchor=CENTER)

# # Mantém a janela aberta
# window.mainloop()


# from tkinter import *

# # Cria a janela principal
# janela = Tk()
# janela.title("Algoritmos")
# janela.geometry("400x400")

# # Cria um rótulo na janela, adiciona um texto e configura a fonte
# rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))
# rotulo.place(x=200, y=100, anchor="center")

# # Cria o botão na janela com o texto desejado
# botao = Button(janela, text="Clique aqui!")
# botao.place(x=200, y=200, anchor=CENTER)

# # Mantém a janela aberta
# janela.mainloop()





# from tkinter import *

# # Cria a janela principal
# janela = Tk()
# janela.title("Algoritmos")
# janela.geometry("400x400")

# # Cria o rótulo na janela
# rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))
# rotulo.place(x=200, y=100, anchor="center")

# # Define a função que será chamada ao clicar no botão
# def clique():
#     rotulo["text"] = "Novo texto!"

# # Cria o botão na janela com o texto desejado
# botao = Button(janela, text="Clique aqui!", command=clique)
# botao.place(x=200, y=200, anchor=CENTER)

# # Mantém a janela aberta
# janela.mainloop()




# from tkinter import *

# # Cria a janela principal
# janela = Tk()
# janela.title("Algoritmos")
# janela.geometry("400x400")

# # Cria o rótulo e posiciona
# rotulo = Label(janela, text="Hello GUI!", font=("Arial Bold", 14))
# rotulo.place(x=200, y=100, anchor="center")

# # Cria o campo de entrada de texto e define seu tamanho e posição
# entrada = Entry(janela, width=14, font=("Arial Bold", 14))
# entrada.place(x=200, y=50, anchor=CENTER)

# # Define a função que será chamada ao clicar no botão
# def clique():
#     resposta = entrada.get()   # Pega o texto digitado
#     rotulo["text"] = resposta  # Atualiza o rótulo com o texto

# # Cria o botão e define a ação do clique
# botao = Button(janela, text="Clique aqui!", command=clique)
# botao.place(x=200, y=200, anchor=CENTER)

# # Mantém a janela aberta
# janela.mainloop()




# from tkinter import *
# # from tkinter import messagebox

# # # Cria a janela principal
# # janela = Tk()
# # janela.title("Exemplo MessageBox")
# # janela.geometry("300x200")

# # # Define a função que será executada ao clicar no botão
# # def show():
# #     res = messagebox.showinfo("Aviso", "O botão foi clicado!")
# #     print(res)  # Exibe no console o retorno da messagebox (normalmente 'ok')

# # # Cria o botão e adiciona à janela
# # botao2 = Button(janela, text="Botão", command=show)
# # botao2.place(x=150, y=100, anchor=CENTER)

# # # Mantém a janela aberta
# # janela.mainloop()





# from tkinter import *
# from tkinter import messagebox

# # Cria a janela principal
# janela = Tk()
# janela.title("Exemplo MessageBox")
# janela.geometry("300x250")

# # Funções de exemplo para cada tipo de caixa de diálogo
# def exemplo_askquestion():
#     res = messagebox.askquestion("Aviso", "Botão clicado!")
#     print("Retorno:", res)  # Retorna "yes" ou "no"

# def exemplo_askyesnocancel():
#     res = messagebox.askyesnocancel("Aviso", "Botão clicado!")
#     print("Retorno:", res)  # Retorna True, False ou None

# def exemplo_askokcancel():
#     res = messagebox.askokcancel("Aviso", "Botão clicado!")
#     print("Retorno:", res)  # Retorna True ou False

# def exemplo_askretrycancel():
#     res = messagebox.askretrycancel("Aviso", "Botão clicado!")
#     print("Retorno:", res)  # Retorna True ou False

# # Cria um botão para cada tipo de messagebox
# Button(janela, text="askquestion", command=exemplo_askquestion).pack(pady=5)
# Button(janela, text="askyesnocancel", command=exemplo_askyesnocancel).pack(pady=5)
# Button(janela, text="askokcancel", command=exemplo_askokcancel).pack(pady=5)
# Button(janela, text="askretrycancel", command=exemplo_askretrycancel).pack(pady=5)

# # Mantém a janela aberta
# janela.mainloop()
