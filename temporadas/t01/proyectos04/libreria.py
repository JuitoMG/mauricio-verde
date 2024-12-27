"""
--- REGRISTRO DE LIBROS ---

Programa que permite gestionar una pequeña base de datos de libros, añadiendo
nuevos libros, modificando datos de los ya existentes, buscando por nombre
o autor, o mostrando directamente todos los libros ordenados.

Funcionamiento:

1.Elegir una opción del menú:
2. Se puede agregar un libro nuevo rellenando los campos solicitados,
hacer una búsqueda de un libro o de los que tiene un autor, actualizar
datos de un libro o mostrar todos. La última opción cierra el programa. 

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

#Validaciones

def val_ano(ano):
    if not ano.isdigit() or int(ano) < 0 or int (ano) > 2024:
        raise ValueError('\nError: Ingresa un año válido.')

def val_precio(precio):
    try:
        precio = float(precio)
        if precio < 0:
            raise ValueError('\nError: El precio tiene que ser positivo.')
    except ValueError:
        raise ValueError('\nEl precio debe ser un número válido.') 

def val_cantidad(cantidad):
    if not cantidad.isdigit() or int(cantidad) < 0:
        raise ValueError('\nIngresa una cantidad válida.')  

def val_estado(estado):
    estados = ['Nuevo','Bueno','Aceptable']
    if estado not in estados:
        raise ValueError('\nIngresa un estado válido: nuevo, bueno, aceptable')   

def val_campo(campo, nombre):
    if not campo.strip():
        raise ValueError(f'El campo "{nombre}" no puede estar vacío')



#Menú
                                           
def menu():
    libreria = Libreria()
    while True:
        print('\n-- LIBRERÍA SEGUNDA MANO --')
        print('1. Registrar un libro nuevo')
        print('2. Buscar un libro por título o autor')
        print('3. Actualizar información de un libro')
        print('4. Ver todos los libros')
        print('5. Salir')
        opcion = input('\nElige una opción: ')

        if opcion == '1':
            try:
                titulo = input('\nTítulo del libro: ')
                val_campo(titulo, 'Título')
                autor = input('\nAutor del libro: ')
                val_campo(autor, 'Autor')  
                ano = input('\nAño de publicación: ') 
                val_ano(ano) 
                precio = input('\nPrecio del libro: ')
                val_precio(precio)  
                cantidad = input('\nCantidad disponible: ')  
                val_cantidad(cantidad)
                estado = input('\nEstado del libro (Nuevo, Bueno, Aceptable): ')
                val_estado(estado)
                nuevo_libro = Libro(titulo,autor,ano,precio,cantidad,estado)
                libreria.registrar_libro(nuevo_libro)
            except ValueError as e:
                print(f'\nError: {e}')    

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
            try:
                nuevo_titulo = input('\nTítulo nuevo: ')
                val_campo(nuevo_titulo, 'Nuevo título')
                nuevo_autor = input('\nAutor nuevo: ')
                val_campo(nuevo_autor, 'Nuevo autor')
                nuevo_ano = input('\nAño nuevo: ')
                val_ano(nuevo_ano)
                nuevo_precio = input('\nPrecio nuevo: ')
                val_precio(nuevo_precio)
                nueva_cantidad = input('\nNueva cantidad: ')
                val_cantidad(nueva_cantidad)
                nuevo_estado = input('\nNuevo estado (Nuevo, Seminuevo, Aceptable): ')
                val_estado(nuevo_estado)

                nuevos_datos = [nuevo_titulo, nuevo_autor, nuevo_ano, nuevo_precio, nueva_cantidad, nuevo_estado]
                libreria.actualizar_libro(titulo_libro, nuevos_datos)
            except ValueError as e:
                print(f'\nError: {e}')    

        elif opcion == '4':
            libreria.imprimir_libros()

        elif opcion == '5':
            print('\nSaliendo del programa...')
            break

        else:
            print('\nOpción no encontrada. Inténtelo de nuevo')    

if __name__ == '__main__':
    menu()            



                 