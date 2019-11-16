#CONDICIONAL DOBLE QUE CALCULA LA COMPRA DE UN CLENTE
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

#CONDICIONAL DOBLE
#SI EL CLIENTE NO SUPERA LOS 450$ NO GANA NADA
if (pagar <=450):
    print("USTED NO A GANADO NADA")
else:
    print("USTED GANO UN DVD GRATIS")
#fin_if
