import random


# Funcion principal del juego
def jugar():
    while True:
        usuario = input("Escoge\n'r' Para roca (piedra)\n'p' para papel\n't' para tijera\n")
        usuario = usuario.lower()
        maquina = random.choice(['r', 'p', 't'])

        # Comprobamos que elusuario halla elegido un caracter valido
        if usuario == 'r' or usuario == 'p' or usuario == 't':
            if usuario == maquina:
                return f"Usted escogió: {usuario}  y la maquina tambien escogió {maquina} por lo tanto es un EMPATE"

            if victoria(usuario, maquina):
                return f"Usted escogió: {usuario}  y la maquina escogió {maquina} por lo tanto GANO"

            return f"Usted escogió: {usuario}  y la maquina escogió {maquina} por lo tanto PERDIO"

        print("\nNO es valida su entrada. Escoja una opcion valida ")


#  para comprobar si hemos ganado o perdido
def victoria(jugador, opnente):
    if (jugador == 'r' and opnente == 't') or (jugador == 't' and opnente == 'p') or (
            jugador == 'p' and opnente == 'r'):
        return True


opc = 1
while opc == 1:
    print(jugar())
    opc = int(input("Quieres volver a jugar?: 1-SI  2-NO "))

print("\nGracias por jugar")


