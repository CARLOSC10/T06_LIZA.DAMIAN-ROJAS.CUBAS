import os
#comprobar si el volumen de un paralelepipedo si es mayor que cero en caso que sea negativo o cero mostrar un mensaje
#Declaración de variables
lado1,lado2,lado3,volumen,a=0.0,0.0,0.0,0.0,""

#input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])

#processing
volumen=lado1*lado2*lado3
if(volumen<=0):
    a="EL VOLUMEN ES INCORRECTO"      #condicion:si el volumen es menor o igual que cero mostrar un mensaje de error

else:
    a="EL VOLUMEN ES CORRECTO"        #condicion:si no, mostrar el volumen es correcto
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
