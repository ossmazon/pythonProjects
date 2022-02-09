import math


def run():
    pass


menu = """ Bienvenido al calculador de volumen
Elige una opcion

1- Cubo o exagono

2- Paralelepipedo o ortoedro

3- Piramide

4- Cilindro

5- Cono

6- Esfera
: """

opcion = int(input(menu))

if opcion == 1:
    print("Elejiste volumen de cubo o exagono")
    lado_cubo = int(input("Introduce un lado del cubo en centimetros: "))
    volumen_cubo = lado_cubo * lado_cubo * lado_cubo
    volumen_cubo = round( volumen_cubo , 4)
    print("El volumen es " + str(volumen_cubo) + " cm3")
    
    

elif opcion == 2:
    print("Elejiste volumne de paralelepipedo o ortoedro")
    lado_ortoedro1 = int(input("Introduce el lado 1 en centimetros: "))
    lado_ortoedro2 = int(input("Introduce el lado 2 en centimetros: "))
    lado_ortoedro3 = int(input("Introduce el lado 3 en centimetros: "))
    volumen_ortoedro = lado_ortoedro1 * lado_ortoedro2 * lado_ortoedro3
    volumen_ortoedro = round( volumen_ortoedro , 4)
    print("El volumen es " + str(volumen_ortoedro) + " cm3")
        

elif opcion == 3:
    print("Elejiste volumen de piramide")
    altura_piramide = int(input("Introduce la altura en centimetros: "))
    base_piramide = int(input("Introduce la base en centimetros: "))
    volumen_piramide = altura_piramide * base_piramide * 1/3
    volumen_piramide = round( volumen_piramide , 4)
    print("El volumen es " + str(volumen_piramide) + " cm3")


elif opcion == 4:
    print("Elejiste volumen de cilindro")
    altura_cilindro = int(input("Introduce la altura en centimetros: "))
    radio_cilindro = int(input("Introduce el radio en centimetros: "))
    volumen_cilindro = math.pi * (radio_cilindro * radio_cilindro) *altura_cilindro
    volumen_cilindro = round( volumen_cilindro , 4)
    print("El volumen es " + str(volumen_cilindro) + " cm3")

elif opcion == 5:
    print("Elejiste volumen de cono")
    altura_cono = int(input("Introduce la altura en centimetros: "))
    radio_cono = int(input("Introduce el radio en centimetros: "))
    volumen_cono = (math.pi * ( radio_cono * radio_cono) * altura_cono)/3
    volumen_cono = round( volumen_cono , 4)
    print("El volumen es " + str(volumen_cono) + " cm3")

elif opcion == 6:
    print("Elejiste volumen de una esfera")
    radio_esfera = int(input("Introduce el radio en centimetros: "))
    volumen_esfera =  (radio_esfera * radio_esfera * radio_esfera) * 4/3 * math.pi
    volumen_esfera = round( volumen_esfera , 4)
    print("El volumen es " + str(volumen_esfera) + " cm3")

  
else:
    print ("Opcion no valida")

if __name__ == "__main__":
    run()