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

if(area_trapecio>0.0):       #condicion:si el area es mayor que cero mostrar Área Correcta
    a="Área Correcta"         #asigna un mensaje en la variable a

else:
    a="Area incorrecta"       #condicion:si no ,mostrar area incorrecta
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
