"""
Lista: Colección ordenada y modificable. 
Se escriben entre corchetes.
"""

miLista = ['Juan', 33, 'Pontevedra']
miLista2 = [22, True, 'listaaa', [1,2]]

#MÉTODOS DE LAS LISTAS

#Hacer una lista de una cadena
miLista = list('Python')
print(miLista)

#Acceder a elementos de una lista
print(miLista[0])

miLista = [[1,2],[3,4],[5,6]]
miVar = miLista[1,1]
print(miVar)

#Función con una lista como parámetro
def miFunción(listaFrutas):
    for x in listaFrutas:
        print(x)

frutas = ['manzana', 'plátano', 'cereza']
miFunción(frutas)

#TUPLAS
#Colección ordenada e inmutable. Entre paréntesis.

miTupla = ('manzana','plátano','fresa')
print(miTupla[1])

#Otra forma de declararla
miTupla = tuple(('manzana','plátano','fresa'))

#Indexación negativa
miTupla[-1]

#Devuelve elementos concretos
miTupla[2:3]

#Convertir tupla en lista para poder cambiarla

miLista = list(miTupla)
miLista[1] = 'kiwi'
miTupla = tuple(miLista)
print(miTupla)

#Recorrer tupla

for x in miTupla:
    print(x)

#Comprobar si existe un elemento

if 'kiwi' in miTupla:
    print('Sí, está')

#O también

print('kiwi' in miTupla)

#Longitud Tupla
print(len(miTupla))

#Unir dos tuplas
tupla1= ('a','b','c')
tupla2=(1,2,3)

tupla3 = tupla1+tupla2
print(tupla3)

#Desempaquetando tupla
laTupla= ('Juan', 33, 70,True)
nombre, edad, peso, hombre = laTupla
print(nombre)
print(edad)
print(peso)
print(hombre)