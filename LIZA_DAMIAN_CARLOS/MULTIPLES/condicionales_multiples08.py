#CONDICIONAL MULTIPLE QUE CALCULA LA COMPRA DE UNA PERSONA
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

#CONDICIONAL MULTIPLE
#SI EL COMPRADOR SUPERA 100$ LE DAN UN TICKET
if (total_pagar >= 100):
    print("RECIBE UN TICKET DE SORTEO")

#SI EL COMPRADOR SUPERA LOS 500$ Y 2000$ SE LLEVA UNA BOLSA DE CEMENTO
if (total_pagar >500 and total_pagar <=2000):
    print("RECIBE UNA BOLSA DE CEMENTO GRATIS")

#SI EL COMPRADOR NO SUPERA LOS 70$ NO RECIBE NADA
if (total_pagar <= 70):
    print("USTED NO RECIBE NINGUN PREMIO")
#fin_if
