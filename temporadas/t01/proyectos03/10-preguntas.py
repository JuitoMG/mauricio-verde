"""
--- JUEGO DE PREGUNTAS ---

Funcionamiento: Juego de preguntas que consulta en una base de datos las preguntas,
elige cinco al azar y se las hace al jugador, haciéndole al final una valoración 
según los puntos que consiga.

1.Se genera un diccionario con las preguntas y respuestas a partir de un archivo,
donde cada pregunta tiene su categoría, pregunta, respuesta y opciones

2.Se ejecuta el juego, que elige 5 preguntas al azar para que las conteste el
jugador de una en una, mostrándole las opciones.

3.El jugador elige una de las opciones y recibe instantáneamente la respuesta.

4. Tras cinco preguntas se muestra la puntuación total.

"""
import os
import random
import csv


#Función que crea el diccionario de preguntas a partir de un archivo csv

def crear_preguntas(archivo_csv):
    preguntas = []
    with open(archivo_csv, mode='r', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector)
        for fila in lector:
            categoria, pregunta, respuesta, opciones = fila
            opciones_lista = opciones.split('|')
            preguntas.append({
                'categoria':categoria,
                'pregunta':pregunta,
                'respuesta':respuesta,
                'opciones':opciones_lista
            })
    return preguntas        

def juego_preguntas(preguntas,num_preguntas=5):
    preguntas_seleccionadas = random.sample(preguntas, min(num_preguntas, len(preguntas)))
    puntuacion = 0

    print('\nBienvenido a nuestro juego de preguntas')
    print(f'Contesta estas {num_preguntas} preguntas para sacar la máxima puntuación')

    for i, pregunta in enumerate(preguntas_seleccionadas, 1):
        print(f'\nPregunta {i}/{num_preguntas} - Categoría: {pregunta["categoria"]}\n')
        print(pregunta['pregunta'])

        opciones = pregunta['opciones']
        random.shuffle(opciones)

        for idx, opcion in enumerate(opciones, 1):
            print(f'{idx}. {opcion}')

        while True:
            try:
                respuesta_usuario = int(input('\nEscribe el número de tu respuesta: '))
                if 1 <= respuesta_usuario <= len(opciones):
                    break
                else:
                    print('\nError. Selecciona un número válido.')
            except ValueError:
                print('\nEntrada inválida. Inténtalo de nuevo')

        if opciones[respuesta_usuario - 1] == pregunta['respuesta']:
            print('\nCorrecto!')
            puntuacion += 1
        else:
            print(f'\nIncorrecto. La respuesta correcta era: {pregunta["respuesta"]}')

    if puntuacion == num_preguntas:
        print(f'\nEnhorabuena! Has acertado todas las preguntas! Puntuación: {puntuacion}/{num_preguntas}')
    elif puntuacion == 0:
        print(f'\nLo siento, desastre total! No has acertado ninguna. Sigue intentándolo!')
    else: 
        print(f'Tu puntuación total es: {puntuacion}/{num_preguntas}. Puedes hacerlo mejor.')    
        

archivo_csv = os.path.join(os.path.dirname(__file__), 'lista_preguntas.csv')
preguntas = crear_preguntas(archivo_csv)

juego_preguntas(preguntas)
                    
