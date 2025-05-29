lista = []
print("Digite zero [-1] para sair")
while True:
    numero= int(input("Digite um numero:"))
    if numero == -1:
        break

    if numero % 2 == 0:
        lista.append(numero)

qtd_par = len(lista)
soma_par = sum(lista)
media_par = soma_par/qtd_par

print(f"Quantidade de sumeros par -->{qtd_par}, Soma dos numeros pares -->{soma_par}, Média dos pares -->{media_par}", )
print(lista)
for item in lista:
    print(item)

