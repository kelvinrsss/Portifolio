def mesagem_numero(mesagem,numero):
    print('mesagem:',mesagem)
    print('numero',numero)
def main():
    mesagem=input('digite uma mensagem:')
    numero=float(input('digite um numero:'))
    mesagem_numero(mesagem,numero)
if __name__=="__main__":
    main()
