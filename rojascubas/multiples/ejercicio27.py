import os
#mostrar un mensaje en una boleta de centro comercial de poder ingresar a un sorteo de un electrodomestico con compras mayores a S/200
print("")
#declararación de variables
nombre_cliente,dinero_consumido,nombre_centro_comercial,a="",0.0,"",""

#input
nombre_cliente=(os.sys.argv[1])
nombre_centro_comercial=(os.sys.argv[2])
dinero_consumido=float(os.sys.argv[3])

#processing
if(dinero_consumido>0 and dinero_consumido<100.0):       #condicion:si el dinero consumido es mayor cero y menor que cero  mostrar un mensaje
    a="poco consumo"      #asigna un mensaje en la variable a

elif(dinero_consumido>200 and dinero_consumido<350):       #condicion:si el dinero consumido es mayor 200 Y MENOR A 350 MOSTRAR UN MENSAJE
    a="moderado consumo"       #condicion:si no ,mostrar un mensaje

elif(dinero_consumido>500.0):  #condicion si el dinero consumido es mayor a 500 mostrar un mensaje
    a="GRAN CONSUMO"           #condicion:si no ,mostrar un mensaje

#fin_si

#output
print("**************************************")
print("*                BOLETA              *")
print("**************************************")
print("*CLIENTE:",nombre_cliente,"                      *")
print("*CENTRO COMERCIAL:",nombre_centro_comercial,"            *")
print("*TOTAL CONSUMIDO:",dinero_consumido,"             *")
print("**************************************")
print(a)
print("**************************************")
