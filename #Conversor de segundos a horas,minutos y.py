#Conversor de segundos a horas,minutos y segundos
segundos_totales=int(input("Dame una cantidad de segundos"))
hora=3600
minuto=60
hora=segundos_totales //3600
segundos_restantes=segundos_totales%3600
minuto=segundos_restantes//60 
segundos_finales=segundos_restantes%60
print (f"{segundos_totales}segundos son {hora} horas,{minuto}minutos y {segundos_finales}segundos.")
