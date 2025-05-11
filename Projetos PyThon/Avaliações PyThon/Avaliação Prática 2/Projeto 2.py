n1=float(input('digite um numero:'))
n2=float(input('digite outro numero:'))
n3=float(input('digite mais um numero:'))
if n1>n2:
    print('o maior valor e {:.0f}'.format(n1))
elif n2>n3:
    print('o numero maior e {:.0f}'.format(n2))
else:
    print('o numero maior e {:.0f}'.format(n3))