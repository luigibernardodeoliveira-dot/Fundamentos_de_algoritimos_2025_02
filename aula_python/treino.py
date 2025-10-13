#exercicio 1
nome = input("Digite seu nome: ")
print(nome)



#exercicio 2
# Solicita os valores de A e B
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Calcula a soma
soma = A + B

# Exibe o resultado
print(soma)




#exercicio 3
numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))
prod = numero1 * numero2
print(f"prod = {prod}")





#exercicio4
# Define o valor de π
pi = 3.14159

# Solicita o valor do raio ao usuário
raio = float(input("Digite o valor do raio: "))

# Calcula a área
area = pi * raio ** 2

# Exibe o resultado
print(area)




#exercicio5

# Solicita os quatro valores inteiros
A = int(input(""))
B = int(input(""))
C = int(input(""))
D = int(input(""))
# Calcula a diferença
DIFERENCA = (A * B) - (C * D)
# Exibe o resultado
print(f"resultado {DIFERENCA}")




#exercicio 6
# Solicita a medida do ovo ao usuário
ovo = float(input("Digite a medida do ovo: "))

# Classifica o ovo com base na medida
if ovo < 30:
    print("pequeno")
else:
    print("grande")

#exercicio7
# Solicita os valores dos três produtos
produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))

# Calcula o total da compra
total = produto1 + produto2 + produto3

# Aplica o desconto conforme o valor total
if total > 500:
    desconto = total * 0.20
else:
    desconto = total * 0.10

# Exibe o valor do desconto com duas casas decimais
print(f"Desconto: {desconto:.2f}")




#exercicio8
import math

# Solicita a escolha do sólido
solido = input("Você deseja calcular o volume do dodecaedro ou icosaedro: ").strip().lower()

# Solicita a medida da aresta
aresta = float(input("Digite o valor da aresta a em metros: "))

# Calcula o volume conforme o sólido escolhido
if solido == "dodecaedro":
    volume = ((15 + 7 * math.sqrt(5)) / 4) * (aresta ** 3)
    print(f"O volume de um dodecaedro regular com {aresta:.2f} de aresta é: {volume:.2f}")
elif solido == "icosaedro":
    volume = (5 / 12) * (3 + math.sqrt(5)) * (aresta ** 3)
    print(f"O volume de um icosaedro regular com {aresta:.2f} de aresta é: {volume:.2f}")
else:
    print("Opção inválida. Escolha entre 'dodecaedro' ou 'icosaedro'.")
    


#exercicio9

# Solicita o código do produto
codigo = int(input("Digite o código do produto: "))

# Solicita a quantidade
quantidade = int(input("Digite a quantidade do produto: "))

# Define os preços com base no código
if codigo == 1:
    preco = 6.00
elif codigo == 2:
    preco = 7.00
elif codigo == 3:
    preco = 8.00
elif codigo == 4:
    preco = 3.00
elif codigo == 5:
    preco = 2.00
else:
    print("Código inválido.")
    preco = 0

# Calcula o total
total = preco * quantidade

# Exibe o resultado com duas casas decimais
if preco > 0:
    print(f"Total: R$ {total:.2f}")





#exercicio10
    # Solicita os dados do usuário
hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial:"))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

# Converte tudo para minutos
inicio_total = hora_inicial * 60 + minuto_inicial
fim_total = hora_final * 60 + minuto_final

# Se o fim for menor ou igual ao início, significa que passou da meia-noite
if fim_total <= inicio_total:
    fim_total += 24 * 60  # adiciona 24 horas em minutos

# Calcula a duração total em minutos
duracao_total = fim_total - inicio_total

# Converte de volta para horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

# Exibe o resultado
print(f"O jogo durou {duracao_horas} hora(s) e {duracao_minutos} minutos(s)")


#exercicio11


lados = int(input(""))

if lados == 3:
    print ("triângulo")
elif lados == 4:
    print ("quadrado")
elif lados == 5:
    print ("pentágono")
elif lados == 6:
    print("hexágono")
elif lados == 7:
    print ("heptágono")
elif lados == 8:
    print ("octógono")
elif lados == 9:
    print ("eneágono")
elif lados == 10:
    print ("decágono")
else:
    print ("Erro!")



#
for index in range()
print()