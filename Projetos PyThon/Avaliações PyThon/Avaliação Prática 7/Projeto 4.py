def fator(n=1, show=True):
    f = 1
    if n < 0:
        return "O fatorial não é definido para números negativos."

    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('= ', end='')
        f *= c
    return f


numero = int(input("Digite um número: "))
print(fator(numero))
