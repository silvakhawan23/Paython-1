cadastro ={ }

while True :

    nome= (input
           (f'''    
        digite o nome e o tipo sanguineo
                ou
        digite 's' para sair
                     
                          '''))
    if nome == 's':
        break
    nome , tipoaguineo = nome.split()
    cadastro[nome]= tipoaguineo

print(cadastro)