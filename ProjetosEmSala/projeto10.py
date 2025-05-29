lista = []
print("Digite [0] para sair")
while True:
    valor = int(input("valor inteiro:"))
    if valor == 0:
        break
    lista.append(valor)
# menor = min(lista)
# maior = max(lista)

# print("O maior valor da lista -->", maior)
# print("O menor valor da lista -->", menor)
lista.sort()
print(f"Lista em orden crescente{lista}")
print(f"O menor numero da lita-->{lista[0]}")
print(f"o maior numero da lista-->{lista[-1]}")

for item in lista:
    print(lista.index(item), item)

