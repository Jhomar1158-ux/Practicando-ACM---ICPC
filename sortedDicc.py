dicc = {
    "aaaa":22,
    "bbb":33,
    "fff":1,
    "cc":2,
}
var= sorted(dicc.items()) #Me devuelve una lista ordenada
print(var)
for val,key in var:
    print(val, key)