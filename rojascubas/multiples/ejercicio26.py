import os
#COMPROBACION DE UNA FECHA
print("")
#declararación de variables
dia,mes,anio,fecha,a,b=0,"",0,"","",""

#input
dia=int(os.sys.argv[1])
mes=os.sys.argv[2]
anio=int(os.sys.argv[3])

#processing
fecha=str(dia)+"/"+mes+"/"+str(anio)
if(dia>=32):                               #condicion:si el dia es mayor o igual a 32 mostrar un mensaje de error
    a="El Valor del Dia Es Errónea"           #asigna un valor en la variable a
    b="FECHA ERRONEA"                         #asigna un valor a la variable b

elif(mes=="enero" or mes=="febrero" or mes=="marzo" or mes=="abril" or mes=="mayo" or mes=="junio" or mes=="julio" or mes=="agosto" or mes=="setiembre" or mes=="octubre" or mes=="noviembre" or mes=="diciembre"):     #condicion:verificar mes si es erroneo mostrar mensaje
    a="EL VALOR DEL MES ES ERRONEA"                    #asigna un valor en la variable a
    b="FECHA ERRONEA"                                  #asigna un valor a la variable b

elif(anio<0):
    a="EL VALOR DEL AÑO ES ERRONEO"                    #asigna un valor en la variable a
    b="FECHA ERRONEA"                                  #asigna un valor a la variable b

#output
print("**************************************")
print("*          VALOR DE LA FECHA         *")
print("**************************************")
print("*DÍA:",dia,"                            *")
print("*MES:",mes,"                         *")
print("*AÑO:",anio,"                          *")
print("*FECHA:",fecha,"               *")
print("**************************************")
print(a)
print(b)
print("**************************************")
