"""
stampare lo stato di aggregazione dell'acqua data la sua temperatura in input
"""
temperatura=input("inserire la temperatura dell'acqua")
if temperatura <=0:
    print("lo stato e solido")
elif temperatura >0:
    print("liquido")
else:
    print("gassoso")
        
    
    