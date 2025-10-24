# def menu_principal():
#      while True:
#         print("SEJA BEM VINDO AO FEIFOOD")
#         print("1 - Cadastrar usuário")
#         print("2 - Login")
#         print("0 - Sair")
#         opcao = input("Escolha: ")

#         if opcao == "1":
#             cadastrar_usuario()
#         elif opcao == "2":
#             login_usuario()
#         elif opcao == "0":
#             break
#         else:
#             print("Opção inválida!")
        




# def cadastrar_usuario():
#     print("Cadastro de Usuário")
#     nome = input("Nome: ")
#     email = input("Email: ")
#     senha = input("Senha: ")
#     data_nasc = input("Data de nascimento (DD/MM/AAAA): ")






    
# def login_usuario():
#     print("Login")
#     email = input("Email: ")
#     senha = input("Senha: ")



# def menu_pedido():
#         print("CARDAPIO FEIFOOD")
#         print("1 - Listar alimentos")
#         print("2 - Fazer pedido")
#         print("3 - Ver pedidos")
#         print("4 - Avaliar pedido")
#         print("0 - Voltar")
#         opcao = input("Escolha: ")

#         if opcao == "1":
#             lista_alimentos()
#         elif opcao == "2":
#             fazer_pedido()
#         elif opcao == "3":
#             ver_pedidos()
#         elif opcao == "4":
#             avaliar_pedido()
#         elif opcao == "0":
#             menu_principal()
#         else:
#             print("Opção inválida!") 



cardapio = [
        ["Hambúrguer", ["Pequena - R$10", "Média - R$15", "Grande - R$20"]],
        ["Pizza", ["Pequena - R$20", "Média - R$30", "Grande - R$40"]],
        ["Refrigerante", ["Pequena - R$5", "Média - R$7", "Grande - R$10"]],
        ["Batata Frita", ["Pequena - R$8", "Média - R$12", "Grande - R$16"]],
        ["Açaí", ["300ml - R$12", "500ml - R$15", "700ml - R$18"]],
        ["Cachorro-Quente", ["Simples - R$10", "Duplo - R$14", "Especial - R$18"]],
        ["Lasanha", ["Bolonhesa - R$25", "Frango - R$27", "Quatro Queijos - R$28"]],
        ["Suco Natural", ["Copo 300ml - R$6", "Copo 500ml - R$8", "Jarra 1L - R$12"]],
        ["Salada", ["Pequena - R$10", "Média - R$13", "Grande - R$16"]],
        ["Sorvete", ["1 Bola - R$5", "2 Bolas - R$8", "3 Bolas - R$10"]],
        ["Milkshake", ["300ml - R$10", "500ml - R$13", "700ml - R$16"]],
        ["Café", ["Pequeno - R$4", "Médio - R$6", "Grande - R$8"]],
        ["Marmitex", ["Pequeno - R$18", "Médio - R$22", "Grande - R$26"]]
]
print(f"Cardápio {cardapio}")

def fazer_pedido():
    print("Fazer Pedido")
    alimento = input("Escolha o alimento: ")
    tamanho = input("Escolha o tamanho (Pequena, Média, Grande): ")
    quantidade = int(input("Quantidade: "))
    print(f"Pedido feito: {quantidade}x {tamanho} {alimento}")






def ver_pedidos():
    print("Ver Pedidos")
    print("Nenhum pedido feito ainda.") 






def avaliar_pedido():
    print("Avaliar Pedido")
    avaliacao = input("Como você avalia seu pedido? (1-5): ")
    print(f"Obrigado pela sua avaliação de {avaliacao} estrelas!")


def pagamento():
        print("Qual a forma de pagamento")
        print("1 - Pix")
        print("2 - Dinheiro")
        print("3 - Débito")
        print("4 - Crédito")
        opcao = input("Escolha: ")
        if opcao == "1":
            print("Pagamento via Pix selecionado.")
        elif opcao == "2":
            print("Pagamento em Dinheiro selecionado.")
        elif opcao == "3":
            print("Pagamento via Débito selecionado.")
        elif opcao == "4":
            print("Pagamento via Crédito selecionado.")
        else:
            print("Opção inválida!")

            def entregue():
                print("Seu pedido foi entregue!")

                def avaliar():
                        print("Avalie seu pedido de 1 a 5 estrelas.")
                        if opcao == "1":
                            print("Obrigado pela sua avaliação!")
                        elif opcao == "2":
                            print("Obrigado pela sua avaliação!")
                        elif opcao == "3":
                            print("Obrigado pela sua avaliação!")
                        elif opcao == "4":
                            print("Obrigado pela sua avaliação!")
                        elif opcao == "5":
                            print("Obrigado pela sua avaliação!")


    


    




# def menu_principal():
#     print("lista de alimentos")

# def porcao(media, pequena, grande):
#     print("tamanho")

# def preco():
#     print("depende do tamanho e do alimento ")
    
# def pedido():
#     print("aqui tera a nome_usuario, alimentos, porçao, preco")

# def pagamento():
#     print("pix,dinheiro,debito,credito")

# def chegou():
#     print("seu pedido chegou")
    
# def avaliar():
#     print("funçao para avaliar o pedido")
