import os
#comprobar si el cliente ingresa el monto total del costo de un celular comprado
#Declaracion de variables
monto_ingresado,nombre_cliente,marca_celular,nombre_tienda,DNI,a=0.0,"","","",0,""

#input
monto_ingresado=float(os.sys.argv[1])
nombre_cliente=os.sys.argv[2]
marca_celular=os.sys.argv[3]
nombre_tienda=os.sys.argv[4]
DNI=os.sys.argv[5]

#processing
if(monto_ingresado==400.0):         #CONDICION:si el monto ingresado es igual a 400.0 mostrar un mensaje
    a="PAGO CANCELADO"              #se asigna un valor a la variable a

elif(monto_ingresado<400.0):        #CONDICION:si el monto ingresado es menor a 400.0 mostrar un mensaje
     a="PAGO INCOMPLETO"            #se asigna un valor a la variable a

elif(monto_ingresado>400.0):        #CONDICION:si el monto ingresado es mayor a 400.0 mostrar un mensaje
    a="PAGO INCORRECTO"             #se asigna un valor a la variable a

#fin_if

#output
print("**************************************")
print("*        COMPROBACION DE DATOS       *")
print("**************************************")
print("*CLIENTE:",nombre_cliente,"                      *")
print("DNI:",DNI,"                            *")
print("*CELULAR:",marca_celular,"                    *")
print("*TIENDA:",nombre_tienda,"                    *")
print("*MONTO:",monto_ingresado,"                     *")
print("**************************************")
print(a)
print("**************************************")
