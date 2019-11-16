#CONDICIONAL MULTIPLE DE BOLETA DE VENTA
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

#CONDICIONAL MULTIPLE
#SI EL PRECIO SUPERA LOS 300$ ENTONSES LA TIENDA LE REGALA UNA CANASTA DE NAVIDAD
if (precio_total >= 300):
    print("USTE SE GANO UNA CANASTA DE NAVIDAD POR SU COMPRA")

#SI EL PRECIO >400$ Y <=10000 USTE ENTRA AL SORTEO DE UNA CAMIONETA 4X4
if (precio_total >400 and precio_total <=10000):
    print("ENTRA AL SORTEO DE UNA CAMIONETA 4X4")

#SI EL PRECIO <199 NO A GANADO NADA
if (precio_total < 199):
    print("USTED NO A GANADO NADA")
#fin_if




