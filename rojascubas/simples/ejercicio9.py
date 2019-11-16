import os
#omprobar si el volumen de un paralelepipedo si es mayor que cero en caso que sea negativo o cer mostrar un mensaje
#Declaración de variables
lado1,lado2,lado3,volumen,a=0.0,0.0,0.0,0.0,""

#input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])

#processing
volumen=lado1*lado2*lado3
if(volumen<=0):
    a="EL VOLUMEN ES INCORRECTO"
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
