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


#Diccionarios

#Declaración
miDiccionario = {
    "Marca":"Ford",
    "Modelo":"Fiesta",
    "Año": 2002
}
print(miDiccionario['Modelo'])

#Reasignar
miDiccionario['Marca'] = 'Opel'
print(miDiccionario)

#Usar una tupla en un diccionario

tuplaEnDic = {'nombre':'Alonso', 'Escudería':'Renault','Campeonatos':[2005,2006]}
print(tuplaEnDic['Campeonatos'])

#Quitar valores
miDiccionario.pop('Modelo')
print(miDiccionario)

#Crear diccionario a partir de dos listas

claves = ['Nombre','Apellido','Edad']
valores = ['Perico','De los Palotes',33]
datosUsuario = dict(zip(claves,valores))
print(datosUsuario)

#Comprobar si una clave está en un diccionario

'Nombre' in datosUsuario

#Imprime las claves del diccionario

for x in datosUsuario:
    print(datosUsuario[x])

#Longitud

print(len(datosUsuario))   

#Eliminar ultimo elemento insertado

coche = {
    'marca':'Ford',
    'modelo':'Mustang',
    'año':1964
}

del coche['modelo']
print(coche)

#Clear vacía el diccionario

coche.clear()
print(coche)

#Copiar diccionario

copiaDiccionario = datosUsuario.copy()
print(copiaDiccionario)

#Diccionarios anidados

pajaro1 = {
    'nombre':'Arcadio',
    'especie':'ninfa'
}

pajaro2 = {
    'nombre':'Melquíades',
    'especie':'ninfa'
}
pajaro3 = {
    'nombre':'Jacinta',
    'especie':'agaporni'
}
pajaro4 = {
    'nombre':'Benito',
    'especie':'agaporni'
}

mascotas = {
    'Animal1':pajaro1,
    'Animal2':pajaro2,
    'Animal3':pajaro3,
    'Animal4':pajaro4,
}
print(mascotas['Animal1'])
print(mascotas['Animal2'])
print(mascotas['Animal3'])
print(mascotas['Animal4'])