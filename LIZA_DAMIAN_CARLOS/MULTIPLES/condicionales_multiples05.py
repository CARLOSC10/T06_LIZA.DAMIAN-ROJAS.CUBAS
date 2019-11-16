#CONDICIONAL MULTIPLE DE VENTA DE PRODUCTO
import os
vendedor,producto,precio,productos_vendidos="","",0.0,0

#ARGUMENTOS
vendedor=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
productos_vendidos=int(os.sys.argv[4])

#PROCESSING
total_pagar=round(precio*productos_vendidos)

#OUTPUT
print("#########################################")
print("           VENTAS DE PRODUCTO            ")
print("#########################################")
print("VENDEDOR:         ",vendedor,"           ")
print("PRODUCTO:         ",producto,"           ")
print("PRECIO U.:        ",precio,"             ")
print("CUANTOS P. VENDIO:",productos_vendidos," ")
print("TOTAL PAGAR:      ",total_pagar,"$       ")
print("#########################################")

#CONDICIONAL MULTIPLE
#SI EL TRABAJADOR VENDE >400$ LA TIENDA LO CONSIDERA UN EXELENTE VENDEDOR
if (total_pagar > 400):
    print("VENDEDOR EXELENTE")

#SI EL TRABAJADOR VENDE >=900$ Y <=5000$ LA TIENDA LE DA UN BONUS DE 100$ POR SU DESENPEÑO EN SUS VENTAS
if (total_pagar >=900 and total_pagar <=5000):
    print("BUEN VENDEDOR Y GANA UN BONUS DE 100$")

#SI EL TRABAJADOR VENDE <100$ LO CONSIDERAN PESIMO VENDEDOR
if (total_pagar < 100):
    print("VENDEDOR PESIMO")
#fin_if
