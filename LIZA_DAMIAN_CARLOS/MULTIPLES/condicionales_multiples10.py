#CONDICIONAL MULTIPLES QUE CALCULA LA COMPRA DE UN CLENTE
import os
cliente,producto_uno,producto_dos,precio_uno,precio_dos,cantidad_uno,cantidad_dos="","","",0.0,0.0,0,0

#ARGUMENTOS
cliente=os.sys.argv[1]
producto_uno=os.sys.argv[2]
producto_dos=os.sys.argv[3]
precio_uno=float(os.sys.argv[4])
precio_dos=float(os.sys.argv[5])
cantidad_uno=int(os.sys.argv[6])
cantidad_dos=int(os.sys.argv[7])

#PROCESSING
pagar=round(precio_uno*cantidad_uno+precio_dos*cantidad_dos)

#OUTPUT
print("#########################################")
print("#              LA CURACAO               #")
print("#########################################")
print("# CLIENTE:            ",cliente,"        ")
print("# PRODUCTO 01:        ",producto_uno,"   ")
print("# PRODUCTO 02:        ",producto_dos,"   ")
print("# PRECIO PRODUCTO 01: ",precio_uno,"     ")
print("# PRECIO PRODUCTO 02: ",precio_dos,"     ")
print("# CANTIDA P. 01:      ",cantidad_uno,"   ")
print("# CANTIDA P. 02:      ",cantidad_dos,"   ")
print("# TOTAL A PAGAR:      ",pagar,"$         ")
print("#########################################")

#CONDICIONAL MULTIPLES
#SI EL CLIENTE SUPERA LOS 500$ GANA UN PANETON
if (pagar >=500):
    print("USTED GANO UN PANETON")

#SI EL CLIENTE SUPERA LOS 800$ y 5000$ LA TIENDA LE REGALA UN TELEVISOR GRATIS
if (pagar >=800 and pagar <=5000):
    print("GANO UN TELEVISOR GRATIS POR SU COMPRA")

#SI SU COMPRA ES MENOR 100$ GANA UN TICKET
if (pagar <=100):
    print("GANO UN TICKET PARA UN SORTEO")
#fin_if
