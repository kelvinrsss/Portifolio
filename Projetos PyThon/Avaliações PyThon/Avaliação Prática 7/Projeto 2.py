def valor_absoluto(numero):
    if numero >= 0:
        return numero
    else:
        return numero *(-1)

if __name__ == '__main__':
    v1= float(input("digite um numero: "))
    print(f" valor retornado: {valor_absoluto(v1)}")
