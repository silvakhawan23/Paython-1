lista = {}
lista2 = {}

while True :
    menu = int(input("digite 1- cadastrar usuario\n digite 2- fazer login \n digite 3- sair\n"))
    if menu == 1:
        lista = input("digite seu usuario  \n ")
        lista = input("digite sua senha  \n ")

    if menu == 3 :
        break
    if menu == 2 :
        lista2 = input("digite seu usuario \n")
        lista2 = input("digite seu senha \n")

        if lista2 == lista :
            print("login aceito \n")
        else :
            print("login negado \n ")




