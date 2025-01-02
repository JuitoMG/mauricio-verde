'''
--- REGISTRO DE MASCOTAS ---

Funcionamiento: Programa que permite agregar mascotas a la
base de datos de un refugio, actualizar sus datos, buscar 
un mascota según parámetros y mostrar la lista entera de 
mascotas.

'''



import sqlite3
import os


class RegistroMascotas:

    dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(dir,'refugio_mascotas.db')

    def __init__(self, db_name=ruta):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mascotas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,            
                edad INTEGER NOT NULL,
                estado TEXT NOT NULL CHECK(estado IN('En adopción','Adoptado'))                        
            )
        ''')
        self.conn.commit()

    def agregar_mascota(self, nombre, tipo, edad, estado):
        self.cursor.execute('''
            INSERT INTO mascotas (nombre, tipo, edad, estado)
            VALUES (?, ?, ?, ?)
        ''',(nombre, tipo, edad, estado))
        self.conn.commit()
        print(f'\nMascota {nombre} registrada con éxito.')

    
    def buscar_mascota(self, criterio, valor):
        consulta = f'SELECT * FROM mascotas WHERE {criterio} LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        resultados = self.cursor.fetchall()
        if resultados:
            print('\nMascotas encontradas: \n')
            for mascota in resultados:
                print(f'ID: {mascota[0]}, Nombre: {mascota[1]}, Tipo: {mascota[2]}, Edad: {mascota[3]}, Estado: {mascota[4]}')
        else:
            print('\nNo se encontraron mascotas con ese criterio.')

    def actualizar_estado(self, id_mascota, nuevo_estado):
        self.cursor.execute('''
            UPDATE mascotas
            SET estado = ?
            WHERE id = ?
        ''',(nuevo_estado,id_mascota))
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print(f'\nEstado de la mascota con ID {id_mascota} actualizado a {nuevo_estado}')
        else:
            print(f'\nNo se encontró ninguna mascota con ID {id_mascota}')

    def listar_mascotas(self):
        self.cursor.execute('SELECT * FROM mascotas ORDER BY nombre ASC')
        mascotas = self.cursor.fetchall()
        print('\nLista de mascotas: \n')
        for mascota in mascotas:
            print(f'ID: {mascota[0]}, Nombre: {mascota[1]}, Tipo: {mascota[2]}, Edad: {mascota[3]}, Estado: {mascota[4]}')  

    def cerrar(self):
        self.conn.close()


#Menú

def menu():
    registro = RegistroMascotas()
    while True:
        print('\n--- Refugio de mascotas ---\n')
        print('1. Registrar mascota nueva')
        print('2. Buscar mascota')
        print('3. Actualizar estado de mascota')
        print('4. Listar todas las mascotas')
        print('5. Salir')
        opcion = input('\nElige una opción ') 

        if opcion == '1':
            nombre= input('\nNombre de la mascota: ')
            tipo = input('\nTipo de mascota (Perro, Gato, etc): ')
            while True:
                try:
                    edad = int(input('\nEdad de la mascota en años: '))
                    break
                except ValueError:
                    print('\nPor favor, ingresa un número válido para la edad.')
            estado = input('\nEstado de la mascota (En adopción, Adoptado): ')
            if estado not in ['En adopción, Adoptado']:
                print('\nEstado inválido. Inténtelo de nuevo.')
            else:
                registro.agregar_mascota(nombre,tipo,edad,estado)

        elif opcion == '2':
            print('\nBuscar por: ')
            print('1. Nombre')
            print('2. Tipo')
            print('3. Estado')   
            criterio = input('\nElige el criterio de búsqueda: ')
            if criterio == '1':
                valor = input('\nIntroduce el nombre: ')
                registro.buscar_mascota('nombre',valor)
            elif criterio == '2':
                valor = input('\nIntroduce el tipo: ')
                registro.buscar_mascota('tipo',valor)
            elif criterio == '3':
                valor = input('\nIntroduce el estado (En adopción, Adoptado): ')
                registro.buscar_mascota('estado',valor)
            else:
                print('\nCriterio inválido.')         

        elif opcion == '3':
            try:
                id_mascota = int(input('\nID de la mascota a actualizar: '))
                nuevo_estado = input('\nNuevo estado (En adopción, Adoptado): ')
                if nuevo_estado not in ['En Adopción','Adoptado']:
                    print('\nEstado inválido. Inténtalo de nuevo. (En adopción - Adoptado)')
                else:
                    registro.actualizar_estado(id_mascota,nuevo_estado)
            except ValueError:
                print('\nPor favor, ingresa un ID válido.') 

        elif opcion == '4':
            registro.listar_mascotas()

        elif opcion == '5':
            print('\nSaliendo del programa...')
            registro.cerrar()
            break
        else:
            print('\nOpción inválida. Inténtalo de nuevo.')

if __name__ == '__main__':
    menu()                
                     


