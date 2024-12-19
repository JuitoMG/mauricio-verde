"""
--- CALCULADORA AVANZADA ---

Funcionamiento:

Esta calculadora hace más operaciones que la básica, y a mayores almacena
los resultados en un historial.

1. Elegir una de las opciones del menú (Suma, resta, multiplicación, división,
    potencia, raíz cuadrada, factorial, logaritmo o trigonometría)
2. Introducir los números que vaya solicitando
3. En el caso de la división, el divisor nunca puede ser cero.
4. Tras introducir los números, veremos el resultado de la operación elegida.
5. Con la opción "10" podemos ver el historial de operaciones realizadas.
6. Para salir del programa hay que escoger "11" en el menú.

"""

import math

def calculadora_avanzada():
    
    #Historial
    
    historial = []

    def mostrar_historial():
        if not historial:
            print('\nEl historial vacío.')
        else:
            print('\nHistorial de operaciones')
            print('-------------------------\n')
            for i, operacion in enumerate(historial, start=1):
                print(f'{i}. {operacion}')

    def imprimir_guardar(linea_resultado):
        historial.append(linea_resultado)
        print(linea_resultado)

    
    #Menú

    print('\n--- CALCULADORA AVANZADA DE MAURICIO ---\n')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Potencia')
    print('6. Raíz cuadrada')
    print('7. Factorial')
    print('8. Logaritmo')
    print('9. Trigonometría')
    print('10. Mostrar historial')
    print('11. Salir')

    while True:
        opcion = input("\nElige una opción: ")

        if opcion == '11':
            print('\nSaliendo...')
            print('\nCalculadora básica cerrada')
            break
        if opcion == '10':
            mostrar_historial()
            continue

        try:
            if opcion in ['1','2','3','3','4','5']:
                numero1 = float(input('\nIntroduce el primer número '))
                numero2 = float(input('\nIntroduce el segundo número '))

            elif opcion == '6':
                numero1 = float(input('\nRaíz cuadrada - Introduce el número: '))
                resultado = math.sqrt(numero1)
                linea_resultado = f'√{numero1} = {resultado}\n'
                imprimir_guardar(linea_resultado)
                continue
                

            elif opcion == '7':
                numero1 = int(input('\nFactorial - Introduce un número entero: '))
                resultado = math.factorial(numero1)
                linea_resultado = f'{numero1}! = {resultado}\n'
                imprimir_guardar(linea_resultado)
                continue
            
            elif opcion == '8':
                numero1 = float(input('\nLogaritmo - Introduce el número: '))
                base = int(input('\nIntroduce la base (Por defecto 10): ') or 10)
                resultado = math.log(numero1, base)
                linea_resultado = f'log{base}({numero1}) = {resultado}\n'
                imprimir_guardar(linea_resultado)

            elif opcion == '9':
                angulo = float(input('\nTrigonometría - Introduce el ángulo en grados: '))
                seno = math.sin(math.radians(angulo))
                coseno = math.cos(math.radians(angulo))
                tangente = math.tan(math.radians(angulo))
                linea_resultado = f'Sen({angulo}°) = {seno}\nCos({angulo}°) = {coseno}\nTan({angulo}°) = {tangente}\n'
                imprimir_guardar(linea_resultado)
                continue

            else:
                print('Opción no válida. Inténtalo de nuevo.')
                continue

            if opcion == '1':
                resultado = numero1 + numero2
                linea_resultado = f'{numero1} + {numero2} = {resultado}\n'
                imprimir_guardar(linea_resultado)
            elif opcion == '2':
                resultado = numero1 - numero2
                linea_resultado = f'{numero1} - {numero2} = {resultado}\n'
                imprimir_guardar(linea_resultado)
            elif opcion == '3':
                resultado = numero1 * numero2
                linea_resultado = f'{numero1} x {numero2} = {resultado}\n'
                imprimir_guardar(linea_resultado)
            elif opcion == '4':
                if numero2 != 0:
                    resultado = numero1 / numero2
                    linea_resultado = f'{numero1} / {numero2} = {resultado}\n'
                    imprimir_guardar(linea_resultado)    
                else:
                    print('\nError: No es posible dividir entre cero')
            elif opcion == '5':
                resultado = math.pow(numero1,numero2)
                linea_resultado = f'{numero1}^{numero2} = {resultado}\n'
                imprimir_guardar(linea_resultado)
            
            
        except ValueError:
            print('\nError: Entrda no válida. Inténtelo de nuevo.')
        except Exception as e:
            print(f'\nError: {e}')

calculadora_avanzada()



