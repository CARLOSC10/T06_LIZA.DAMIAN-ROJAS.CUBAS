#CONDICIONAL MULTIPLES QUE CALCULA LA EDAD DE UNA PERSONA
import os
nombre,anio_nacimiento,anio_actual="",0,0

#ARGUMENTOS
nombre=os.sys.argv[1]
anio_nacimiento=int(os.sys.argv[2])
anio_actual=int(os.sys.argv[3])

#PROCESSING
edad=round(anio_actual - anio_nacimiento)

#OUTPUT
print("######################################")
print("         EDAD DE UNA PERSONA          ")
print("######################################")
print("NOMBRE:           ",nombre,"          ")
print("AÑO DE NACIMIENTO:",anio_nacimiento," ")
print("AÑO ACTUAL:       ",anio_actual,"     ")
print("EDAD:             ",edad,"            ")
print("######################################")

#CONDICIONAL MULTIPLE
#SI SU EDAD ES MAYOR DE 34 AÑOS PORTA DNI AZUL
if (edad > 34):
    print("PUEDE PEDIR UN EMPRESTAMO A CUALQUIER BANCO")

#SI SU EDAD >=18 Y <=100 PUEDE BOTAR EN LA ELECCIONES
if (edad >=18 and edad <=100):
    print("PUEDE BOTAR EN LAS ELECCIONES PRESIDENCIALES")

#SI SU EDAD <18 TODABIA LOS MANDAN SUS PADRES
if (edad < 18):
    print("EL MENOR TODAVIA ESTA AL PODER DE SUS PADRES")
#fin_if
