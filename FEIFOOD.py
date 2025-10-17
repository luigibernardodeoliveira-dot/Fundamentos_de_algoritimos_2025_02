def menu_principal():
     while True:
        print("SEJA BEM VINDO AO FEIFOOD")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login_usuario()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")





def cadastrar_usuario():
    print("Cadastro de Usuário")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ")






    
def login_usuario():
    print("Login")
    email = input("Email: ")
    senha = input("Senha: ")



def menu_pedido():
        print("CARDAPIO FEIFOOD")
        print("1 - Listar alimentos")
        print("2 - Fazer pedido")
        print("3 - Ver pedidos")
        print("4 - Avaliar pedido")
        print("0 - Voltar")
        opcao = input("Escolha: ")

        if opcao == "1":
            lista_alimentos()
        elif opcao == "2":
            fazer_pedido()
        elif opcao == "3":
            ver_pedidos()
        elif opcao == "4":
            avaliar_pedido()
        elif opcao == "0":
            menu_principal()
        else:
            print("Opção inválida!")





def lista_alimentos():
    print("Lista de Alimentos")
    alimentos = ["Pizza", "Hambúrguer", "Sushi", "Salada"]
    for alimento in alimentos:
        print(f"- {alimento}")





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

menu_principal()

    




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
