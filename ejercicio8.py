#Si tengo una cantidad de Soles, dar su equivalente en dólares
#y después en euros. Se sabe que 1 dólar =3.25 soles y 1
#euro=3.83 soles.

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Valor de la moneda Dolar en soles y euros")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

sol = float(input("Ingrese la cantidad de Soles a calcular:  "))

valor_sol_a_dolar = float((1 * sol)/3.25 )
redondeado = round(valor_sol_a_dolar, 2)

valor_sol_a_euros = float((1 * sol)/3.83 )
redondeado1 = round(valor_sol_a_euros, 2)

print("De Soles a Dolares")
print(redondeado)

print("De Soles a euros")
print(redondeado1)




