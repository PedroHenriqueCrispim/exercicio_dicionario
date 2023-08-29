dicionarios_dados_alunos={}

for i in range(5):
    ra = int(input("Digite o RA do aluno: "))
    notas = []
    for i in range(3):
            nota = float(input(f"Digite a nota {i+1} dos alunos: "))
            notas.append(nota)
    dicionarios_dados_alunos[ra] = notas

print(dicionarios_dados_alunos)

for ra, notas in dicionarios_dados_alunos.items():
      media = sum(notas) / len(notas)
      print(f"Media do aluno de RA {ra}: {media:2f}")
      