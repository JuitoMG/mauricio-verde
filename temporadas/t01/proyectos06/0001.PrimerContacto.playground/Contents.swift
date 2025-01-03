// import UIKit
var greeting = "Hello, playground"

// variables

var nombre = "Juan"

// Constante

let pi = 3.14

//Imprimir qué hay dentro de una variable

var perro = "Chiguagua"
print(perro)

perro = "Pitbull"
print(perro)

perro = "Boxer"
print(perro)


// Strings

let cita = "Cuando te llamé se me cayó el teléfono \"fijo\" al suelo"
print(cita)

let citaDeTresLineas = """
El otro día
imprimí varias líneas
en un mismo String
"""

//Contar los caracteres de un string
let nameLength = cita.count
print(nameLength)
print(cita.uppercased())

let filename = "1.jpg"
print(filename.hasSuffix(".jpg"))

// Números

let edad = 33

let numeroGigante = 1_000_000_000
print(numeroGigante)

let sumaDeCosas = edad + 10
print(sumaDeCosas)

var contador = 10
contador = contador + 5
print(contador)

//Alternativa

contador += 5

let numero120 = 120
print(numero120.isMultiple(of: 3))

//Swift no permite mezclar tipos de variable numéricas, hay que indicarlo de forma especial

let a = 1
let b = 2.0
// let c = a + b
let c = a + Int(b)
 //O también
let d = Double(a) + b



