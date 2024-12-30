"""
--- RESTAURADOR DE ARCHIVOS ---

Funcionamiento: Pequeño programa hecho a propósito para arreglar un archivo csv.
El Restaurador recorrerá cada fila añadiendo los campos que faltan y añadiendo
contenido en ellos si fuese necesario, como un precio por defecto.

"""


import csv
import os

class RestauradorLibros:
    def __init__(self, archivo_entrada, archivo_salida):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida


    def restaurar(self):
        libros_restaurados = []
        with open(self.archivo_entrada, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for fila in reader:
                libro = {
                    'Título':fila['Título'] if fila['Título'].strip() else 'Sin título',
                    'Autor':fila['Autor'] if fila['Autor'].strip() else 'Anónimo',
                    'Año':self.restaurar_ano(fila['Año']),
                    'Precio':fila['Precio'] if fila['Precio'].strip() else '5.99',
                    'Cantidad':fila['Cantidad'] if fila['Cantidad'].strip() else '1',
                    'Estado':fila['Estado'] if fila['Estado'].strip() else 'Aceptable',
                }
                libros_restaurados.append(libro)
        self.escribir_archivo(libros_restaurados)        


    def restaurar_ano(self,ano):
        if ano.strip() and ano.isdigit() and 1500 <= int(ano) <= 2024:
            return ano
        return '1970'   

    def escribir_archivo(self,libros):
        with open(self.archivo_salida, mode='w',newline='',encoding='utf-8') as file:
            campos = ['Título','Autor','Año','Precio','Cantidad','Estado']
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            writer.writerows(libros)
        print('\nÉxito!')    
        print(f'\nArchivo reparado guardado como "{self.archivo_salida}".')

archivo_corrupto = os.path.join(os.path.dirname(__file__), 'librosant.csv')
archivo_restaurado = os.path.join(os.path.dirname(__file__),'libros_restaurados.csv')

restaurador = RestauradorLibros(archivo_corrupto, archivo_restaurado)
restaurador.restaurar()

