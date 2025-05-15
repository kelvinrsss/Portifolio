def calcule_soma(a, b):
    return a+b

def calcule_subtracao(a, b):
    return a-b

if __name__ == '__main__':

    n1 = int(input("Digite o primeiro valor :"))
    n2 = int(input("Digite o segundo valor :"))

    opcao = int(input("Digite [1] para somar\nDigite [2] para subtrair\n--> "))

    if opcao==1:
        calcule_soma(n1, n2)
        print("a soma dos valores:", calcule_soma(n1, n2))
    elif opcao==2:
        calcule_subtracao(n1, n2)
        print("a subtracao dos valores:", calcule_subtracao(n1, n2))
    else:
        print("não tem essa opcao!!!")