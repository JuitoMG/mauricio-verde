"""
--- CALCULADORA BÁSICA ---

Funcionamiento: 

1. Elegir una de las opciones del menú (Suma, resta, multiplicación, división)
2. Introducir el primer número, luego el segundo.
3. En el caso de la división, el divisor nunca puede ser cero.
4. Tras introducir los números, veremos el resultado de la operación elegida.
5. Para salir del programa hay que escoger "5" en el menú.

"""

#Operaciones 

def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicar (a, b):
    return (a * b)
def division (a, b):
    if b != 0:
        return a / b
    else:
        print('\nError: Imposible dividir entre cero')

#Programa con menú

def calculadora():
    print("\n--- CALCULADORA BÁSICA DE MAURICIO---\n")
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Salir\n')

    while True:
        opcion = input('Elige una opción ')
        if opcion == '5':
            print('\nSaliendo...')
            print('\nCalculadora básica cerrada')
            break
        
        if opcion in ['1','2','3','4']:
            try:
                numero1 = float(input('\nIntroduce el primer número '))
                numero2 = float(input('\nIntroduce el segundo número '))
            except ValueError:
                print('\nError: Número no válido')
                continue

            if opcion == '1':
                print(numero1,'+',numero2,f'= {suma(numero1,numero2)}')
            if opcion == '2':
                print(numero1,'-',numero2,f'= {resta(numero1,numero2)}') 
            if opcion == '3':
                print(numero1,'x',numero2,f'= {multiplicar(numero1,numero2)}') 
            if opcion == '4':
                print(numero1,'/',numero2,f'= {division(numero1,numero2)}') 
        else:
            print('\nOpción no válida. Inténtalo de nuevo.')

#Inicia el programa
calculadora()                                        

