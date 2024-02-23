lista = []
aux =0
while True:
    num = int(input("digite o numero "))
    if num == 999 :
        break
    lista.append(num)
for i in lista :
     if i > aux :
        aux =i
print(aux)