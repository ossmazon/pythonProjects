import random


def generar_contrasena():
    mayusculas = [ "G", "A", "LL", "E", "T", "A"]
    minusculas = ["g", "a", "ll", "e", "t", "a"]
    simbolos = ["!", "#", "$", "%", "&"]
    numeros = [ "1", "9", "9", "3"]

    caracteres = mayusculas + minusculas + simbolos + numeros


    contrasena = []

    for i in range(20):
        caracter_random = random.choice (caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena



def run():
    contrasena = generar_contrasena()
    print("Tu nueva contrasena es: " + contrasena)

if __name__ == "__main__":
    run()