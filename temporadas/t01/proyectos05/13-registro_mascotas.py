import sqlite3
import os

class RegistroMascotas:
    def __init__(self, db_name='refugio_mascotas.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXIST mascotas (
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
    