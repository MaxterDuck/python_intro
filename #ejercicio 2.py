#ejercicio 2 
num=int(input("Dame 4 numeros cifras"))
digito=int(input("Dame un digito en especifico para mostrarte cuantas veces aparece"))
if num >= 1000 and num <=9999:
    num_str=str (num)
    contador=0
    for d in num_str:
        if d == digito:
            contador+=1
    print(f"El digito {digito} aparece {contador} veces en el numero {num}. ")
else:
    print("El numero no es valido ")