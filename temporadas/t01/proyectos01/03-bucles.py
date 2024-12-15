# if elif else

nota = int(input('Introduzca nota'))
if nota < 5:
    calificacion = 'Suspenso'
else:
    calificacion = 'Aprobado'

print(calificacion)

# If también evalúa si la variable tiene información

variable = 20

if variable:
    print('Contiene información')
else:
    print('No contiene información')

if variable == True:
    print('Contiene información')
else:
    print('No contiene información') 

#Programa que controla si es mayor o menos de edad

edad = int(input('Introduce edad'))

if edad < 18:
    print('No puedes pasar')
elif edad > 100:
    print('Edad incorrecta')
else:
    print('Puedes pasar')

nota = float(input('Introduce nota'))

if nota <5:
    print('Suspenso')
elif nota <7:
    print('Suficiente')
elif nota <9:
    print('Notable')
else:
    print('Sobresaliente')

#IF abreviado

n1 = 5
n2 = 10

if n1 > n2: print(n1,'es mayor que',n2)

#Concatenacion

edad = 117

if 0<edad<100: #Como poner if edad > 0 and edad < 100
    print('Edad correcta')
else:
    print('Edad incorrecta')  

#if anidados
#Para comprar coche hay que ser mayor d edad y tener dinero 

dinero=10000

if edad < 18:
    print('No tienes la edad adecuada')
else:
    if dinero < 20000:
        print('Necesitas más dinero')
    else:
        print('Puedes comprar el coche')    

#Menú básico

condicion = int(input('Elige una opción'))
if condicion ==1:
    print('1')
elif condicion ==2:
    print('2') 
else:
    print('Error')       
