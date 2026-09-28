"""
data una lista di 20 elementi di temperature randomiche nell'intervallo -20 +40,
calcolare il numero di elementi sopra lo 0, sotto lo 0 e stampare a video la scritta
freddo estremo se le temperature sotto lo 0 superano quelle sopra, caldo estremo nnell'altro caso
"""
import random
lista=[]

for i in range(0, 20):
    lista.append(random.randint(-20, +40))
    caldoestremo=0
    freddoestremo=0
for i in range (0, 20):
    print(lista[i])
    if lista[i]>0:
        caldoestremo=caldoestremo+1
    else:
        freddoestremo=freddoestremo+1
if freddoestremo>caldoestremo:
    print("freddo estremo")
else:
    print("caldo estremo")