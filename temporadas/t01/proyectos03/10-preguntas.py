"""
--- JUEGO DE PREGUNTAS ---

"""

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

    print('Bienvenido')
    print(f'Contesta estas {num_preguntas} preguntas para sacar la máxima puntuación')

    for i, pregunta in enumerate(preguntas_seleccionadas, 1):
        print(f'Pregunta {i}/{num_preguntas} - Categoría: {pregunta["categoria"]}')
        print(pregunta['pregunta'])

        opciones = pregunta['opciones']
        random.shuffle(opciones)

        for idx, opcion in enumerate(opciones, 1):
            print(f'{idx}. {opcion}')

        while True:
            try:
                respuesta_usuario = int(input('Escribe el número de tu respuesta: '))
                if 1 <= respuesta_usuario <= len(opciones):
                    break
                else:
                    print('Error. Selecciona un número válido.')
            except ValueError:
                print('Entrada inválida. Inténtalo de nuevo')

        if opciones[respuesta_usuario - 1] == pregunta['respuesta']:
            print('Correcto!')
            puntuacion += 1
        else:
            print(f'Incorrecto. La respuesta correcta era: {pregunta["respuesta"]}')


archivo_csv = 'lista_preguntas.csv'
preguntas = crear_preguntas(archivo_csv)

juego_preguntas(preguntas)
                    
