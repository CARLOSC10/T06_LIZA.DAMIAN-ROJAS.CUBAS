#CONDICIONAL MULTIPLE QUE CALCULA EL SALARIO QUE GANA UN PROFESOR DE QUIMICA A LA SEMANA
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

#CONDICIONAL MULTIPLE
#SI EL SUELDO ES >750 EL PROFESOR TUBO UN BUENA SEMANA
if (salario > 750):
    print("BUENA SEMANA TIENES UN BUEN SUELDO")

#SI EL SUELDO ES >=900 Y <=1900 TUBO UNA EXELENTE SEMANA
if (salario >=900 and salario <=1900):
    print("EXELENTE SEMANA , EXELENTE SUELDO")

#SI EL SUELDO <400 MALA SEMANA
if (salario < 400):
     print("MAL SUELDO")
#fin_if
