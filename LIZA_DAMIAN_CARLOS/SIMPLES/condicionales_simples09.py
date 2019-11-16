#CONDICIONAL SIMPLE QUE CALCULA LA FORMULA DE LA HIDROSTATICA
import os
densidad_liquido,gravedad,Altura=0.0,0.0,0.0

#ARGUMENTOS
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
Altura=float(os.sys.argv[3])

#PROCESSING
precion_hidrostatica=densidad_liquido*gravedad*Altura

#OUTPUT
print("#####################################################")
print("#         HALLA LA PRECION HIDROSTATICA             #")
print("#####################################################")
print("# DENSIDAD DEL LIQUIDO: ",densidad_liquido,"kg/m.m.m ")
print("# GRAVEDAD:             ",gravedad,"m/s.s            ")
print("# ALTURA:               ",Altura,"m                  ")
print("# PRECION HIDROSTATICA: ",precion_hidrostatica,"     ")
print("#####################################################")

#CONDICIONAL SIMPLE
#PRECION HIDROSTATICA >400
if (precion_hidrostatica > 400):
    print("LA PRECION HIDROSTATICA ES MAYOR QUE 400")
#fin_if
