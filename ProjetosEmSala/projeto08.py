m_notas = []
print("Digite [-1] para sair")
while True:
    nota = int(input("Digite a nota de um aluno na turma: "))
    if nota == -1:
        break
    m_notas.append(nota)
    print("lista", m_notas)

qtd_alunos = len(m_notas)
soma_notas = sum(m_notas)
media = soma_notas/qtd_alunos

print("A quantidade de alunos -->", qtd_alunos)
print("A média da turma -->", media)

