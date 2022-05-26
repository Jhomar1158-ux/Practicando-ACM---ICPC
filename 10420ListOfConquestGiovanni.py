# Ingresamos la cantidad de mujeres de Giovanni
cantMujeres = int(input())
# Creamos un diccionario para contabilizar por pais
dicc={}
# iteramos la cantidad de mujeres
for i in range(cantMujeres):
    # Elejimos el primer valor de la lista como pais
    pais = list(input().split())[0]
    print(type(pais))
    
    # Incializamos valores
    if pais in dicc:
        dicc[pais]+=1
    else: 
        dicc[pais]=1
    print(dicc) 
    # Ordenamos con sorted
    for key,val in sorted(dicc.items()):
        print(f'{key} {val}')



