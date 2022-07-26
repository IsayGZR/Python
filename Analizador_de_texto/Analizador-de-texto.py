texto = input("Introduce un texto cualquiera: ")
letras = []
texto = texto.lower()

print("\nIngrese la letras a buscar en el texto que ingreso: \n")
letras.append(input("Ingresa la primera letra: ".lower()))
letras.append(input("Ingresa la segunda letra: ".lower()))
letras.append(input("Ingresa la tercera letra: ".lower()))

print("\nCANTIDAD DE LETRAS")
cantidad_letras1=texto.count(letras[0])
cantidad_letras2=texto.count(letras[1])
cantidad_letras3=texto.count(letras[2])

print(f"Se ha enctrado la letra \"{letras[0]}\", repetida {cantidad_letras1} veces")
print(f"Se ha enctrado la letra \"{letras[1]}\", repetida {cantidad_letras2} veces")
print(f"Se ha enctrado la letra \"{letras[2]}\", repetida {cantidad_letras3} veces")

print("\nCANTIDAD DE PALABRAS")
palabras=texto.split()
print(f"Se tienen \"{len(palabras)}\" palabras en el texto")

print("\nLETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra del inicio del texto ingresado es: \"{letra_inicio}\" y la letra del final es: \"{letra_final}\"")

print("\nTEXTO INVERTIDO")
palabras.reverse()
texto_invertido=' '.join(palabras)
print(f"El texto inertido quedaría: \"{texto_invertido}\"")

print("\nBuscando la palabra 'Python' en el texto")
buscar_python = "Python".lower() in texto
dic = {True:"Si",False:"No"}
print(f"La palabra Python \"{dic[buscar_python]}\" se encuentra en el texto")

