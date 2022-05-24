numbers = "2 3 4"
# map -> Devuelve un Objeto
result = map(int, numbers)
print( numbers.split())
resultList=list(map(int, numbers.split()))
print(resultList)

numbers2= [1,2,3,4]
# map(funcion, iterable -> Lista, String, tupla)
result2 = map(lambda x: x+3, numbers2)
print(list(result2))

