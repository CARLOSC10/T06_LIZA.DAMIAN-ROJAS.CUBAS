#CONDICIONAL DOBLE QUE CALCULA LA COMPRA DE UNA PERSONA
import os
comprador,producto,precio,cantidad="","",0.0,0

#ARGUMENTOS
comprador=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

#PROCESSING
total_pagar=round(precio*cantidad)

#OUTPUT
print("##########################################")
print("#          FERRETERIA DON JOSE           #")
print("##########################################")
print("# COMPRADOR:     ",comprador,"            ")
print("# PRODUCTO:      ",producto,"             ")
print("# PRECIO DEL P.: ",precio,"               ")
print("# CANTIDAD:      ",cantidad,"             ")
print("# TOTAL A PAGAR: ",total_pagar,"$         ")
print("##########################################")

#CONDICIONAL DOBLE
#SI EL COMPRADOR NO SUPERA LOS 150$ NO LE DAN NINGUN TICKET
if (total_pagar < 150):
    print("NO RECIBE NINGUN TICKET")
else:
    print("RECIBE UN TICKET POR SU COMPRA")
#fin_if
