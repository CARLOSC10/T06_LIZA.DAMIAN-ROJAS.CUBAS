import os
# distancia que a rrecorrido un auto que realizo(M.R.U.V)
print("")
#declaracion de variables
velocidad_inicial,tiempo,aceleracion,distancia,a=0.0,0.0,0.0,0.0,""

#input
velocidad_inicial=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
aceleracion=float(os.sys.argv[3])

#processing
distancia=(velocidad_inicial*tiempo)+(aceleracion*tiempo**2)/2

if(distancia>=0.0):         #condicion:si la distancia es mayor que cero mostar Distancia válida
    a="Distancia Válida"    #asigna un mensaje en la variable a

else:
    a="Distancia invalida"   #condicion:si no ,mostrar distancia invalida
#fin_if

#otput
print("************************************************************************")
print("*        DISTANCIA DE UN AUTO EN UN MOVIMIENTO(M.R.U.V)                *")
print("************************************************************************")
print("*la velocidad inicial es:",velocidad_inicial,"metros por segundo","                     *")
print("*el tiempo en segundos es:",tiempo,"                                       *")
print("*la aceleracion es:",aceleracion,"metros/segundo al cuadrado","                   *")
print("*la distancia que rrecorrio el auto es:",distancia,"metros","                 *")
print("************************************************************************")
print(a)
print("************************************************************************")
