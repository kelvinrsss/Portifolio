
def somar(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

def subtrair(a, b):
    resultado = a - b
    print(f"{a} - {b} = {resultado}")

def multiplicar(a, b):
    resultado = a * b
    print(f"{a} x {b} = {resultado}")

def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero não é permitida.")
    else:
        resultado = a / b
        print(f"{a} / {b} = {resultado:.2f}")


if __name__ == '__main__':
    print("=== CALCULADORA ===")
    operador = input("Digite a operação (+, -, x, /): ").strip()
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operador == '+':
        somar(num1, num2)
    elif operador == '-':
        subtrair(num1, num2)
    elif operador in ('x', '*'):
        multiplicar(num1, num2)
    elif operador == '/':
        dividir(num1, num2)
    else:
        print("Operador inválido.")
