# Letras del nombre
from collections import Counter
nombre = input("Dame tu nombre")
conteo = Counter(nombre.lower())
print ("Cantidad de letras: ")
for letra,cantidad in conteo.items():
    print (f"{letra}: {cantidad}")
