#Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.
costo=float(input("Cuanto valio la comida"))
total=0
print ("Que porcentaje de propina quieres dar")
print ("1. 10 porciento de propina ")
print ("2. 15 porciento de propina ")
print ("3. 20 porciento de propina")
opcion =int (input()) 
if opcion==1:
    total=costo+(costo*0.10) 
    print ("Muchas gracias,el valor total a pagar es con el 10% de propina es: ",total)
elif opcion==2:
    total=costo+(costo*0.15) 
    print ("Muchas gracias,el valor total a pagar es con el 15% de propina es: ",total)
elif opcion==3:
    total=costo+(costo*0.20) 
    print ("Muchas gracias,el valor total a pagar es con el 20% de propina es: ",total)
else: 
    print ("Opcion incorrecta")