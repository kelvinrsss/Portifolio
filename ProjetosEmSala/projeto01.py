def calcule_soma(a, b):
    soma = a+b
    return soma

def calcule_subtracao(a, b):
    subtracao = a-b
    return subtracao

if __name__ == '__main__':

    n1 = int(input("Digite o primeiro valor :"))
    n2 = int(input("Digite o segundo valor :"))

    print(f"teste:1 {n1} e {n2}   saida: soma= {calcule_soma(n1, n2)} e subtracao= {calcule_subtracao(n1, n2)} ")
