s_pares = 0
s_impares = 0
qt_pares = 0
qt_impares = 0
while True:
    num = int(input("Digite um número (-1 para sair): "))
    if num == -1:
        break
    if num % 2 == 0:
        s_pares += num
        qt_pares += 1
    else:
        s_impares += num
        qt_impares += 1
media_pares = s_pares / qt_pares
media_impares = s_impares / qt_impares
print("A media dos numeros impares são:", media_impares)
print("A media dos numeros pares são:", media_pares)