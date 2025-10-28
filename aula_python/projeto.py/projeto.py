# feifood.py
# Projeto FEIFood - versão funcional simples usando arquivos .txt
# Arquivos usados: usuarios.txt, alimentos.txt, pedidos.txt
# Autor: Gerado pelo ChatGPT (adaptar conforme necessário)

import os
import datetime
import itertools

USUARIOS_FILE = "usuarios.txt"
ALIMENTOS_FILE = "alimentos.txt"
PEDIDOS_FILE = "pedidos.txt"

# --- Helpers de arquivo ----------------------------------------------------
def ensure_files():
    for f in (USUARIOS_FILE, ALIMENTOS_FILE, PEDIDOS_FILE):
        if not os.path.exists(f):
            open(f, "a").close()

def ler_usuarios():
    usuarios = []
    try:
        with open(USUARIOS_FILE, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                nome, email, senha, data_nasc = linha.split(";")
                usuarios.append({"nome": nome, "email": email, "senha": senha, "data_nasc": data_nasc})
    except FileNotFoundError:
        pass
    return usuarios

def salvar_usuario_txt(usuario):
    with open(USUARIOS_FILE, "a", encoding="utf-8") as arq:
        arq.write(f"{usuario['nome']};{usuario['email']};{usuario['senha']};{usuario['data_nasc']}\n")

def ler_alimentos():
    alimentos = []
    try:
        with open(ALIMENTOS_FILE, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                # formato: id;nome
                id_, nome = linha.split(";", 1)
                alimentos.append({"id": int(id_), "nome": nome})
    except FileNotFoundError:
        pass
    return alimentos

def salvar_alimentos_lista(alimentos):
    with open(ALIMENTOS_FILE, "w", encoding="utf-8") as arq:
        for a in alimentos:
            arq.write(f"{a['id']};{a['nome']}\n")

def ler_pedidos():
    pedidos = []
    try:
        with open(PEDIDOS_FILE, "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                # formato:
                # id;email_usuario;data;itens_str;avaliacao
                # itens_str = itemId:quantidade: tamanho | itemId:quantidade:tamanho | ...
                id_, email, data_hora, itens_str, avaliacao = linha.split(";", 4)
                itens = []
                if itens_str:
                    for it in itens_str.split("|"):
                        if not it:
                            continue
                        parts = it.split(":")
                        # itemId:quantidade:tamanho:itemNomeEncoded
                        if len(parts) >= 4:
                            itemId, qtd, tamanho, nome_enc = parts
                            itens.append({"id": int(itemId), "qtd": int(qtd), "tamanho": tamanho, "nome": nome_enc})
                avg = None
                if avaliacao.strip() != "":
                    avg = int(avaliacao)
                pedidos.append({"id": int(id_), "email": email, "data_hora": data_hora, "itens": itens, "avaliacao": avg})
    except FileNotFoundError:
        pass
    return pedidos

def salvar_pedidos_lista(pedidos):
    with open(PEDIDOS_FILE, "w", encoding="utf-8") as arq:
        for p in pedidos:
            itens_str = "|".join(f"{it['id']}:{it['qtd']}:{it['tamanho']}:{it['nome']}" for it in p["itens"])
            aval = "" if p["avaliacao"] is None else str(p["avaliacao"])
            arq.write(f"{p['id']};{p['email']};{p['data_hora']};{itens_str};{aval}\n")

# --- Utilitários -----------------------------------------------------------
def gerar_id(lista):
    if not lista:
        return 1
    else:
        return max(item["id"] for item in lista) + 1

def encontrar_alimento_por_id(alimentos, id_):
    for a in alimentos:
        if a["id"] == id_:
            return a
    return None

# --- Funcionalidades do usuário --------------------------------------------
def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
    usuarios = ler_usuarios()
    if any(u["email"].lower() == email.lower() for u in usuarios):
        print("Erro: email já cadastrado.")
        return
    usuario = {"nome": nome, "email": email, "senha": senha, "data_nasc": data_nasc}
    salvar_usuario_txt(usuario)
    print("Usuário cadastrado com sucesso!")

def login_usuario():
    print("\n=== Login de Usuário ===")
    email = input("Email: ").strip()
    senha = input("Senha: ").strip()
    usuarios = ler_usuarios()
    for u in usuarios:
        if u["email"].lower() == email.lower() and u["senha"] == senha:
            print(f"Bem-vindo(a), {u['nome']}!")
            return u
    print("Login incorreto.")
    return None

# --- Pedido e avaliações ---------------------------------------------------
def menu_pedido(usuario):
    while True:
        print("\n=== CARDÁPIO FEIFOOD ===")
        print("1 - Listar alimentos")
        print("2 - Fazer pedido")
        print("3 - Ver meus pedidos")
        print("4 - Avaliar pedido")
        print("5 - Excluir pedido")
        print("0 - Voltar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            lista_alimentos()
        elif opcao == "2":
            fazer_pedido(usuario)
        elif opcao == "3":
            ver_pedidos_usuario(usuario)
        elif opcao == "4":
            avaliar_pedido(usuario)
        elif opcao == "5":
            excluir_pedido_usuario(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def lista_alimentos():
    alimentos = ler_alimentos()
    if not alimentos:
        print("Nenhum alimento cadastrado.")
        return
    print("\n--- Alimentos Disponíveis ---")
    for a in alimentos:
        print(f"{a['id']} - {a['nome']}")

def fazer_pedido(usuario):
    alimentos = ler_alimentos()
    if not alimentos:
        print("Nenhum alimento disponível no momento.")
        return
    pedidos = ler_pedidos()
    id_pedido = gerar_id(pedidos)
    itens_pedido = []
    while True:
        lista_alimentos()
        escolha = input("Digite o ID do alimento para adicionar (ou 'fim' para finalizar): ").strip()
        if escolha.lower() == "fim":
            break
        try:
            id_alim = int(escolha)
        except ValueError:
            print("ID inválido.")
            continue
        alim = encontrar_alimento_por_id(alimentos, id_alim)
        if not alim:
            print("Alimento não encontrado.")
            continue
        try:
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida. Use número inteiro.")
            continue
        tamanho = input("Tamanho (Pequena, Média, Grande): ").strip()
        itens_pedido.append({"id": alim["id"], "qtd": qtd, "tamanho": tamanho, "nome": alim["nome"]})
        print(f"{qtd}x {tamanho} {alim['nome']} adicionado ao pedido.")
    if not itens_pedido:
        print("Pedido vazio, cancelado.")
        return
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    novo = {"id": id_pedido, "email": usuario["email"], "data_hora": data_hora, "itens": itens_pedido, "avaliacao": None}
    pedidos.append(novo)
    salvar_pedidos_lista(pedidos)
    print(f"Pedido #{id_pedido} criado com sucesso!")

def ver_pedidos_usuario(usuario):
    pedidos = ler_pedidos()
    seus = [p for p in pedidos if p["email"].lower() == usuario["email"].lower()]
    if not seus:
        print("Você não tem pedidos.")
        return
    print("\n--- Seus Pedidos ---")
    for p in seus:
        print(f"Pedido #{p['id']} - {p['data_hora']} - Avaliação: {p['avaliacao'] if p['avaliacao'] is not None else 'Não avaliado'}")
        for it in p["itens"]:
            print(f"   - {it['qtd']}x {it['tamanho']} {it['nome']} (id {it['id']})")

def avaliar_pedido(usuario):
    pedidos = ler_pedidos()
    seus = [p for p in pedidos if p["email"].lower() == usuario["email"].lower()]
    if not seus:
        print("Você não tem pedidos para avaliar.")
        return
    try:
        idp = int(input("Digite o ID do pedido que quer avaliar: "))
    except ValueError:
        print("ID inválido.")
        return
    p_encontrado = None
    for p in seus:
        if p["id"] == idp:
            p_encontrado = p
            break
    if not p_encontrado:
        print("Pedido não encontrado ou não pertence a você.")
        return
    if p_encontrado["avaliacao"] is not None:
        print("Pedido já avaliado.")
        return
    try:
        nota = int(input("Avaliação (0 a 5): "))
    except ValueError:
        print("Avaliação inválida.")
        return
    if nota < 0 or nota > 5:
        print("Avaliação deve ser entre 0 e 5.")
        return
    # atualizar pedido
    all_pedidos = ler_pedidos()
    for p in all_pedidos:
        if p["id"] == idp:
            p["avaliacao"] = nota
            break
    salvar_pedidos_lista(all_pedidos)
    print("Obrigado pela avaliação!")

def excluir_pedido_usuario(usuario):
    pedidos = ler_pedidos()
    try:
        idp = int(input("Digite o ID do pedido que quer excluir: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in pedidos:
        if p["id"] == idp and p["email"].lower() == usuario["email"].lower():
            pedidos.remove(p)
            salvar_pedidos_lista(pedidos)
            print(f"Pedido #{idp} excluído.")
            return
    print("Pedido não encontrado ou não pertence a você.")

# --- Admin -----------------------------------------------------------------
# credenciais de admin simples (pode ser alterado)
ADMIN_EMAIL = "admin@feifood"
ADMIN_SENHA = "admin123"

def login_admin():
    print("\n=== Login Administrador ===")
    email = input("Email admin: ").strip()
    senha = input("Senha admin: ").strip()
    if email.lower() == ADMIN_EMAIL and senha == ADMIN_SENHA:
        print("Login administrador OK.")
        return True
    print("Credenciais admin inválidas.")
    return False

def menu_admin():
    while True:
        print("\n=== MENU ADMINISTRADOR ===")
        print("1 - Cadastrar alimento")
        print("2 - Excluir alimento")
        print("3 - Consultar usuários")
        print("4 - Ver estatísticas")
        print("5 - Listar alimentos")
        print("0 - Voltar")
        op = input("Escolha: ").strip()
        if op == "1":
            cadastrar_alimento()
        elif op == "2":
            excluir_alimento()
        elif op == "3":
            consultar_usuarios()
        elif op == "4":
            ver_estatisticas()
        elif op == "5":
            lista_alimentos()
        elif op == "0":
            break
        else:
            print("Opção inválida.")

def cadastrar_alimento():
    nome = input("Nome do alimento: ").strip()
    alimentos = ler_alimentos()
    id_novo = gerar_id(alimentos)
    alimentos.append({"id": id_novo, "nome": nome})
    salvar_alimentos_lista(alimentos)
    print(f"Alimento '{nome}' cadastrado com ID {id_novo}.")

def excluir_alimento():
    alimentos = ler_alimentos()
    if not alimentos:
        print("Nenhum alimento cadastrado.")
        return
    try:
        id_ex = int(input("ID do alimento a excluir: "))
    except ValueError:
        print("ID inválido.")
        return
    for a in alimentos:
        if a["id"] == id_ex:
            alimentos.remove(a)
            salvar_alimentos_lista(alimentos)
            print(f"Alimento ID {id_ex} removido.")
            return
    print("Alimento não encontrado.")

def consultar_usuarios():
    usuarios = ler_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print("\n--- Usuários ---")
    for u in usuarios:
        print(f"{u['nome']} - {u['email']} - {u['data_nasc']}")

def ver_estatisticas():
    alimentos = ler_alimentos()
    pedidos = ler_pedidos()
    usuarios = ler_usuarios()
    total_users = len(usuarios)
    total_alimentos = len(alimentos)
    # calcular médias por alimento a partir das avaliações dos pedidos
    notas_por_alimento = {}
    for p in pedidos:
        if p["avaliacao"] is None:
            continue
        for it in p["itens"]:
            id_ = it["id"]
            notas_por_alimento.setdefault(id_, []).append(p["avaliacao"])
    medias = []
    for a in alimentos:
        notas = notas_por_alimento.get(a["id"], [])
        if notas:
            media = sum(notas) / len(notas)
            medias.append({"id": a["id"], "nome": a["nome"], "media": media, "qtd_avals": len(notas)})
    medias_sorted_desc = sorted(medias, key=lambda x: x["media"], reverse=True)
    medias_sorted_asc = sorted(medias, key=lambda x: x["media"])
    print("\n=== Estatísticas ===")
    print(f"Total de usuários: {total_users}")
    print(f"Total de alimentos: {total_alimentos}")
    print("\nTop 5 melhores alimentos (por média de avaliações):")
    for a in medias_sorted_desc[:5]:
        print(f"  {a['nome']} - média {a['media']:.2f} ({a['qtd_avals']} avaliações)")
    print("\nTop 5 piores alimentos (por média de avaliações):")
    for a in medias_sorted_asc[:5]:
        print(f"  {a['nome']} - média {a['media']:.2f} ({a['qtd_avals']} avaliações)")

# --- Menu Principal --------------------------------------------------------
def menu_principal():
    ensure_files()
    while True:
        print("\n=== SEJA BEM VINDO AO FEIFOOD ===")
        print("1 - Cadastrar usuário")
        print("2 - Login (usuário)")
        print("3 - Login (administrador)")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = login_usuario()
            if usuario:
                menu_pedido(usuario)
        elif opcao == "3":
            ok = login_admin()
            if ok:
                menu_admin()
        elif opcao == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
