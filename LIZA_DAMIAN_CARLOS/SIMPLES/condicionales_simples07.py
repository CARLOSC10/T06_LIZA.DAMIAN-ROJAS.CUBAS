#CONDICIONAL SIMPLE QUE CALCULA EL AREA DE TRAPECIO
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

#CONDICIONAL SIMPLE
#SI EL AREA DEL TRAPECIO ES >150
if (area_trapecio > 150):
    print(" EL AREA DEL TRAPECIO ES MAYOR QUE 150")
#fin_if


