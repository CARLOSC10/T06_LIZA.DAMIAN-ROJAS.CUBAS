import os
#comparar tres números y si el "primer número" es mayor mostrar un mensaje
print("")
#declararación de variables
A,B,C,a=0.0,0.0,0.0,""

#input
A=float(os.sys.argv[1])
B=float(os.sys.argv[2])
C=float(os.sys.argv[3])


#processing
if( A>B and A>C):                       #CONDICION:si A es mayor que B y A es mayor que C entonces mostrar "A es mayor que B y mayor que C"
    a="A es mayor que B y mayor que C"      #asigna un mensaje en la variable a

else:
    a="NO CUMLE LA CONDICION"           #condicion:si no,mostrar un mensaje
#fin_if

#output
print("**************************************")
print("*          COMPARAR NÚMEROS          *")
print("**************************************")
print("*A vale:",A,"                        *")
print("*B vale:",B,"                       *")
print("*C vale:",C,"                        *")
print("**************************************")
print(a)
print("**************************************")
