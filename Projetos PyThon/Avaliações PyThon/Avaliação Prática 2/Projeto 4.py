n1=float(input('digite um lado do triangulo:'))
n2=float(input('digite outro lado do triangulo:'))
n3=float(input('digite outro lado do triangulo:'))
if n1==n2==n3:
    print('o triangulo e equilátero.')
elif n1==n2:
    print('o triangulo e isósceles.')
elif n2==n3:
    print('o triangulo e isósceles.')
elif n1==n3:
    print('o triangulo e isósceles.')
else:
    print('o triangulo e escaleno.')