def maximo(a, b):
    if a>b:
        return a
    else:
        return b

def minimo(a, b):
    if a<b:
        return a
    else:
        return b
if __name__ == '__main__':

    n1=int(input("Digite o primeiro valor:"))
    n2=int(input("Digite o segundo valor:"))
    print("Maior numero --->", maximo(n1, n2))

    n1=int(input("Digite o primeiro valor:"))
    n2=int(input("Digite o segundo valor:"))
    print("Menor numero --->", minimo(n1, n2))
