#Extraer dígitos de un número de 4 cifras
num = int(input("Dame un numero de 4 cifras"))
if num >= 1000 and num <=9999: 
    num_str=str(num)
    print (num_str[0], num_str[1], num_str[2], num_str[3], sep=",") 
else:
    print ("Lo siento,El numero no es valido :( ")
