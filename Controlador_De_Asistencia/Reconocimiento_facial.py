from cv2 import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file("Isay_1.jpeg")
foto_prueba = fr.load_image_file("Brad_Pitt.jpg")

# Pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_1 = fr.face_locations(foto_control)[0]
cara_codificada_1 = fr.face_encodings(foto_control)[0]
lugar_cara_2 = fr.face_locations(foto_prueba)[0]
cara_codificada_2 = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulos
cv2.rectangle(foto_control,
              (lugar_cara_1[3], lugar_cara_1[0]),
              (lugar_cara_1[1], lugar_cara_1[2]),
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_2[3], lugar_cara_2[0]),
              (lugar_cara_2[1], lugar_cara_2[2]),
              (0, 255, 0),
              2)

# Realizar compracion
resultado = fr.compare_faces([cara_codificada_1], cara_codificada_2, 0.5)


# Medida de distancia
distancia = fr.face_distance([cara_codificada_1], cara_codificada_2)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado}{distancia.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (0,255,0),
            2)


# Mostrar imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)
