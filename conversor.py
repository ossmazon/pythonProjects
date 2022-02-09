def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos"+ tipo_pesos + "tienes?:")
    pesos = float (pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")


menu = """ Bienvenido al conversor de monedas  🤑
Elige una opcion
1-Pesos colombianos a Dolares
2-Pesos mexicanos a Dolares
3-Dolares a pesos Mexicanos
Elige una opcion: """

opcion = int(input(menu))
if opcion == 1:
    conversor(" Colombianos ", 3875)

elif opcion == 2:
    conversor(" Mexicanos ", 20)

elif opcion == 3:
    dolares = input ("Cuantos dolares tienes?")
    dolares = float(dolares)
    valor_peso = 0.050
    pesos = dolares / valor_peso
    pesos = str(pesos)
    print("Tienes $" + pesos + "pesos")

else:
    print("Elige alguna opcion")