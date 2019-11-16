import os
#promedio de 4 notas del curso de Historia (calificar el promedio)
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

if(promedio<=10.5):      #condición: si el promedio supera los 10.5 mostrar un mensaje
        a="PROMEDIO BUENO"       #asigna un valor en la variable a

elif(promedio>=10.5 and promedio<15):        #condición: si el promedio supera los 10.5 y menor que 15 mostrar un mensaje
    a="PROMEDIO BUENO"                        #asigna un valor en la variable a

elif(promedio>15 and promedio<=20):           #condición: si el promedio supera los 15 y menor o igual a 20 mostrar un mensaje
    a="PROMEDIO EXCELENTE"                    #asigna un valor en la variable a
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
