"""
scrivere un programma che:

chieda all'utente la distanza percorsa (in m) e il tempo impiegato (in h).
valcola la velocità media.
stampa il risultato con due cifre decimali e indica l'unità di misura.

"""

distanza=input("inserire la distanza in chilometri")
distanza=float(distanza)
tempo=input("inserire il tempo impiegato in ore")
tempo=int(tempo)
velocita=distanza/tempo
velocita=round(velocita,2)
print(velocita)