import os
#comparar la cantidad de volumen de un paralelepipedo
#Declaración de variables
lado1,lado2,lado3,volumen,a=0.0,0.0,0.0,0.0,""

#input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])

#processing
volumen=lado1*lado2*lado3
if(volumen>0 and volumen<100.0):   #condicion:si el volumen es mayor que cero y menor a 100 mostrar un mensaje
    a="POCA CANTIDAD DE VOLUMEN"     #se agrega un valor a la variable a

elif(volumen>100.0 and volumen<350.0):        #condicion:si el volumen es mayor que 100 y menor a 350 mostrar un mensaje
    a="MODERADA CANTIDAD DE VOLUMEN"          #se agrega un valor a la variable a

elif(volumen>350.0):                         #condicion:si el volumen es mayor que 350
    a="GRAN CANTIDAD DE VOLUMEN"             #se agrega un valor a la variable a



#fin_if

#output
print("**************************************")
print("*    VOLUMEN DE PARALELEPIPEDO       *")
print("**************************************")
print("*LADO1:",lado1,"                        *")
print("*LADO2:",lado2,"                        *")
print("*LADO3:",lado3,"                       *")
print("*volumen:",volumen,"                   *")
print("**************************************")
print(a)
print("**************************************")
