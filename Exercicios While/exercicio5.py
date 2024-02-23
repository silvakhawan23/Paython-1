x=1
y=1
z=1
s=1
e=1

while x==1:

    nome= input('digite seu nome com mais de 3 carcteres \n')
    qtd=len(nome)
    if qtd < 4 :
        print('parece que é besta, digita de  novo irmao  \n')
    else :
        x=2

while y ==1 :
    idade= int(input('digite sua idade \n'))
    if idade < 0 and idade >150 :
        print('idade invalida \n')
    else :
        y=2
while z==1 :
    salario = float(input('digite seu salario \n '))
    if salario <=0 :
        print('igita outro\n')
    else :
        z =2
while s==1 :

    sexo = input( "sexo, m para masculino, f para feminino \n"
                  "")
    if sexo != 'm'or sexo!= 'f' :
        print('incorreto escreva m ou f \n')
    else:
        s=2
while e==1 :
    estado= input('s- solteiro \n c- casado \n v- viuvo\n d-nao sei ')
    if estado != s or estado != c or  estado != v or  estado != d :
        print("invalido digite novamente\n")
    else :
        e=2
