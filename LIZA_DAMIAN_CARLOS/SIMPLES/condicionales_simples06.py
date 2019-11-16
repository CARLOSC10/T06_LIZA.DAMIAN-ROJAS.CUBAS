#CONDICIONAL SIMPLE QUE CALCULA EL SALARIO QUE GANA UN PROFESOR DE QUIMICA A LA SEMANA
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

#CONDICIONAL SIMPLE
# SI EL SUELDO ES >700 EL PROFESOR TUBO UN SUELDO
if (salario > 700):
    print("TUBO UN BUEN SUELDO")
#fin_if
