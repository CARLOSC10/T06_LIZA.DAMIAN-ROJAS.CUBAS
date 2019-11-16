#CONDICIONAL MULTIPLES CALCULA SI INGRESA A LA UNPRG
import os
alumno,puntos_algebra,puntos_fisica,puntos_geometria="",0,0,0

#ARGUMENTOS
alumno=os.sys.argv[1]
puntos_algebra=int(os.sys.argv[2])
puntos_fisica=int(os.sys.argv[3])
puntos_geometria=int(os.sys.argv[4])

#PROCESSING
resultados=round(puntos_algebra+puntos_fisica+puntos_geometria)

#OUTPUT
print("###########################################")
print("         INGRESO A LA UNIVERSIDAD          ")
print("###########################################")
print("ALUMNO:              ",alumno,"            ")
print("PUNTOS DE ALGEBRA:   ",puntos_algebra,"    ")
print("PUNTOS DE FISICA:    ",puntos_fisica,"     ")
print("PUNTOS DE GEOMETRIA: ",puntos_geometria,"  ")
print("RESULTADOS DE EXAMEN:",resultados,"        ")
print("###########################################")

#CONDICIONAL MULTIPLES
#SI EL ALUMNO SACA UN PUNTAJE >80 PUNTOS INGRESA A LA UNPRG
if (resultados > 80):
    print("INGRESA A LA UNPRG")

#SI EL ALUMNO SACA UN PUNTAJE >=95 Y <=100 INGRESA CON UN PUNTAJE MAYOR
if (resultados >=95 and resultados <=100):
    print("INGRESA CON UN PUNTAJE MAYOR SACO EL COMPUTO")

#SI EL ALUMNO SACA UN PUNTAJE <=30 NO INGRESA
if (resultados <= 30):
    print("NO ALCANZO VACANTE A LA UNPRG")
#fin_if
