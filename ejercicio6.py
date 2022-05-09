#Se necesita elaborar un algoritmo que solicite el
#número de respuestas correctas, incorrectas y en blanco,
#correspondientes a postulantes, y muestre su puntaje final
#considerando que por cada respuesta correcta tendrá
#3 puntos, respuestas incorrectas tendrá -1 y respuestas en
#blanco tendrá 0.

print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("respuestas correctas, incorrectas y en blanco")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")

respuestas_correctas =  int(input("ingrese las respuestas correctas: "))
respuestas_incorrectas = int(input("ingrese las respuestas incorrectas: "))
respuestas_en_blanco = int(input("ingrese las respuestas en blanco: "))

puntos_respuestas_correctas = int(respuestas_correctas * 3)
puntos_respuestas_incorrectas = int(respuestas_incorrectas * -1)

print("los puntos totales de su examen es")
total_puntos_respuestas = (puntos_respuestas_correctas + puntos_respuestas_incorrectas)
print(int(total_puntos_respuestas))



