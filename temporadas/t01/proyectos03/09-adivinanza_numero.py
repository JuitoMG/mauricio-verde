"""
--- JUEGO ADIVINAR NÚMERO ---

Funcionamiento: 

Se genera un número aleatorio entre 1 y 100 que tienes que adivinar en 10 intentos.
Introduce un número en cada intento, fijándote en las pistas que te dan para adivinarlo.
Tras 10 intentos, el juego se acaba. Si aciertas antes, recibes una felicitación.

"""

import random

def juego_adiv_num():
    print('\n--- EL GENIO DE LOS NÚMEROS ---')
    print('\nBienvenido al cursillo para genios de la lámpara.\nAquí aprenderás a afinar tus poderes básicos de adivinación.\nPara ello tendrás que adivinar qué número del 1 al 100 estoy pensando.\nSolo tendrás 10 intentos. Concéntrate bien y... Adelante!\n')
    numero_secreto = random.randint(1,100)
    intentos_restantes = 10

    while intentos_restantes >0:
        try:
            respuesta = int(input('\nEn qué número estoy pensando? '))
            if respuesta == numero_secreto:
                print("\nEnhorabuena! Acertaste! Tus poderes son cada vez mayores!")
                break
            elif respuesta < numero_secreto:
                print(f'\nNo, no es el {respuesta}. Es mayor.')
            else:
                 print(f'\nNo, no es el {respuesta}. Es menor.')
            intentos_restantes -= 1
            print(f'\nTe quedan {intentos_restantes} intentos.')
        except ValueError:
            print('\nError. Introduce un número válido.')

    if intentos_restantes == 0:
        print(f'\nLo siento, te quedaste sin intentos. El número era el {numero_secreto}. Vuelve cuando mejores tus poderes de adivinación.')     

juego_adiv_num()