#practica chatgpt.2
from collections import Counter
palabra=input("Dame una palabra")
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letra in palabra: 
    if letra in vocales: 
        vocales[letra] += 1
print("Cantidad de vocales:")
for vocal, cantidad in vocales.items():
    if cantidad > 0:  
        print(f"{vocal}: {cantidad}")
