import operator as op


c = "jhomar"
t = (1,2,3,4,50)
d = {
    "nombre":"Elias",
    "edad":22,
}
# Para cadenas y tuplas acepta el indice
elementos = op.itemgetter(2,4)
print(elementos(t))

# Para diccionarios acepta la clave
elementoDicc = op.itemgetter("nombre")
print(elementoDicc(d))

listDicc = [
    {"nombre":"jhomar", "apellido": "astuyauri", "edad":22},
    {"nombre":"elias", "apellido": "estuyauri", "edad":23},
    {"nombre":"cristian", "apellido": "istuyauri", "edad":21},
    {"nombre":"asthero", "apellido": "hstuyauri", "edad":99}
]

def ordenarApellido(listDicc):
    return sorted(listDicc, key=op.itemgetter("edad"))


# Ordenamos la siguiente lista por orden de apellido
print(ordenarApellido(listDicc))