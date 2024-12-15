
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






#Menú ejercicios

print('Menú')
print('1. Edad, mayor o menor')
print('2. Número mayor, menor o igual')
print('3. Calificación de nota')
print('4. Descuentos almacén')
print('5. Descuentos por gasto')

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

else:
    print('Opción incorrecta')
