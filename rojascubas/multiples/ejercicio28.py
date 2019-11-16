import os
#comparar tres números
print("")
#declararación de variables
A,B,C,a=0.0,0.0,0.0,""

#input
A=float(os.sys.argv[1])
B=float(os.sys.argv[2])
C=float(os.sys.argv[3])


#processing
if( A>B and A>C):                       #CONDICION:si A es mayor que B y A es mayor que C entonces mostrar "A es mayor que B y mayor que C"
    a="A es mayor que B y mayor que C"      #asigna un valor en la variable a

elif(B>A and B>C):                       #condicion:si B es mayor que A y B es mayor que C entonces mostrar "B es mayor que A y mayor que C"
    a="B es mayor que A y mayor que C"        #asigna un valor en la variable a

elif(C>A and C>B):                         #CONDICION:si C es mayor que A y C es mayor que B entonces mostrar "C es mayor que A y mayor que B"
    a="C es mayor que A y mayor que B"     #asigna un valor en la variable a
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
