total_alunos = 0
aprovados = 0
reprovados = 0
while True:
    nota = input("Digite a nota dos alunos e use o comando '-1' para fechar: ")
    if nota == "-1":
        break
    nota = float(nota)
    if nota >= 5:
        aprovados += 1
    else:
        reprovados += 1
    total_alunos += 1
print("Alunos que fizeram a prova:", total_alunos)
print("Alunos aprovados:", aprovados)
print("Alunos reprovados:", reprovados)