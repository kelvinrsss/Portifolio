def horas_para_minutos_2 (n1, n2):
    v = n1 * 60
    b = v + n2
    print("Resultado:", b)


if __name__ == '__main__':
    n1 = int(input("Digite horas:"))
    n2 = int(input("Digite minutos:"))
    r = horas_para_minutos_2(n1, n2)
