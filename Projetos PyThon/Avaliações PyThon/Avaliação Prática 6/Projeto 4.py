def calcular_desconto(preco,percentual):
    desconto = preco * (percentual/100)
    desconto_final=preco-desconto
    return desconto_final
if __name__=='__main__':
    nome_produto=input('digite o nome do produto:')
    preco=float(input('digite o preco do produto'))
    percentual=float(input('digite o percentual de desconto:'))
    print(f'o {nome_produto} fica com o total de desconto de {calcular_desconto(preco,percentual)}')