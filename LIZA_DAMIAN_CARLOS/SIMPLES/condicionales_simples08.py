#CONDICIONAL SIMPLE QUE CALCULA LA COMPRA DE UNA PERSONA
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

#CONDICIONAL SIMPLE
#SI EL COMPRADOR SUPERA 200$ LE DAN UN TICKET
if (total_pagar >= 200):
    print("RECIBE UN TICKET DE SORTEO")
#fin_if
