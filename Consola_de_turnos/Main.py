import numeros


def preguntar():

    print("Bienvido a farmacias Python")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["F", "P", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():
    cambiar = True
    while cambiar:
        preguntar()
        try:
            otro_turno = input("¿Quiere otro turno?\nSi - [S]\nNo - [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()


