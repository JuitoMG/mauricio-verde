
# find() retorna la posición de la primera similitud de la substring

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no"
print(cadenaDeTexto.find('quien'))
#Devolvería 52

#---------------------------------------------------------------------------------

# rfind() retorna la última posición de la similitud de la substring

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no"
print(cadenaDeTexto.rfind('quien'))
#Devolvería 94

#---------------------------------------------------------------------------------

# replace devuelve una cadena donde un valor especificado se reemplaza con un valor especificado

miString = "Esto es bonito. Esto es bueno."
newString = miString.replace("es","FUE")
print(newString)

#Devolvería Esto FUE bonito. Esto FUE bueno.


#TRABAJAR CON STRINGS
'''
Los Strings son secuencias de caracteres de texto.
Todos los objetos en Python se engloban en Mutables o inmutables
Los tipos básicos mutables son las listas, los diccionarios y los sets
Los tipos básicos inmutables son los números, los strings y las tuplas
Los objetos mutables pueden ser cambiados en el mismo objeto, los inutables no
'''

#Concatenar textos con + o coma. Con la coma añade un espacio, con el + no.

#Concatenacion y multiplicación de strings

a= "uno"
b = "dos"
c = a+b     # c es "unodos"
c = a * 3   # c es "unounouno"

#METODOS CON STRINGS

#lower(): Convierte a minúsculas
texto = "BlabLAblA"
print(texto.lower())

# capitalice(): Pone la primera letra mayúscula
# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres
# find(): Indica el índice en el que está un caracter o grupo de caracteres
# rfind(): Igual que find() pero contando desde atrás
# isdigit(): Devuelve un booleano diciendo si el valor es un String. Entre comillas o dará error.
# isalum(): Devuelve verdadero si todos los caracteres son numéricos y hay al menos un caracter. Sino devuelve falso
# isalpha(): Comprueba si hay solo letras. Los espacios no cuentan
# split(): Separa las palabras utilizando espacios. Crea una lista. Se puede separar con coma split(',')
# strip(): Borra espacios sobrantes al prinicpio y al final
# replace(): Cambia una palabra o letra por otra
