n1=int(input(' Digite o valor inicial em °F: '))
n2=int(input('Digite o valor final em °F:'))
print("Fahrenheit | Celsius")
if n1<=n2:
    for f in range(n1, n2 + 1):
        c = (5 * (f - 32)) / 9
        print(f"{f:.1f} °F | {c:.3f} °C")
else:
    for f in range(n1, n2 - 1, -1):
        c = (5 * (f - 32)) / 9
        print(f"{f:.1f} °F | {c:.3f} °C")
print("\n")