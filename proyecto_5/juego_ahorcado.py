from random import choice

# VARIABLES
lista_palabras = ["elefante", "murcielago", "astronauta", "biblioteca", "camaleon", "dinosaurio", "escalera", "futbol", "guitarra", "hipopotamo"]
palabra = choice(lista_palabras)
letras_usadas = []
vidas = 6
aciertos = 0
fin_juego = False

# FUNCIONES
def mostrar_guiones(palabra):
    for letra in palabra:
        if letra in letras_usadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def pedir_letra():
    while True:
        letra = input("Escribe una letra: ")
        if validar_letra(letra):
            return letra

def validar_letra(letra):
    if not letra.isalpha():
        print("Por favor, introduce solo letras")
        return False
    if len(letra) != 1:
        print("Por favor, introduce solo una letra")
        return False
    return True

def chequear_letra(letra, palabra, vidas, aciertos):
    if letra not in palabra:
        vidas -= 1
        if letra not in letras_usadas:
            letras_usadas.append(letra)
        print("La letra elegida no estaba en la palabra, pierdes 1 vida")
    else:
        if letra not in letras_usadas:
            letras_usadas.append(letra)
            aciertos += palabra.count(letra)
            print("Has acertado una letra")
        else:
            vidas -= 1
            print("La letra elegida está repetida, pierdes 1 vida")

    print(f"Te quedan: {vidas} vidas. Letras usadas: {letras_usadas}")
    return vidas, aciertos

def condicion_ganadora(vidas, aciertos):
    if vidas == 0:
        print("Se te han acabado las vidas, has perdido. La palabra era:", palabra)
        return True
    elif aciertos == len(palabra):
        print("Has acertado la palabra, has ganado")
        return True
    return False

# BUCLE PRINCIPAL
while not fin_juego:
    mostrar_guiones(palabra)
    letra = pedir_letra()
    vidas, aciertos = chequear_letra(letra, palabra, vidas, aciertos)
    print()
    fin_juego = condicion_ganadora(vidas, aciertos)