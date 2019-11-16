import os
#Área del trapecio
print("")
#declararación de variables
base_menor,base_mayor,altura,area_trapecio,a=0.0,0.0,0.0,0.0,""

#input
base_menor=float(os.sys.argv[1])
base_mayor=float(os.sys.argv[2])
altura=float(os.sys.argv[3])

#processing
area_trapecio=((base_mayor+base_menor)/2)*altura

if(area_trapecio>0.0 and area_trapecio<100.0):       #condicion:si el area es mayor que cero Y MENOR QUE 100 mostrar UN MENSAJE
    a="ÁREA PEQUEÑA "         #asigna un mensaje en la variable a

elif(area_trapecio>100.0 and area_trapecio<500):       #condicion:si el area es mayor que 100 Y menor QUE 500 mostrar UN MENSAJE
    a="AREA EXTENSA"              #asigna un valor en la variable a

elif(area_trapecio>500):         #condicion:si el area es mayor 500 mostrar UN MENSAJE
    a="AREA SUPER EXTENSA"       #asigna un valor en la variable a

#Output
print("**************************************************")
print("*                ÁREA DEL TRPECIO                *")
print("**************************************************")
print("*la Base mayor:",base_mayor,"                            *")
print("*la base menor:",base_menor,"                            *")
print("*la altura:",altura,"                                *")
print("*el area del Trapecio:",area_trapecio,"                    *")
print("**************************************************")
print(a)
print("**************************************************")
