ct=0
fin=int(input("digite ate qual numero devo contar: "))
for c in range(1,fin+1):
    ct+=1
    if c==fin:
        print(f"{c}.",end="")
    else:
        print(f"{c},", end="")
print(f"\nquantidade de numeros: {ct}.")
