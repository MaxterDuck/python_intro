#Ejemplo de ejercicio 
num=int(input("Dame 4 numeros para sumarlos"))
if num >= 1000 and num <=9999:
    num_str=str (num)
    suma=0 
    for digito in num_str:
        suma += int(digito)
    print ("La suma es igual a: ",suma) 
else:
    print("El numero no tiene 4 cifras")
