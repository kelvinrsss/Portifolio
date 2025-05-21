def positivo_nulo_negativo(numero):
    if numero == 0:
        print("valor nulo")
    elif numero > 0:
        print("valor positivo")
    else:
        print("valor negativo")

if __name__ == '__main__':
    num=float(input("digite um numero: "))
    positivo_nulo_negativo(num)
