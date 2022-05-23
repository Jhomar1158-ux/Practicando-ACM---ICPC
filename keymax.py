freq_dic={
    "hola":4,
    "ff":5,
    "r":3,
}
key_max = max(freq_dic.keys(), key=(lambda k: freq_dic[k]))
# print(key_max)

nst = [ [1001, 0.0009], [1005, 0.07682], [1201, 0.57894], [1677, 0.0977] ]

valMax = max(nst, key=(lambda i:i[0]))

print(valMax)

# COMPRENDIENTO LO VISTO CON MAX y KEY

diccNotas = {
    "jhomar":13,
    "elias":18,
    "cristian":12,
    "asthero":19
}
# Si quiero obtener el item con mayor nota puedo usar MAX con Key
var2, itemMax = max(diccNotas, key=(lambda i:diccNotas[i]))
print(itemMax)
print(var2)