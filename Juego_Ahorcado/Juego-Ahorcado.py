from random import choice

palabras = ["hola","como","estas","carritos"]
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabra):
    palabra_elegida = choice(lista_palabra)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = " "
    es_valido = False
    abecedario = "abcdefghijklmnñopqrstuvwxyz"

    while not es_valido:
        letra_elegida = input("Ingresa un letra: ")
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valido = True
        else:
            print("Has elegido una letra incorrecta")
    return letra_elegida


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append("_")
    print(" ".join(lista_oculta))


def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin = False

    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -=1
    if vidas == 0:
        fin = perder()
    elif coincidencias == letra_unicas:
        fin= ganar(palabra_oculta)
    return vidas, fin ,coincidencias


def perder():
    print("\nTe has quedado sin vidas")
    print(f"\nLa palabra era: {palabra}")
    return True


def ganar(palabra_descubierta):
    print("\nFelicitaciones has encontrado la palabra!!!!!")
    mostrar_nuevo_tablero(palabra_descubierta)

    return True


palabra, letra_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*" * 30 + "\n")
    mostrar_nuevo_tablero(palabra)
    print("\n")
    print("Letras incorrectas: "+" ".join(letras_incorrectas))
    print(f"Vidas: {intentos}")
    print("\n" + "*" * 30 + "\n")
    letra =pedir_letra()

    intentos,terminado,aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado




