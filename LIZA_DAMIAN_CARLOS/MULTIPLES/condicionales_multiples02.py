#CONDICIONAL MULTIPLE DE NOTAS DE PROGRAMACION
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
print("       NOTAS DE PROGRAMACION       ")
print("###################################")
print("# NOTA 01: ",nota_uno,"            ")
print("# NOTA 02: ",nota_dos,"            ")
print("# NOTA 03: ",nota_tres,"           ")
print("# NOTA 04: ",nota_cuatro,"         ")
print("# NOTAS TOTALES: ",notas_totales," ")
print("###################################")

#CONDICIONAL MULTIPLE
# SI NOTA ES MAYOR A 10.5 ENTONCES ESTA APROVADO
if (notas_totales > 10.5):
    print("ALUMNO APROBADO")

# SI NOTA ES >=7 Y <=10 ENTONCES PUEDE DAR EL SUSTI
if (notas_totales >=7 and notas_totales <=10):
    print("EL ALUMNO VA DAR RECUPERACION DE EXAMEN DE SUSTI")

# SI NOTA ES MAYOR A 17 TIENE EXELENTE NOTA
if (notas_totales > 17):
    print("ALUMNO CON EXELENTE NOTA")
#fin_if

