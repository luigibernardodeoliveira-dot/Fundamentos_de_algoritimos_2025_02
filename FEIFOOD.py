
pedidos = []

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
    senha2 = input("Confirme a senha: ")

    if senha != senha2:
        print("As senhas não coincidem! Tente novamente.")
        return


    try:
        #Abre o arquivo existente
        arquivo = open("feifood.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()

            #Verifica se o e-mail já está cadastrado
        for linha in linhas:   
            _, email_salvo, _ = linha.strip().split(",")# _ ignora nome e senha
            if email.lower() == email_salvo.lower():
                print("Este email já está cadastrado! Tente outro.")
                return

    except FileNotFoundError:  
   


        arquivo = open("feifood.txt", "a")  # salva em modo append
        arquivo.write(f"{nome},{email},{senha}\n")
        arquivo.close()

    print(" Usuário cadastrado com sucesso!")
    print("Voltando ao menu principal...")
    print("=================================")





def login_usuario(): # Função para login do usuário aqui o usuario ira logar para poder fazer pedidos
    print("=========== Login ===========")
    email = input("Email: ")
    senha = input("Senha: ")

    try:
        arquivo = open("feifood.txt", "r")  # abre o arquivo no modo leitura
        linhas = arquivo.readlines()        # lê todas as linhas do arquivo
        arquivo.close()                     # fecha o arquivo (mesmo estilo do original)

        for linha in linhas:  # percorre cada linha do arquivo
            nome_salvo, email_salvo, senha_salva = linha.strip().split(",")

            # Verifica se o email e senha batem
            if email == email_salvo and senha == senha_salva:
                print(f"Login realizado com sucesso! Bem-vindo(a), {nome_salvo}!")
                print("=============================")
                menu_pedido()  # entra no menu de pedidos
                return# sai da função após login bem-sucedido

        # se nenhuma correspondência for encontrada
        print("Email ou senha incorretos. Tente novamente!")

    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda. Cadastre-se primeiro!")





    menu_pedido()  # vai para o menu de pedidos








def menu_pedido():# Menu de pedidos do FeiFood aqui o usuario podera ver o cardapio, fazer pedidos, ver pedidos, finalizar e avaliar
    while True:# essa parte e um loop para o menu de pedidos
        print("======= CARDÁPIO FEIFOOD =======")
        print("1 - Fazer pedido")
        print("2 - Ver pedidos")
        print("3 - Finalizar pedido")
        print("4 - Avaliar pedido")
        print("0 - Voltar ao menu principal")
        print("================================")
        opcao = input("Escolha: ")

     
        if opcao == "1":
            fazer_pedido()
        elif opcao == "2":
            ver_pedidos()
        elif opcao == "3":
            finalizar_pedido()
        elif opcao == "4":
            avaliar_pedido()
        elif opcao == "0":
            print("Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida!")








def lista_alimentos():
    print("========== LISTA DE ALIMENTOS DISPONÍVEIS ============")

    A = [
        # PRATOS PRINCIPAIS
        {"nome": "Pizza Calabresa", "preco": 35.00, "categoria": "Prato Principal"},
        {"nome": "Pizza Quatro Queijos", "preco": 37.00, "categoria": "Prato Principal"},
        {"nome": "Pizza Portuguesa", "preco": 39.00, "categoria": "Prato Principal"},
        {"nome": "Lasanha Bolonhesa", "preco": 29.00, "categoria": "Prato Principal"},
        {"nome": "Macarrão Carbonara", "preco": 27.50, "categoria": "Prato Principal"},
        {"nome": "Strogonoff de Frango", "preco": 28.00, "categoria": "Prato Principal"},
        {"nome": "Strogonoff de Carne", "preco": 31.00, "categoria": "Prato Principal"},
        {"nome": "Filé de Frango Grelhado", "preco": 25.00, "categoria": "Prato Principal"},
        {"nome": "Feijoada Completa", "preco": 32.00, "categoria": "Prato Principal"},
        {"nome": "Bife à Parmegiana", "preco": 33.00, "categoria": "Prato Principal"},
        {"nome": "Risoto de Camarão", "preco": 42.00, "categoria": "Prato Principal"},
        {"nome": "Escondidinho de Carne Seca", "preco": 29.90, "categoria": "Prato Principal"},
        {"nome": "Panqueca de Carne", "preco": 18.00, "categoria": "Prato Principal"},
        {"nome": "Panqueca de Frango", "preco": 17.50, "categoria": "Prato Principal"},
        {"nome": "Yakissoba Tradicional", "preco": 26.00, "categoria": "Prato Principal"},

        # LANCHES
        {"nome": "Hambúrguer Artesanal", "preco": 22.50, "categoria": "Lanche"},
        {"nome": "Cheeseburger", "preco": 18.00, "categoria": "Lanche"},
        {"nome": "X-Bacon", "preco": 23.00, "categoria": "Lanche"},
        {"nome": "Hot Dog", "preco": 10.00, "categoria": "Lanche"},
        {"nome": "Misto Quente", "preco": 8.50, "categoria": "Lanche"},
        {"nome": "Tapioca Salgada", "preco": 11.00, "categoria": "Lanche"},
        {"nome": "Coxinha", "preco": 5.00, "categoria": "Lanche"},
        {"nome": "Esfiha de Queijo", "preco": 5.50, "categoria": "Lanche"},
        {"nome": "Pastel de Carne", "preco": 7.00, "categoria": "Lanche"},
        {"nome": "Empada de Frango", "preco": 6.00, "categoria": "Lanche"},
        {"nome": "Pão de Queijo", "preco": 4.00, "categoria": "Lanche"},
        {"nome": "Crepe Francês", "preco": 20.00, "categoria": "Lanche"},
        {"nome": "Batata Frita", "preco": 12.00, "categoria": "Lanche"},
        {"nome": "Batata com Cheddar e Bacon", "preco": 18.00, "categoria": "Lanche"},
        {"nome": "Mini Coxinhas (10un)", "preco": 15.00, "categoria": "Lanche"},

        # SAUDÁVEIS / VEGANOS / FITNESS
        {"nome": "Salada Caesar", "preco": 19.50, "categoria": "Saudável"},
        {"nome": "Salada Tropical", "preco": 18.00, "categoria": "Saudável"},
        {"nome": "Wrap de Frango", "preco": 17.00, "categoria": "Fitness"},
        {"nome": "Wrap Vegano", "preco": 18.50, "categoria": "Vegano"},
        {"nome": "Tapioca Doce", "preco": 10.50, "categoria": "Fitness"},
        {"nome": "Smoothie de Frutas Vermelhas", "preco": 14.00, "categoria": "Fitness"},
        {"nome": "Açaí 500ml", "preco": 15.00, "categoria": "Fitness"},
        {"nome": "Suco Detox", "preco": 12.00, "categoria": "Fitness"},
        {"nome": "Bowl de Frutas com Granola", "preco": 16.00, "categoria": "Fitness"},
        {"nome": "Tofu Grelhado com Legumes", "preco": 22.00, "categoria": "Vegano"},
        {"nome": "Hambúrguer Vegano", "preco": 24.00, "categoria": "Vegano"},
        {"nome": "Quinoa com Legumes", "preco": 20.00, "categoria": "Vegano"},
        {"nome": "Panqueca Integral de Banana", "preco": 14.00, "categoria": "Fitness"},

        # SOBREMESAS
        {"nome": "Torta de Limão", "preco": 14.00, "categoria": "Sobremesa"},
        {"nome": "Bolo de Chocolate", "preco": 8.50, "categoria": "Sobremesa"},
        {"nome": "Brownie", "preco": 9.00, "categoria": "Sobremesa"},
        {"nome": "Donut", "preco": 8.00, "categoria": "Sobremesa"},
        {"nome": "Mousse de Maracujá", "preco": 7.50, "categoria": "Sobremesa"},
        {"nome": "Sorvete 2 bolas", "preco": 10.00, "categoria": "Sobremesa"},
        {"nome": "Petit Gâteau", "preco": 15.00, "categoria": "Sobremesa"},
        {"nome": "Pudim de Leite", "preco": 9.50, "categoria": "Sobremesa"},
        {"nome": "Creme Brûlée", "preco": 17.00, "categoria": "Sobremesa"},
        {"nome": "Açaí com Granola e Mel", "preco": 17.50, "categoria": "Sobremesa"},

        # BEBIDAS
        {"nome": "Refrigerante Lata", "preco": 6.50, "categoria": "Bebida"},
        {"nome": "Suco Natural", "preco": 9.00, "categoria": "Bebida"},
        {"nome": "Suco de Laranja", "preco": 8.00, "categoria": "Bebida"},
        {"nome": "Água Mineral", "preco": 4.00, "categoria": "Bebida"},
        {"nome": "Água com Gás", "preco": 5.00, "categoria": "Bebida"},
        {"nome": "Café Expresso", "preco": 6.00, "categoria": "Bebida"},
        {"nome": "Cappuccino", "preco": 8.00, "categoria": "Bebida"},
        {"nome": "Milkshake Chocolate", "preco": 16.00, "categoria": "Bebida"},
        {"nome": "Milkshake Morango", "preco": 16.00, "categoria": "Bebida"},
        {"nome": "Chá Gelado", "preco": 7.50, "categoria": "Bebida"}
    ]
    for item in A:
        print(f"{item['nome']} - R$ {item['preco']:.2f} ({item['categoria']})")

    print("==================================================")
    return A



def fazer_pedido():
    pedidos = []    
    A = lista_alimentos()

    while True:
        alimento = input("Escolha um item (ou digite 'fim' para encerrar): ")

        if alimento.lower() == "fim":
            break

        encontrado = False

        for item in A:
            if alimento.lower() == item["nome"].lower():
                quantidade = int(input(f"Quantas unidades de {item['nome']}? "))
                total_item = quantidade * item["preco"]
                pedidos.append({"nome": item["nome"], "quantidade": quantidade, "total": total_item})
                print(f"{quantidade}x {item['nome']} adicionado ao pedido.")
                encontrado = True
                break

        if not encontrado:
            print("Item não encontrado no cardápio.")

    print("Pedido finalizado!")



def ver_pedidos():
    global pedidos
    print("======== SEUS PEDIDOS ======")

    if not pedidos:
        print("Nenhum pedido foi feito ainda.")
        return

    total_geral = 0
    for item in pedidos:
        print(f"{item['nome']} - {item['quantidade']}x - R$ {item['total']:.2f}")
        total_geral += item['total']

    print(f"TOTAL DO PEDIDO: R$ {total_geral:.2f}")
    print("============================")


def finalizar_pedido():
    global pedidos
    if not pedidos:
        print("Nenhum pedido para finalizar.")
        return

    ver_pedidos()
    print("Finalizando pedido...")
    pedidos.clear()
    print("Seu pedido foi entregue!")



def avaliar_pedido():
    print("Avaliar Pedido")
    avaliacao = input("Como você avalia seu pedido? (1-5): ")
    print(f"Obrigado pela sua avaliação de {avaliacao} estrelas!")



# Inicia o programa
menu_principal()
