"""
--- REGRISTRO DE LIBROS ---

"""

import os
import csv

class Libro:
    def __init__(self, titulo, autor, ano, precio, cantidad, estado):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.precio = precio
        self.cantidad = cantidad
        self.estado = estado

    def __str__(self):
        return f'"{self.titulo}", por {self.autor} ({self.ano}) - {self.estado} - {self.precio}€ - {self.cantidad} unidades.'


class Libreria:

    dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir,'libreria.csv')

    def __init__(self, archivo=ruta):
        self.archivo = archivo

    def registrar_libro(self, libro):
        with open(self.archivo,mode='a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([libro.titulo, libro.autor, libro.ano, libro.precio, libro.cantidad, libro.estado])
        print(f'\nLibro "{libro.titulo}" registrado con éxito.')
    
    def buscar_libro(self, criterio):
        resultados = []
        with open(self.archivo, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for fila in reader:
                if criterio.lower() in ','.join(fila).lower():
                    resultados.append(Libro(*fila))
        return resultados
    
    
    def actualizar_libro(self, titulo_libro,nuevos_datos):
        libros = []
        encontrado = False
        with open(self.archivo, mode='r',encoding='utf-8') as file:
            reader = csv.reader(file)
            for fila in reader:
                if fila[0].lower == titulo_libro.lower():
                    libros.append(nuevos_datos)
                    encontrado = True
                else:
                    libros.append(fila)

        if encontrado:
            with open(self.archivo, mode='w', newline='', encoding='uft-8') as file:
                writer = csv.write(file)
                writer.writerows(libros)
            print(f'\nLibro "{titulo_libro}" actualizado con éxito.')
        else:
            print(f'\nLibro "{titulo_libro}" no encontrado')
    
    def imprimir_libros(self):
        libros = []
        with open(self.archivo, mode='r',newline='',encoding='utf-8') as file:
            reader = csv.reader(file)
            for fila in reader:
                libros.append(Libro(*fila))
        
        ordenar = sorted(libros, key=lambda libro: libro.autor.lower())
        print('\nLista de libros: \n')  
        for libro in ordenar:
            print(libro)        


#Menú
                                           
def menu():
    libreria = Libreria()
    while True:
        print('\n-- LIBRERÍA SEGUNDA MANO --')
        print('1. Registrar un libro nuevo')
        print('2. Buscar un libro por título')
        print('3. Actualizar información de un libro')
        print('4. Ver todos los libros')
        print('5. Salir')
        opcion = input('\nElige una opción: ')

        if opcion == '1':
            titulo = input('\nTítulo del libro: ')
            autor = input('\nAutor del libro: ')  
            ano = input('\nAño de publicación: ')  
            precio = input('\nPrecio del libro: ')  
            cantidad = input('\nCantidad disponible: ')  
            estado = input('\nEstado del libro (Nuevo, Bueno, Aceptable): ')
            nuevo_libro = Libro(titulo,autor,ano,precio,cantidad,estado)
            libreria.registrar_libro(nuevo_libro)

        elif opcion == '2':
            criterio = input('\nIngrese el título o autor del libro: ')
            resultados = libreria.buscar_libro(criterio)
            if resultados:
                print('\nLibros encontrados: ')
                for libro in resultados:
                    print(libro)
            else:
                print('No se encontraron libros con ese título')

        elif opcion == '3':
            titulo_libro = input('\nTítulo del libro a actualizar: ')
            print('\nIngresa los datos nuevos')
            nuevo_titulo = input('\nTítulo nuevo: ')
            nuevo_autor = input('\nAutor nuevo: ')
            nuevo_ano = input('\nAño nuevo: ')
            nuevo_precio = input('\nPrecio nuevo: ')
            nueva_cantidad = input('\nNueva cantidad: ')
            nuevo_estado = input('\nNuevo estado (Nuevo, Seminuevo, Aceptable): ')
            nuevos_datos = [nuevo_titulo, nuevo_autor, nuevo_ano, nuevo_precio, nueva_cantidad, nuevo_estado]
            libreria.actualizar_libro(titulo_libro, nuevos_datos)

        elif opcion == '4':
            libreria.imprimir_libros()

        elif opcion == '5':
            print('\nSaliendo del programa...')
            break

        else:
            print('\nOpción no encontrada. Inténtelo de nuevo')    

if __name__ == '__main__':
    menu()            



                 