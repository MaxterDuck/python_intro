#ejercicio 3 
num=int(input("Dame 4 numeros para saber si es par o impar"))
if num >= 1000 and num <=9999:
    if num%2==0:
        print("El numero es par.")
    else:
        print("El numero es impar")
else: 
    print ("El numero no es valido")