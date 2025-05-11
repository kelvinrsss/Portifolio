ct=0
soma=0
menor=0
print('digite 0 para parar o programa.')
while True:

    n1=float(input('digite um numero:'))
    if n1==0:
        break
    if menor <=20:
        menor+=1
    ct = ct + 1
    soma = soma + n1
media = soma / ct
print("os valores maior de 20 sao {}".format(menor))
print('valor total de numero e {}'.format(ct))
print('a soma dos valores e {}'.format(soma))
print('o valor da media arimetmedica {:.2f }'.format(media))