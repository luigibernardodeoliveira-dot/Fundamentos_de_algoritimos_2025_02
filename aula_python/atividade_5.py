quantidade = int(input("digite a quantidade de numeros a serem testados  "))
primos = 0
for i in range (1, quantidade + 1):
    num = int(input(f"digite o numero {i}:"))
    
    if num> 1:
        eh_primo = True
        for j in range (2, num) :
            if num % j == 0:
                eh_primo = False
                break
            if eh_primo :
                primos += 1
                print(f"voce digitou {primos} numeros primos de um total de {quantidade}numeros ")  