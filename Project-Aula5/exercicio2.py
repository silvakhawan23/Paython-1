dic = {}
while True :
    opc= input(f'''
    Digite 1 para acrecentar um produto "
    Digite s para fechar
          ''')
    if opc == '1':
        item=input('item\n')
        dic[item]=input('digite a quantidade\n')

    if opc == 's':
        break

print(dic)
