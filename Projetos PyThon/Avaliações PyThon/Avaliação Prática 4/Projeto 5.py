ct=0
inc=int(input("digite ate qual numero devo contar: "))
for c in range(inc,-1,-1):
    ct+=1
    if c==0:
        print(f"{c}.",end="")
    else:
        print(f"{c},", end="")
print(f"\nquantidade de numeros: {ct}.")
