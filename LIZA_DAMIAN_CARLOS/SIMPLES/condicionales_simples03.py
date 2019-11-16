#CONDICIONAL SIMPLE DE BOLETA DE VENTA
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
print("          BOLETA DE VENTA          ")
print("###################################")
print("CLIENTE:     ",cliente,"           ")
print("PRODUCTO:    ",producto,"          ")
print("P.U:         ",precio,"            ")
print("CANTIDAD:    ",cantidad,"          ")
print("PRECIO TOTAL:",precio_total,"$     ")
print("###################################")

#CONDICIONAL SIMPLE
#SI EL PRECIO es >200$ ENTONSES LA TIENDA LE REGALA UNA CANASTA DE NAVIDAD
if (precio_total > 200):
    print("SE LLEVA UNA CANASTA DE NAVIDAD GRATIS")
#fin_if
