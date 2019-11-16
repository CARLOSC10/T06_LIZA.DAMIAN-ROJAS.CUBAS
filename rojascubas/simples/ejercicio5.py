import os
#precio final de un producto
print("")
#declaracion de variables
nombre_cliente,producto,precio,igv,precio_final,a="","",0.0,0.0,0.0,""

#input
nombre_cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])

#processing
igv=0.18*precio
precio_final=precio+igv
if(precio_final<=0.0):                    #condicion:si el pecio final es igual a cero  mostar precio final erróneo
    a="Precio Final Erróneo"              #asigna un mensaje en la variable a
#fin_if

#output
print("**************************************")
print("*      PRECIO FINAL DE UN PRODUCTO   *")
print("**************************************")
print("*CLIENTE:",nombre_cliente,"                    *")
print("*PRODUCTO:",producto,"                *")
print("*PRECIO:S/",precio,"              *")
print("**************************************")
print(a)
print("**************************************")
