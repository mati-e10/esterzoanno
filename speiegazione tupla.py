#tupla (struttura dati diversa dalla lista ma simile)
mytuple=(3,6,8)
#stampare primo elemnto tupla
print(mytuple[0])
#stamapre tutti gli elementi della tupla
for i in range (0,len(mytuple)):
                print (mytuple[i])
#modificare elemnto della tupla
#mytuple[0]=2
#asseganamento non permesso
mytuple_list=list(mytuple)
mytuple_list[0]=2
mytuple=tuple(mytuple_list)
