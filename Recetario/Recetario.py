import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Desktop/GitHub/Python/Recetario/Recetas")


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def inicio():
    system("cls")
    print("*" * 50)
    print("*" * 5 + " BIENVENIDO AL ADMINISTRADOR DE RECETAS " + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total de recetas: {contar_recetas(mi_ruta)}")
    eleccion = " "
    while not eleccion.isnumeric() or int(eleccion) not in range(1, 7):
        print('''
        [1] - Leer Receta
        [2] - Crear Receta Nueva
        [3] - Crear Catgoria Nueva
        [4] - Eliminar Receta
        [5] - Eliminar Categoria
        [6] - Salir Del Programa ''')
        eleccion = input("Elige una opcion: ")
    return int(eleccion)


def mostrar_categoria(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1

    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = "x"
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_recetas(lista):
    eleccion_receta = " "
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")

    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("La siente esa receta ya existe")


def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu receta {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("La siente esa categoria ya existe")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminada")


def volver_incio():
    eleccion_regresar = " "

    while eleccion_regresar.lower() != "a":
        eleccion_regresar = input("\nPresione a para volver al menu: ")


finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_incio()

    elif menu == 2:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_incio()

    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_incio()

    elif menu == 4:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_incio()

    elif menu == 5:
        mis_categorias = mostrar_categoria(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_incio()

    elif menu == 6:
        finalizar_programa = True
