
pedidos = []
arquivo = open("feifood.txt", "a")
def menu_principal(): # Menu principal do sistema FeiFood aqui o usuário pode escolher entre cadastrar, logar ou sair
    while True:
        print("\n====== SEJA BEM-VINDO AO FEIFOOD ======")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("0 - Sair")
        print("=======================================")
        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            login_usuario()
        elif opcao == "0":
            print("===Saindo... Obrigado por usar o FeiFood!===")
            break
        else:
            print("Opção inválida!")







def cadastrar_usuario(): # Função para cadastrar um novo usuário aqui o usuario ira se cadastrar para en seguida poder logar
    print("\n========== Cadastro de Usuário ==========")#devera ser salvo em txt
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ")

    print(" Usuário cadastrado com sucesso!")
    print("Voltando ao menu principal...")
    print("=================================")





def login_usuario(): # Função para login do usuário aqui o usuario ira logar para poder fazer pedidos
    print("=========== Login ===========")
    email = input("Email: ")
    senha = input("Senha: ")

    print("Login realizado com sucesso!")
    print("=============================")








    menu_pedido()  # vai para o menu de pedidos








def menu_pedido():# Menu de pedidos do FeiFood aqui o usuario podera ver o cardapio, fazer pedidos, ver pedidos, finalizar e avaliar
    while True:# essa parte e um loop para o menu de pedidos
        print("======= CARDÁPIO FEIFOOD =======")
        print("1 - Listar alimentos")
        print("2 - Fazer pedido")
        print("3 - Ver pedidos")
        print("4 - Finalizar pedido")
        print("5 - Avaliar pedido")
        print("0 - Voltar ao menu principal")
        print("================================")
        opcao = input("Escolha: ")

        if opcao == "1":
            lista_alimentos()
        elif opcao == "2":
            fazer_pedido()
        elif opcao == "3":
            ver_pedidos()
        elif opcao == "4":
            finalizar_pedido()
        elif opcao == "5":
            avaliar_pedido()
        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida!")








def lista_alimentos(): # Função que cria e exibe a lista de alimentos com preços
    print("=== LISTA DE ALIMENTOS DISPONÍVEIS ===")
    A = [
        ["Pizza Calabresa", 35.00],
        ["Hambúrguer Artesanal", 22.50],
        ["Sushi Combo", 48.90],
        ["Lasanha Bolonhesa", 29.00],
        ["Salada Caesar", 19.50],
        ["Açaí 500ml", 15.00],
        ["Refrigerante Lata", 6.50],
        ["Suco Natural", 9.00],
        ["Batata Frita", 12.00],
        ["Coxinha", 5.00],
        ["Hot Dog", 10.00],
        ["Torta de Limão", 14.00],
        ["Sorvete 2 bolas", 10.00],
        ["Macarrão Carbonara", 27.50],
        ["Strogonoff de Frango", 28.00]
    ]

    for linha in range(len(A)): # Loop para exibir cada alimento e seu preço formatado
        for coluna in range(len(A[linha])):
            print(A[linha] [coluna], end=" - ")
        print() 

    return A  # retorna a lista de alimentos para uso posterior
    

def fazer_pedido():  
    pedidos = []   
    A = lista_alimentos()     

    while True:  # Inicia um loop para permitir que o usuário faça vários pedidos
        alimento = input("Escolha (ou digite 'fim' para encerrar): ")
                                 
        if alimento.lower() == "fim":
            break 
        encontrado = False # Variável de controle — indica se o alimento foi encontrado no cardápio

        # Procura o alimento dentro da lista 'A'
        for item in A: 
            if alimento.lower() == item[0].lower():   
                quantidade = int(input(f"Quantas unidades de {item[0]}? "))
                total_item = quantidade * item[1] # Calcula o valor total desse item
                pedidos.append([item[0], quantidade, total_item]) #adiciona o pedido à lista de pedidos 
                print(f"{quantidade}x {item[0]} adicionado(s) ao pedido.")
                                

                encontrado = True
                break #quando encontrar o alimento, sai do loop de for

        if not encontrado:#se nenhum alimento for encontrado
            print("Item não encontrado.")

    print("Pedido finalizado!")


def ver_pedidos():
    pedidos = []   

    print("======== SEUS PEDIDOS ======")

    if len(pedidos) == 0:  # Verifica se a lista de pedidos está vazia
        print("Nenhum pedido foi feito ainda.")
        return 

    total_geral = 0  #Variável para somar o valor total de todos os pedidos

    # Percorre todos os pedidos e exibe de forma organizada
    for item in pedidos:
        nome = item[0]       
        quantidade = item[1]   
        total_item = item[2]   

        print(f"{nome} - {quantidade}x - R$ {total_item:.2f}")
        total_geral += total_item  # Soma o valor ao total geral

    print(f"TOTAL DO PEDIDO: R$ {total_geral:.2f}")
    print("============================")



def finalizar_pedido():
    pedidos = []   
    if len(pedidos) == 0:
        print("Nenhum pedido para finalizar.")
        return

    ver_pedidos()
    print("Finalizando pedido...")
    pedidos.clear()  # Limpa a lista de pedidos após finalizar
    print("Seu pedido foi entrege !")


def avaliar_pedido():
    print("Avaliar Pedido")
    avaliacao = input("Como você avalia seu pedido? (1-5): ")
    print(f"Obrigado pela sua avaliação de {avaliacao} estrelas!")



# Inicia o programa
menu_principal()
