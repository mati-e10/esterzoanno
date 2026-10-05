#esercizio1 matematica
import math
coefficenti=[(1,-3,2),(1,2,1),(2,1,3)]
prima=coefficenti[0]
a=prima[0]
b=prima[1]
c=prima[2]


delta=b**2-4*a*c
if delta>0:
        x1=(-b+math.sqrt(delta))/2*a
        x2=(-b-math.sqrt(delta))/2*a
        tipo="due soluzioni distinte"
        soluzioni={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzioni":str(x1)+""+ str(x2)}
elif delta==0:
        x=-b/(2*a)
        tipo="due soluzioni ugulai"
        soluzioniuno={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzione":str(x)}
else:
        x=0
        tipo="soluzione uguale a 0"
        soluzionidue={"a":a,"b":b,"c":c,"delta":delta,"tipo":tipo,"soluzioni":str(x)}
print(soluzioni)
with open ("soluzioni.txt", "w") as fw:
    fw.write("soluzioni")
    fw.write("\n")
    fw.write("soluzioniuno")
    fw.write("\n")
    fw.write("soluzionidue")
    fw.write("\n")

    

    

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
