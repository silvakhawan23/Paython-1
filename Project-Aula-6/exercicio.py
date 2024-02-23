alunos=[]
while True :
    aluno= input(" digite o nome o email e sua data de nascimento")
    if aluno == '':
         break
    nome ,email,nascimento= aluno.split()
    alunos.append((nome,email,nascimento))
for aluno in alunos :
    print(aluno)
