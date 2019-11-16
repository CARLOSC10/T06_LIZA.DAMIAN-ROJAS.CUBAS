#CONDICIONAL DOBLE DE NOTAS DE PROGRAMACION
import os
nota_uno,nota_dos,nota_tres,nota_cuatro=0,0,0,0

#ARGUMENTOS
nota_uno=int(os.sys.argv[1])
nota_dos=int(os.sys.argv[2])
nota_tres=int(os.sys.argv[3])
nota_cuatro=int(os.sys.argv[4])

#PROCESSING
notas_totales=round(nota_uno+nota_dos+nota_tres+nota_cuatro)/4

#OUTPUT
print("###################################")
print("      NOTAS DE PROGRAMACION        ")
print("###################################")
print("# NOTA 01: ",nota_uno,"            ")
print("# NOTA 02: ",nota_dos,"            ")
print("# NOTA 03: ",nota_tres,"           ")
print("# NOTA 04: ",nota_cuatro,"         ")
print("# NOTAS TOTALES: ",notas_totales," ")
print("###################################")

#CONDICIONAL DOBLE
#SI LA NOTA ES MENOR 10.5 ENTONCES ESTA DESAPROVADO
if (notas_totales < 10.5):
    print("ALUMNO DESAPROBADO")
else:
    print("ALUMNO APROBADO")
#fin_if
