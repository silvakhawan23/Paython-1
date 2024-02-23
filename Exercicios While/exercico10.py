num1 =1
num2 =0
x= 0
soma =0
while num1 >num2 :
    print("digite n1 maior que n2")
    num1 = int(input("digite o primeiro intervalo "))
    num2= int(input("digite o primeiro intervalo "))

for x in range(num1 +1  ,num2) :
    soma = soma +x
    print(x)
print("A soma do Intervalo é",soma)