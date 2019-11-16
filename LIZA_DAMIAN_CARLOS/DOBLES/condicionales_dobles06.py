#CONDICIONAL DOBLE QUE CALCULA EL SALARIO QUE GANA UN PROFESOR DE QUIMICA A LA SEMANA
import os
profesor,horas_de_clase,pago_horas_clase,="",0,0

#ARGUMENTOS
profesor=os.sys.argv[1]
horas_de_clase=int(os.sys.argv[2])
pago_horas_clase=float(os.sys.argv[3])

#PROCESSING
salario=round(horas_de_clase*pago_horas_clase)

#OUTPUT
print("################################################")
print("        SALARIO DE UN PROFESOR DE QUIMICA       ")
print("################################################")
print("PROFESOR:                  ",profesor,"         ")
print("HORAS DE CLASE A LA SEMANA:",horas_de_clase,"   ")
print("PAGO POR 1 HORAS DE CLASE: ",pago_horas_clase," ")
print("SALARIO:                   ",salario,"$         ")
print("################################################")

#CONDICIONAL DOBLE
# SI EL SUELDO ES <=300 EL PROFESOR TUBO UNA MALA SEMANA
if (salario <= 300):
    print("TUBO UNA MALA SEMANA PESIMO SUELDO")
else:
    print("BUEN SUELDO")
#fin_if
