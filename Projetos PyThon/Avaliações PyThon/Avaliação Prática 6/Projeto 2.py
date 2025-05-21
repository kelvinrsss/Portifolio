def calculo(valor,ano):
    retorno=ano-valor
    return retorno
def main():
    n1=int(input('digite o ano que voce nasceu:'))
    n2=int(input('digite o ano que voce esta:'))
    print(calculo(n1,n2))
if __name__=='__main__':
    main()
    print(main)