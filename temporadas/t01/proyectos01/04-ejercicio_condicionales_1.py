
#1. Programa que pregunta al ususario su edad y la muestra por pantalla, y si eres mayor de edad o no

def opcion1():
    edad = int(input('Introduce tu edad'))
    print('Tu edad es de',edad,'años')
    if edad >= 18:
        print('Eres mayor de edad')
    else:
        print('Eres menor de edad')    


#2. Solicita dos números y determina si uno es mayor que otro, menor, o iguales

def opcion2():
    numero1 = int(input('Introduce el primer número'))
    numero2 = int(input('Introduce el segundo número'))

    print('Primer número:',numero1)
    print('Segundo número:',numero2)
    if numero1 > numero2:
        print('El primer número es mayor')
    elif numero1 < numero2:
        print('El segundo número es mayor')
    else:
        print('Los dos números son iguales')

#3. Script que solicita una calificacion y luego imprime
#Suspenso, Suficiente, notable y sobresaliente segun nota

def opcion3():
    nota = float(input('Introduzca una nota'))

    if nota >= 9:
        print('Sobresaliente')
    elif nota >= 7:
        print('Notable')
    elif nota >= 6:
        print('Bien')
    elif nota >= 5:
        print('Suficiente')
    else:
        print('Suspenso')                 


#4. Un almacen da un descuento del 15% si la compra del cliente supera los 1000€.
#Escribe el programa que pida el total de la compra y calcule el descuento.
#si aplica y el total a pagar

def opcion4():
    total_compra = float(input('Total de la compra'))

    if total_compra > 1000:
        descuento = total_compra * 0.15
        #redondeo
        descuento_redondeado = round(descuento, 2)

        total_final = round(total_compra - descuento_redondeado, 2)

        print(f'Se aplicó un descuento del 15%, un total de {descuento_redondeado}€. Total a pagar: {total_final}€')
    else:
        total_final = round(total_compra, 2)
        print(f'Total a pagar: {total_final}€')

#5. Otra tienda ofrece descuento según total de compra
# Si es mayor a 100€, descuento del 10%, si es mayor a 500€,
# desuento de 20%. Calcula el total a pagar tras descuento

def opcion5():
    compra = float(input('Introduce el total de la compra en euros'))
    if compra >500:
        total = compra * 0.8
        print(f'El total de la compra tras el descuento del 20% es {total:.2f}€')
    elif compra > 100:
        total = compra*0.9
        print(f'El total de la compra tras el descuento del 10% es {total:.2f}€')
    else:
        print(f'Total a pagar: {compra:.2f}€')     

#6. Escribe un programa que sume todos los números enteros del
#  1 al 100 usando un bucle for

def opcion6():
    suma = 0
    for numero in range(1,100):
        suma += numero
    print('La suma de los números del uno al 100 es: ',suma) 


#7. Genera e imprime la lista de los cuadrados de los 
# primeros 10 números enteros

def opcion7():
    cuadrados = []
    for numero in range(1,11):
        cuadrados.append(numero ** 2)
    print('Cuadrados de los números del 1 al 10:',cuadrados)   

#8. Cuenta cuántas veces aparece la letra 'a' en un String

def opcion8():
    texto = str(input('Escribe una palabra o frase'))
    contador = 0
    for caracter in texto:
        if caracter == 'a':
            contador +=1
    print(f'La letra "a" aparece {contador} veces en "{texto}".') 

#9. Tabla de multiplicar

def opcion9():
    numero = int(input('Introdue un número para saber su tabla'))
    print('--- Tabla del ',numero,'---')
    for i in range(1,11):
        resultado = numero * i
        print(f'{numero}x{i}={resultado}')

#10. Suma los números introduccidos hasta que se introduzca un 0,
#  mostrando el resultado al final

def opcion10():
    suma = 0
    numero = int(input('Introduce un número (0 para terminar) '))
    while numero !=0:
        suma += numero
        numero = int(input('Introduce otro número (0 para terminar) '))
    print('La suma total es: ',suma)            






#Menú ejercicios

print('--- Menú ---\n')
print('--- Ejercicios condicionales ---\n')
print('1. Edad, mayor o menor')
print('2. Número mayor, menor o igual')
print('3. Calificación de nota')
print('4. Descuentos almacén')
print('5. Descuentos por gasto')
print('\n--- Ejercicios bucles ---\n')
print('6. Suma números enteros')
print('7. Lista de los primeros 10 cuadrados')
print('8. Conteo letra A')
print('9. Tabla de multiplicar')
print('10. Suma de números proporcionados')


opcion = int(input('Elige opción: '))

if opcion == 1:
    opcion1()
elif opcion == 2:
    opcion2()
elif opcion == 3:
    opcion3()
elif opcion == 4:
    opcion4()
elif opcion == 5:
    opcion5()
elif opcion == 6:
    opcion6()
elif opcion == 7:
    opcion7()
elif opcion == 8:
    opcion8() 
elif opcion == 9:
    opcion9()
elif opcion == 10:
    opcion10()                         

else:
    print('Opción incorrecta')
