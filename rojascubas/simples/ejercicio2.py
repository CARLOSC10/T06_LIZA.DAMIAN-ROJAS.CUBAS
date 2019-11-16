import os
#acceder a una cuenta con nombre,usuario("12345F") y contraseña("1234567")
print("")
#declararación de variables
nombre,usuario,contraseña,a="","","",""

#input
nombre=os.sys.argv[1]
usuario=os.sys.argv[2]
contraseña=os.sys.argv[3]

#processing
if(usuario=="12345F" and contraseña=="1234567"):     #condicion: si el usuario es igual a "12345F" y la contraseña igual a "1234567 entonces mostrar Accseo permitido
        a="Acceso Permitido"                            #asigna un mensaje en la variable a
#fin_if

#output
print("**************************************")
print("*             CUENTA                 *")
print("**************************************")
print("*NOMBRE:",nombre,"                       *")
print("*USUARIO:",usuario,"                    *")
print("*CONTRASEÑA:",contraseña,"                *")
print("**************************************")
print(a)
print("**************************************")
