n1=float(input('digite um valor:'))
n2=float(input('digite outro valor:'))
s=input('voce deseja -,+,/,*:')
somar= n1+n2
dividir=n1/n2
multiplicar=n1*n2
subtrair=n1-n2
if somar == '+':
    print('a soma dos numeros e {}'.format(somar))
elif subtrair == "-":
    print('o valor da subtracao e {}'.format(subtrair))
elif multiplicar=="*":
    print('o valor da multiplicao e {}'.format(multiplicar))
elif multiplicar=='/':
    print('o valor da divisao e {}'.format(dividir))