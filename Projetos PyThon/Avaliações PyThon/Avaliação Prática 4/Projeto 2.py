s=0
for c in range(3,22,3):
    if c==21:
        print(f"{c}.",end="")
    else:
        print(f"{c},",end="")
    s+=c
print(f"\nsoma dos números gerados: {s}")
