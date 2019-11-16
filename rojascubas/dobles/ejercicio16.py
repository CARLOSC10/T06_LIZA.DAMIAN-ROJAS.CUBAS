import os

#COMPROBACION DE UNA FECHA CON LA VERIFICACION DE EL DIA
print("")
#declararación de variables
dia,mes,anio,fecha,a=0,"",0,"",""

#input
dia=int(os.sys.argv[1])
mes=os.sys.argv[2]
anio=int(os.sys.argv[3])

#processing
fecha=str(dia)+"/"+mes+"/"+str(anio)
if(dia>=32 and dia<=0):                               #condicion:si el dia es mayor o igual a 32 y menor igual a cero mostrar un mensaje de error
    a="El Valor de la Fecha Es Errónea"    #asigna un mensaje en la variable a

else:
    a="El Valor de la Fecha Es Valida"          #condicion:si no ,mostrar la fecha es valida
#fin_if

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
print("**************************************")
