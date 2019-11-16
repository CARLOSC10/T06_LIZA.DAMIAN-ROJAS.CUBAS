import os
#precio final de un producto(calificar precio)
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

if(precio_final>0.0 and precio_final<10.0):                    #condicion:si el pecio final es mayor a cero  y menor a 10 mostar un mensaje
    a="PRECIO FINAL BARATO"                              #asigna un valor en la variable a


elif(precio_final>10.0 and precio_final<20.0):           #condicion:si el pecio final es mayor 10   y menor a 20.0 mostar un mensaje
     a="PRECIO FINAL COMODO"                             #asigna un valor en la variable a

elif(precio_final>20.0):                 #condicion:si el precio final es mayor a 20 mostrar un mensaje
    a="PRECIO FINAL CARO"               #asigna un valor en la variable a

#fin_if

#output
print("**************************************")
print("*      PRECIO FINAL DE UN PRODUCTO   *")
print("**************************************")
print("*CLIENTE:",nombre_cliente,"                    *")
print("*PRODUCTO:",producto,"                *")
print("*PRECIO:S/",precio,"              *")
print("*PRECIO FINAL:",precio_final,"         *")
print("**************************************")
print(a)
print("**************************************")
