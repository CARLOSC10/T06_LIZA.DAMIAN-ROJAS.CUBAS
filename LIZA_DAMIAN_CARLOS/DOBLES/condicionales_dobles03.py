#CONDICIONAL DOBLE DE BOLETA DE VENTA
import os
cliente,producto,precio,cantidad="","",0.0,0

#ARGUMENTOS
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

#PROCESSING
precio_total=round(precio*cantidad)

#OUTPUT
print("###################################")
print("         BOLETA DE VENTA           ")
print("###################################")
print("CLIENTE:     ",cliente,"           ")
print("PRODUCTO:    ",producto,"          ")
print("P.U:         ",precio,"            ")
print("CANTIDAD:    ",cantidad,"          ")
print("PRECIO TOTAL:",precio_total,"      ")
print("###################################")

#CONDICIONAL DOBLE
#SI EL PRECIO <199$ ENTONSES LA TIENDA NO LE REGALA NADA
if (precio_total < 199):
    print("USTE NO A GANADO NADA")
else:
    print("SE GANO UNA CANASTA DE NAVIDAD GRATIS")
#fin_if
