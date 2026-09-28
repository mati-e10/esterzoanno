#dizionari
diz= {"enzimaA":12,"enzimaB":16, "enzimaC":2}
#accede singolo elemnto
print(diz["enzimaB"])
diz["enzimaC"]=2314
#scorrere dizzionario
for key, value in diz.items():
    print(key)
    print(value)