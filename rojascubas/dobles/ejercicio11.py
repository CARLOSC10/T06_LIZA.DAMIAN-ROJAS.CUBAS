#condicionales dobles
#1
import os
#promedio de 4 notas del curso de Historia
print("")
#declararación de variables
nota1,nota2,nota3,nota4,promedio,a=0.0,0.0,0.0,0.0,0.0,""

#input
nota1=float(os.sys.argv[1])
nota2=float(os.sys.argv[2])
nota3=float(os.sys.argv[3])
nota4=float(os.sys.argv[4])

#processing
promedio=(nota1+nota2+nota3+nota4)/4

if(promedio>=10.5):      #condición: si el promedio supera los 10.5 mostrar aprobado
    a="Alumno Aprobado"  #asigna un mensaje en la variable a

else:                          #condicion:si no ,mostrar alumno desaprobado
    a="ALUMNO DESAPROBADO"
#fin_if

#output
print("**************************************")
print("*       PROMEDIO DE HISTORIA         *")
print("**************************************")
print("*NOTA1:",nota1,"                        *")
print("*NOTA2:",nota2,"                        *")
print("*NOTA3:",nota3,"                        *")
print("*NOTA4:",nota4,"                        *")
print("*PROMEDIO:",promedio,"                    *")
print("**************************************")
print(a)
print("**************************************")
