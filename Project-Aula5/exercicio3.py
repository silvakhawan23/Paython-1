palavra=['a','a','a','a','f','f','h','h','h' ,'h','y','y']
dic ={}
for i in palavra :
    if i in list(dic.keys()):


        dic[i] +=1
    else :
        dic[i]= 1

print(dic)
