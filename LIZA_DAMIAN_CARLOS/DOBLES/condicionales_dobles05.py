#CONDICIONAL DOBLE DE VENTA DE PRODUCTO
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
print("            VENTAS DE PRODUCTO           ")
print("#########################################")
print("VENDEDOR:         ",vendedor,"           ")
print("PRODUCTO:         ",producto,"           ")
print("PRECIO U.:        ",precio,"             ")
print("CUANTOS P. VENDIO:",productos_vendidos," ")
print("TOTAL PAGAR:      ",total_pagar,"$       ")
print("#########################################")

#CONDICIONAL DOBLE
#SI EL TRABAJADOR VENDE <100$ LA TIENDA LO CONSIDERA MAL VENDEDOR
if (total_pagar < 100):
    print("MAL VENDEDOR")
else:
    print("EXELENTE VENDEDOR")
#fin_if
