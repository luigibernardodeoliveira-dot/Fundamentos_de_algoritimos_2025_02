
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
    print("\n========== Cadastro de Usuário ==========")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    senha2 = input("Confirme a senha: ")

    if senha != senha2:
        print("As senhas não coincidem! Tente novamente.")
        return


    arquivo = open("feifood.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    # Verifica se o email já existe
    for linha in linhas:
        _, email_salvo, _ = linha.strip().split(",")
        if email.lower() == email_salvo.lower():
            print("Este email já está cadastrado! Tente outro.")
            return


    arquivo = open("feifood.txt", "a")
    arquivo.write(f"{nome},{email},{senha}\n")
    arquivo.close()

    print("Usuário cadastrado com sucesso!\n")
    print("Voltando ao menu principal...")
    print("=================================")





def login_usuario(): # Função para login do usuário aqui o usuario ira logar para poder fazer pedidos
    print("=========== Login ===========")
    email = input("Email: ")
    senha = input("Senha: ")

    arquivo = open("feifood.txt", "r")
    linhas = arquivo.readlines() 
    arquivo.close()                     

    for linha in linhas:  # percorre cada linha do arquivo
            nome_salvo, email_salvo, senha_salva = linha.strip().split(",")#

            if email.lower() == email_salvo.lower() and senha == senha_salva:
                print(f"Login bem-sucedido! Bem-vindo, {nome_salvo}!")

                menu_pedido()
                return
    print("Email ou senha incorretos! Tente novamente.")
            

     



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

    # Dicionário com alimentos, preços e categorias
    A = {
       
        "Pizza Calabresa": {"preco": 35.00, "categoria": "Prato Principal"},
        "Pizza Quatro Queijos": {"preco": 37.00, "categoria": "Prato Principal"},
        "Pizza Portuguesa": {"preco": 39.00, "categoria": "Prato Principal"},
        "Lasanha Bolonhesa": {"preco": 29.00, "categoria": "Prato Principal"},
        "Macarrão Carbonara": {"preco": 27.50, "categoria": "Prato Principal"},
        "Strogonoff de Frango": {"preco": 28.00, "categoria": "Prato Principal"},
        "Strogonoff de Carne": {"preco": 31.00, "categoria": "Prato Principal"},
        "Filé de Frango Grelhado": {"preco": 25.00, "categoria": "Prato Principal"},
        "Feijoada Completa": {"preco": 32.00, "categoria": "Prato Principal"},
        "Bife à Parmegiana": {"preco": 33.00, "categoria": "Prato Principal"},
        "Risoto de Camarão": {"preco": 42.00, "categoria": "Prato Principal"},
        "Escondidinho de Carne Seca": {"preco": 29.90, "categoria": "Prato Principal"},
        "Panqueca de Carne": {"preco": 18.00, "categoria": "Prato Principal"},
        "Panqueca de Frango": {"preco": 17.50, "categoria": "Prato Principal"},
        "Yakissoba Tradicional": {"preco": 26.00, "categoria": "Prato Principal"},

        
        "Hambúrguer Artesanal": {"preco": 22.50, "categoria": "Lanche"},
        "Cheeseburger": {"preco": 18.00, "categoria": "Lanche"},
        "X-Bacon": {"preco": 23.00, "categoria": "Lanche"},
        "Hot Dog": {"preco": 10.00, "categoria": "Lanche"},
        "Misto Quente": {"preco": 8.50, "categoria": "Lanche"},
        "Tapioca Salgada": {"preco": 11.00, "categoria": "Lanche"},
        "Coxinha": {"preco": 5.00, "categoria": "Lanche"},
        "Esfiha de Queijo": {"preco": 5.50, "categoria": "Lanche"},
        "Pastel de Carne": {"preco": 7.00, "categoria": "Lanche"},
        "Empada de Frango": {"preco": 6.00, "categoria": "Lanche"},
        "Pão de Queijo": {"preco": 4.00, "categoria": "Lanche"},
        "Crepe Francês": {"preco": 20.00, "categoria": "Lanche"},
        "Batata Frita": {"preco": 12.00, "categoria": "Lanche"},
        "Batata com Cheddar e Bacon": {"preco": 18.00, "categoria": "Lanche"},
        "Mini Coxinhas (10un)": {"preco": 15.00, "categoria": "Lanche"},

    
        "Salada Caesar": {"preco": 19.50, "categoria": "Saudável"},
        "Salada Tropical": {"preco": 18.00, "categoria": "Saudável"},
        "Wrap de Frango": {"preco": 17.00, "categoria": "Fitness"},
        "Wrap Vegano": {"preco": 18.50, "categoria": "Vegano"},
        "Tapioca Doce": {"preco": 10.50, "categoria": "Fitness"},
        "Smoothie de Frutas Vermelhas": {"preco": 14.00, "categoria": "Fitness"},
        "Açaí 500ml": {"preco": 15.00, "categoria": "Fitness"},
        "Suco Detox": {"preco": 12.00, "categoria": "Fitness"},
        "Bowl de Frutas com Granola": {"preco": 16.00, "categoria": "Fitness"},
        "Tofu Grelhado com Legumes": {"preco": 22.00, "categoria": "Vegano"},
        "Hambúrguer Vegano": {"preco": 24.00, "categoria": "Vegano"},
        "Quinoa com Legumes": {"preco": 20.00, "categoria": "Vegano"},
        "Panqueca Integral de Banana": {"preco": 14.00, "categoria": "Fitness"},

       
        "Torta de Limão": {"preco": 14.00, "categoria": "Sobremesa"},
        "Bolo de Chocolate": {"preco": 8.50, "categoria": "Sobremesa"},
        "Brownie": {"preco": 9.00, "categoria": "Sobremesa"},
        "Donut": {"preco": 8.00, "categoria": "Sobremesa"},
        "Mousse de Maracujá": {"preco": 7.50, "categoria": "Sobremesa"},
        "Sorvete 2 bolas": {"preco": 10.00, "categoria": "Sobremesa"},
        "Petit Gâteau": {"preco": 15.00, "categoria": "Sobremesa"},
        "Pudim de Leite": {"preco": 9.50, "categoria": "Sobremesa"},
        "Creme Brûlée": {"preco": 17.00, "categoria": "Sobremesa"},
        "Açaí com Granola e Mel": {"preco": 17.50, "categoria": "Sobremesa"},

      
        "Refrigerante Lata": {"preco": 6.50, "categoria": "Bebida"},
        "Suco Natural": {"preco": 9.00, "categoria": "Bebida"},
        "Suco de Laranja": {"preco": 8.00, "categoria": "Bebida"},
        "Água Mineral": {"preco": 4.00, "categoria": "Bebida"},
        "Água com Gás": {"preco": 5.00, "categoria": "Bebida"},
        "Café Expresso": {"preco": 6.00, "categoria": "Bebida"},
        "Cappuccino": {"preco": 8.00, "categoria": "Bebida"},
        "Milkshake Chocolate": {"preco": 16.00, "categoria": "Bebida"},
        "Milkshake Morango": {"preco": 16.00, "categoria": "Bebida"},
        "Chá Gelado": {"preco": 7.50, "categoria": "Bebida"}
    }

  
    for nome in A:#
        print(f"{nome} - R$ {A[nome]['preco']:.2f} ({A[nome]['categoria']})")

    print("==================================================")
    return A



def fazer_pedido():# Função para fazer pedidos aqui o usuario podera escolher os itens do cardapio e fazer o pedido
    A = lista_alimentos()

    while True:
        alimento = input("Escolha um item (ou digite 'fim' para encerrar): ")

        if alimento.lower() == "fim":
            print("Pedido finalizado!")
            break

        if alimento in A:
            quantidade = int(input(f"Quantas unidades de {alimento}? "))
            total_item = quantidade * A[alimento]["preco"]

            # Salva o pedido no arquivo sem apagar os anteriores
            arquivo = open("pedidos.txt", "a")
            linha = f"{alimento},{quantidade},{total_item:.2f}\n"
            arquivo.write(linha)
            arquivo.close()

            print(f"{quantidade}x {alimento} adicionado ao pedido. Total: R$ {total_item:.2f}")
        else:
            print("Item não encontrado no cardápio.")





def ver_pedidos():
    print("========== PEDIDOS REALIZADOS ==========")

    arquivo = open("pedidos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    if len(linhas) == 0:
        print("Nenhum pedido realizado ainda.")
    else:
        # Mostra todos os pedidos atuais
        for linha in linhas:
            alimento, quantidade, total_item = linha.strip().split(",")
            print(f"{quantidade}x {alimento} - Total: R$ {total_item}")

        print("=======================================")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("0 - Voltar")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            A = lista_alimentos()  # pega o cardápio
            alimento = input("Nome do alimento que deseja adicionar: ")

            if alimento in A:
                quantidade = int(input("Quantidade: "))
                preco = A[alimento]["preco"]   # pega preço do dicionário
                total = quantidade * preco

                arquivo = open("pedidos.txt", "a")
                arquivo.write(f"{alimento},{quantidade},{total:.2f}\n")
                arquivo.close()
                print(f"{quantidade}x {alimento} adicionado com sucesso! Total R$ {total:.2f}")
            else:
                print("Item não está no cardápio.")

        elif opcao == 2:
            alimento = input("Nome do alimento que deseja remover: ")

            for i in range(len(linhas)):
                nome, quantidade, total_item = linhas[i].strip().split(",")
                if alimento.lower() == nome.lower():
                    linhas.pop(i)
                    break
            else:
                print("Esse item não está no pedido.")
                return

            arquivo = open("pedidos.txt", "w")
            arquivo.writelines(linhas)
            arquivo.close()
            print(f"{alimento} removido com sucesso!")

        elif opcao == 0:
            print("Voltando ao menu de pedidos...")
        else:
            print("Opção inválida!")

    print("=======================================")


   


def finalizar_pedido():
    arquivo = open("pedidos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    if len(linhas) == 0:
        print("Nenhum pedido realizado para finalizar.")
        return

    total_geral = 0
    print("========== RESUMO DO PEDIDO ==========")
    for linha in linhas:
        alimento, quantidade, total_item = linha.strip().split(",")
        print(f"{quantidade}x {alimento} - Total: R$ {total_item}")
        total_geral += float(total_item)

    print(f"Total Geral do Pedido: R$ {total_geral:.2f}")
    print("=====================================")

    confirmar = input("Deseja confirmar o pedido? (s/n): ")
    if confirmar.lower() == "s":

        print("Pedido confirmado! Obrigado por usar o FeiFood.")
        arquivo = open("pedidos.txt", "w")
        arquivo.close()
    else:
        print("Pedido não confirmado. Voltando ao menu de pedidos.")
    



    
def avaliar_pedido():
    avaliacao = input("Por favor, avalie seu pedido de 1 a 5 estrelas: ")
    comentario = input("Deixe um comentário sobre seu pedido (opcional): ")

    arquivo = open("avaliacoes.txt", "a")
    arquivo.write(f"Avaliacoes: {avaliacao} estrelas\nComentario: {comentario}\n\n")
    arquivo.close()

    print("Obrigado por sua avaliação!")
   

menu_principal()
