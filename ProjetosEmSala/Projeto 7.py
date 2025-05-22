lista = []

print("Digite [0] para sair")
while True:
    valor = int(input("Valor: "))
    if valor == 0:
        break
    else:
        lista.append(valor)
print(lista)
for i in lista:
    print(i)
qtd=len(lista)
soma=sum(lista)
m=max(lista)
n=min(lista)
print("Quantidade de numeros digitados na lista -->", qtd)
print("Soma dos valores digitados na lista -->", soma)
print("O maior numero presenta na lista -->", m)
print("O menor numero presenta na lista -->", n)

pesquisa=int(input("Digite o valor que voce queira pesquisar na lista:"))

if pesquisa in lista:
    print(f"O valor {pesquisa} está na lista, na posição --> {lista.index(pesquisa)}")
else:
    print("Esse valor não está na lista")
lista.sort()
print(f"lista em ordem crescente {lista}")
lista.insert(1, 33)
print(lista)
lista.sort()
lista.reverse()
print(f"lista em ordem decrescente {lista}")
media=sum(lista)/len(lista)
print(f"A media aritimética {media:.3f}")
lista.remove(33)
c=0
for o in lista:
    if o>10:
        c+=1
print(f" tem {c} elementos maior que 10")
percentual=(c*100)/len(lista)
print(f"{percentual:.2f}% é maior que 10")
print(lista)