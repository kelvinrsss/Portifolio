def soma(n1,n2,n3):
    soma=n1+n2+n3
    return soma
if __name__=='__main__':
    n1=int(input('digitee um valor:'))
    n2=int(input('digite outro valor:'))
    n3=int(input('digite mais um valor:'))
    print(f'a soma dos 3 valores digitados e {soma(n1,n2,n3)}')