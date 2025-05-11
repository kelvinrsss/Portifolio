soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
print(f"4. Soma dos números ímpares e múltiplos de 3 de 1 a 500: {soma}\n")


soma = 0
for i in range(1, 501):
    if i % 2 == 0:
        soma += i
print(f"Soma dos números pares de 1 a 500: {soma}")