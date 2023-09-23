# Escreva um programa que solicita o nome de alunos e respecivas notas de 4 provas
# No final ele imprimir o nome dos alunos e media


nome_alunos = [] 
notas_alunos = []

while True:
    adicionarAluno = int(input("Digite (1) para Adicionar Aluno ou (2) para Sair: "))
    if adicionarAluno == 1 :
        nomeAluno = input("Escreva o nome do aluno: ")
        notaP1 = float(input("Escreva a nota da P1: "))
        notaP2 = float(input("Escreva a nota do P2: "))
        notaP3 = float(input("Escreva a nota da P3: "))
        notaP4 = float(input("Escreva a nota da P4: "))
        media = (notaP1 + notaP2 + notaP3 + notaP4) / 4
        adicionarAluno = int(input("Deseja adicionar mais Alunos: (1) para SIM ou (2) para NÃO: "))

        nome_alunos.append(nome_alunos)
        notas_alunos.append(media)

    elif adicionarAluno == 2:
        for i in nome_alunos:
            print(i)
        break
    else: 
        print("opção invalida! ")
       




