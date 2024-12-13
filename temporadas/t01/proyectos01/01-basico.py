#PYTHON CON MAURICIO VERDE

# VARIABLES

#Declaración de números enteros y de coma flotante

edad = 25
peso = 73.5
print('Con ',edad,' años, peso ',peso,'Kg.')

#Declaración de String y String en varias líneas

nombre = 'Fulánez'
texto_largo = '''Esto es 
un mensaje más largo 
en varias líneas'''

print(nombre)
print(texto_largo)

#Las variables se puedes reescribir cambiando el tipo 

edad2 = 33
edad2 = '34'
print(edad)

#Declaración de una constante

NUMEROPI = 3.14159
print(NUMEROPI)

#Booleanos

es_verdadero = True
es_falso = False

True == 1
False == 0

print(True + 2)

#Cuando se valida una condición, se devuelve V o F

print(10>9)
print(10 == 9)

#Declaración multiple

a, b, c = 'string', 15, True
print(a,b,c)

#Verificar tipo de variable

print(type(edad))
print(type(peso))
print(type(nombre))
print(type(edad2))
print(type(es_verdadero))
print(type(NUMEROPI))

# CASTING

#Forzado de tipos

#Entero
x = int(1)      # x valdrá 1
y = int(2.7)    # y valdrá 2
z = int('3')    # z valdrá 3

#Float
x = float(1)      # x valdrá 1.0
y = float(2.7)    # y valdrá 2.0
z = float('3')    # z valdrá 3.0
w = float("4.1")  # w valdrá 4.1

#String
x = str("s1")   # x valdrá 's1'
y = str(2)      # y valdrá '2'
z = str(3.0)    # z valdrá '3.0'

#Casting reconversión de tipos

#De int a float
numero = 13
numero2 = float(numero)

#De float a int
numero3 = 3.456
numero4 =int(numero3)

#De String a int
texto = '234'
numero5 = int(texto)

#De int a String
numero6 = 345
texto2 = str(numero6)

#OPERADORES

#Resto
numerador = 10
denominador = 2
denominador2 = 3

print(numerador%denominador)
print(numerador%denominador2)

#Suma e incremento +=

numeroCualquiera = 40
numeroCualquiera += 1
print(numeroCualquiera)

#operadores lógicos

a = True
b = False
resultadoY = a and b
resultadoOR = a or b
resultadoNOT = not a
print(resultadoY,resultadoOR,resultadoNOT)

#Sintaxis para varios operadores lógicos
edadAhora = 33

veintes = edad >= 20 and edad <30
print(veintes)
treintas = edad >= 30 and edad <40
print(treintas)

if (20 <= edad < 30) or (30 <= edad < 40):
    print('Dentro de rango (20\'s) o (30\'s)')
else:
    print('No está dentro de rango')    