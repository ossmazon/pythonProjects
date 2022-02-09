def run():
    pass

jugador1 = """ Bienvenido al juego de piedra, papel o tijera.  🤑

Jugador 1 elige una opcion

piedra 
papel
tijera
:
"""

opcion1 = input(jugador1)
print("tu eleccion fue " + opcion1)        

jugador2 = """

Jugador 2 elige una opcion

piedra 
papel
tijera
:
"""
opcion2 = input(jugador2)
print("tu eleccion fue " + opcion2)

if opcion1 == opcion2:
        print("Empate")


elif opcion1 == "piedra" and opcion2 == "tijera":
        print("Gana jugador 1")   

elif opcion1 == "tijera" and opcion2 == "piedra":
        print("Gana jugador 2")   

elif opcion1 == "papel" and opcion2 == "piedra":
        print("Gana jugador 1")

elif opcion1 == "piedra" and opcion2 == "papel":
        print("Gana jugador 2")

elif opcion1 == "papel" and opcion2 == "tijera":
        print("Gana jugador 2")

elif opcion1 == "tijera" and opcion2 == "papel":
        print("Gana jugador 1")

if __name__ ==  "__main__":
    run()