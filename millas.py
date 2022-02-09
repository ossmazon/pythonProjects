def run():
    pass


menu = """ Bienvenido al conversor de millas
Elige una opcion

1-Millas a kilometros

2-Kilometros a millas
: """



opcion = int(input(menu))

if opcion == 1:
    print("Elejiste millas a kilometros")
    millas = int(input("Introduce las millas: "))
    resultado_kilometros = millas / 0.62137
    resultado_kilometros = round(resultado_kilometros, 4)
    print("El resultado es " + str(resultado_kilometros) + " kilometros")


elif opcion == 2:
        print("Elejiste kilometros a millas")
        kilometros = int(input("Introduce los kilometros: "))
        resultado_millas = kilometros * 0.62137
        resultado_millas = round( resultado_millas, 4)
        print("El resultado es " + str(resultado_millas) + " millas")

elif opcion != 1 and opcion != 2:
    print ("Opcion no valida")
    

if __name__ == "__main__":
    run()