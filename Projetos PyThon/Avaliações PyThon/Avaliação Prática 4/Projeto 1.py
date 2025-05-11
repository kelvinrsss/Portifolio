ct=0
for c in range(1,14,2):
    if c==13:
        print(f"{c}.",end="")
    else:
        print(f"{c},",end="")
    ct+=1
print(f"\nquantidade de números da sequência: {ct}")
