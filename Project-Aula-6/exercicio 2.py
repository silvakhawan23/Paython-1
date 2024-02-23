dic = {}
while True :
    pessoa= input("\n digite cpf, nome, email e ano de nascimento\n")
    if pessoa == '':
        break
    cpf, nome,email,ano =pessoa.split()
    dic[cpf]=(nome,email,ano)
    print(dic)
    while True :
        entrada= input(f'''vc quer cadastrar uma nova pessoa digite 1 se quiser perguntar digite 2 ''')
        if entrada=='1':
            break
        if entrada == '2':
            aux=input("digite um cpf")
            for i in dic.keys() :
                  if i == aux :
                    print(dic[i])



