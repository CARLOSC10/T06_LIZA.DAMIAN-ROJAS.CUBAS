#CONDICIONAL SIMPLE QUE CALCULA LA EDAD DE UNA PERSONA
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

#CONDICIONAL SIMPLE
#SI SU EDAD ES MAYOR DE 18 AÑOS PORTA DNI AZUL
if (edad >= 18):
    print("TIENE DNI AZUL")
#fin_if
