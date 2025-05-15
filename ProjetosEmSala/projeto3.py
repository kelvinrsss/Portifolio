def calcule_soma(a, b):
    return a+b

def calcule_subtracao(a, b):
    return a-b

if __name__ == '__main__':

    n1 = int(input("Digite o primeiro valor :"))
    n2 = int(input("Digite o segundo valor :"))

    opcao = (input("Digite [+] para somar\nDigite [-] para subtrair\n--> "))

    if opcao=="+":
        calcule_soma(n1, n2)
        print("a soma dos valores:", calcule_soma(n1, n2))
    elif opcao=="-":
        calcule_subtracao(n1, n2)
        print("a subtracao dos valores:", calcule_subtracao(n1, n2))
    else:
        print("não tem essa opcao!!!")