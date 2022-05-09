#Elaborar un algoritmo que permita ingresar el número de
#partidos ganados, perdidos y empatados, por ABC club en el
#torneo apertura, se debe de mostrar su puntaje total,
#teniendo en cuenta que por cada partido ganado obtendrá 3
#puntos, empatado 1 punto y perdido 0 puntos.

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("PUNTOS EQUIPO DE FUTBOL")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

ganados = input(int("ingrese los partidos ganardos"))
perdidos = input(int("ingrese los partidos pertidos"))
empatados = input(int("Ingrese partidos empatados"))

puntos_ganados = int(ganados * 3)
puntos_perdidos = int(perdidos * 0)
puntos_empatados = empatados

puntos_totales = puntos_ganados + puntos_perdidos + puntos_empatados

print("los puntos totales del equipo son")
print(int(puntos_totales))

