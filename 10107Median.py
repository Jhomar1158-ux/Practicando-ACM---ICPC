# a = []

# while True:
# 	try:
# 		a.append(int(input()))
# 	except EOFError:
# 		break
	
# 	a.sort()
# 	half = len(a) // 2
# 	print( int( (a[half] + a[~half]) / 2 ) )

from sys import stdin, stdout
# Ordenamos los elementos de menor a mayor
def binary_search(n, key):
    low = 0
    high = n - 1
    while low < high:
        middle = (low + high) // 2
        if lst[middle] <= key:
            low = middle + 1
        else:
            high = middle
    return low

sizeNumbers=int(input("Tamaño de nums: "))+2
# Solicitamos un número al usuario
lines = stdin.readlines(sizeNumbers)
lst = []
size = 0
ans = '' #Almacenamos la respuesta como string
for s in lines:
    num = int(s)
    size += 1
    # Ordenamos los elementos
    idx = binary_search(size, num)
    # Ubicamos cada elemento ordenamos en la lista "lst"
    lst.insert(idx, num)
    mid = size // 2
    # Si el tamaño ingresado es impar(debido a que empieza en 1)
    if size % 2:
        ans += str(lst[mid])
    # Si es par, es la suma de los 2 del medio
    else:
        ans += str((lst[mid] + lst[mid - 1]) // 2)
    # Le damos un salto de línea a cada respuesta
    ans += '\n'
stdout.write("La respuesta es: \n")
stdout.write(ans) #Podemos usar "print(ans)" también