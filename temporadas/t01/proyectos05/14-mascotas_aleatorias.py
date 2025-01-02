"""
Este programa únicamente añade una lista aleatoria de mascotas
a la base de datos de refugio_mascotas.db

"""


import sqlite3
import os

dir = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(dir,'refugio_mascotas.db')

conn = sqlite3.connect(ruta)
cursor = conn.cursor()

mascotas = [
    ("Max", "Perro", 5, "En adopción"),
    ("Luna", "Gato", 3, "Adoptado"),
    ("Charlie", "Perro", 2, "En adopción"),
    ("Bella", "Conejo", 1, "En adopción"),
    ("Rocky", "Perro", 6, "Adoptado"),
    ("Daisy", "Gato", 4, "En adopción"),
    ("Cooper", "Hámster", 2, "Adoptado"),
    ("Coco", "Perico", 3, "En adopción"),
    ("Bailey", "Perro", 7, "Adoptado"),
    ("Oliver", "Gato", 5, "En adopción"),
    ("Lily", "Conejo", 2, "En adopción"),
    ("Milo", "Perro", 4, "Adoptado"),
    ("Ruby", "Hámster", 1, "En adopción"),
    ("Tucker", "Perro", 3, "Adoptado"),
    ("Lucy", "Gato", 6, "En adopción"),
    ("Rosie", "Conejo", 1, "En adopción"),
    ("Buddy", "Perro", 8, "Adoptado"),
    ("Jasper", "Gato", 7, "En adopción"),
    ("Willow", "Conejo", 3, "Adoptado"),
    ("Teddy", "Perro", 5, "En adopción"),
    ("Mia", "Gato", 2, "Adoptado"),
    ("Finn", "Perro", 4, "En adopción"),
    ("Sadie", "Gato", 5, "Adoptado"),
    ("Oscar", "Conejo", 2, "En adopción"),
    ("Ruby", "Perico", 6, "Adoptado"),
    ("Chloe", "Hámster", 1, "En adopción"),
    ("Archie", "Perro", 3, "En adopción"),
    ("Zoe", "Gato", 4, "Adoptado"),
    ("Jack", "Perro", 7, "En adopción"),
    ("Hazel", "Conejo", 2, "Adoptado")
]

cursor.executemany('''
    INSERT INTO mascotas (nombre, tipo, edad, estado)
    VALUES (?,?,?,?)
''',mascotas)

conn.commit()
print('\nMascotas aleatorias añadidas con éxito')
conn.close()