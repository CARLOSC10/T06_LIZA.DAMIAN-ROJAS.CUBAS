#CONDICIONAL MULTIPLE QUE CALCULA EL AREA DE TRAPECIO
import os
Base_mayor,Base_menor,altura=0,0,0

#ARGUMENTOS
Base_mayor=int(os.sys.argv[1])
Base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#PROCESSING
area_trapecio=((Base_mayor+Base_menor)/2*altura)

#OUTPUT
print("##########################################")
print("#           AREA DEL TRAPECIO            #")
print("##########################################")
print("# BASE MAYOR:    ",Base_mayor,"           ")
print("# BASE MENOR:    ",Base_menor,"           ")
print("# ALTURA:        ",altura,"               ")
print("# AREA TRAPECIO: ",area_trapecio,"        ")
print("##########################################")

#CONDICIONAL MULTIPLE
#SI EL AREA DEL TRAPECIO ES >120
if (area_trapecio > 120):
    print("AREA DEL TRAPECIO ES MAYOR QUE 120")

#SI AREA DEL TRAPECIO ES >=500 Y <800 EL TRAPECIO ES MAXIMO
if (area_trapecio >=500 and area_trapecio < 800):
    print("AREA DEL TRAPECIO MAXIMO")

#SI EL AREA DEL TRAPECIO <50 EL TRAPECIO ES MINIMO
if (area_trapecio < 50):
    print("AREA DE TRAPECIO MINIMO")
#fin_if

