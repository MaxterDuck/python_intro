#Conversor de minutos a días y horas
minutos_totales =int(input("Dame una cantidad de minutos"))
dias=minutos_totales//1440 
minutos_restantes=minutos_totales%1440 
horas = minutos_restantes // 60
minutos_finales = minutos_restantes % 60
print(f"{minutos_totales} minutos son {dias} días, {horas} horas y {minutos_finales} minutos.")


