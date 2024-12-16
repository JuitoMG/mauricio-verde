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


#El bucle For

for i in[1,10]:
    print('Hola')

for i in ['primavera', 'verano', 'otoño','invierno']:
    print(i)    

#Repite el print tantas veces como caracteres hay en el string

for i in 'frase':
    print('Hola', end=' ')

#Evaluar si un mail contiene el caracter @


miEmail=input('Introduce email')
email=False
for i in miEmail:
    if i=='@':
        email=True
if email==True:
    print('Email correcto')
else:
    print('Email incorrecto')                


#Unir valores de texto con valores de variable

for i in range(5):
    print(f'Valor de la variable {i}')

for i in range(5,10):
    print(f'Valor de la variable {i}')

#Tercer argumento con el que especificamos de cuanto en cuanto va el conteo

for i in range(5,10,2):
    print(f'Valor de la varible {i}')    

#Las cadenas son iterables

for x in 'Banana':
    print(x)    

#Con break se puede interrumpir la ejecución

frutas = ["manzana", "banana", "cereza"]
for x in frutas:
  print(x)
  if x == "banana":
    break    

#Con continue se puede detener la iteración actual y continuar después

frutas = ["manzana", "banana", "cereza"]
for x in frutas:
  if x == "banana":
    continue
  print(x)


#Con range se recorre un código un número específico de veces
for x in range(6):
    print(x)

#Funcion de range con parámetro de inicio incrementado en 1
for x in range(2,6):
    print(x)    

#Funcion range con paámetro de inicio incrementado en 3
for x in range(2,30,3):
    print(x)    

#Bucle for anidado
color = ['verde','amarillo','rojo']
frutas = ['manzana','plátano','cereza']
for x in frutas:
    for y in color:
        print(x,y) 

#Los bucles for no pueden estar vacíos. Se usa pass si no hay contenido
for x in [0,1,2]:
    pass           

#BUCLE WHILE

#Imprime edad cuando el contador llegue a 18

edad = 0
while edad < 18:
    edad = edad+1
print('Tienes '+str(edad))

#Pregunta edad mientras sea negtiva
edad = int(input('Introduce edad: '))
while edad<0:
    print('Edad incorrecta')
    edad = int(input('Introduce edad: '))

#Calcula la raíz cuadrada. Tenemos 3 intentos y el número no puede ser negativo

import math
intentos=0
num = int(input('Introduce número: '))

while num<0:
    intentos= intentos+1
    print('Incorrecto')
    num = int(input('Introduce número: '))

    if intentos==2:
        print('Demasiados intenros')
        break
if intentos <2:
    intentos=intentos+1
    solucion=math.sqrt(num)
    print('La raíz cuadrada de '+str(num)+' es: '+str(solucion)) 

#Bucle While con if anidado
num = 1
while num < 6:
    print(num)
    if num == 3:
        break
    num += 1
