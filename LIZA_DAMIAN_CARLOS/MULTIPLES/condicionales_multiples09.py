#CONDICIONAL MULTIPLE QUE CALCULA LA FORMULA DE LA HIDROSTATICA
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

#CONDICIONAL MULTIPLE
#PRECION HIDROSTATICA >500
if (precion_hidrostatica > 500):
    print("LA PRECION HIDROSTATICA ES MAYOR QUE 500")

#SI P. HIDROSTATICA >=800 Y <1000 ENTONCES ES MAXIMA
if (precion_hidrostatica >=800 and precion_hidrostatica <=1000):
    print("PRECION HIDROSTATICA MAXIMA")

#SI P. HIDROSTATICA ES <200 ES MINIMA
if (precion_hidrostatica <200):
    print("PRECION HIDROSTATICA MINIMA")
#fin_if

