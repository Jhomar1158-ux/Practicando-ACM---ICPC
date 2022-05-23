# input:
# 3 baababacb
# ouput:
# aba

line = input("""Ingrese el tamaño de la contraseña y 
                la encriptación separados por un espacio: """).strip()
# Si recibimos una cadena VACÍA
while line == "":
    line = input().strip()
# Dividimos el TAMAÑO y la ENCRIPTACIÓN
line = line.split()
if len(line) == 2:
    n = int(line[0])
    text = line[1]
else:
    n = int(line[0])
    text = input().strip()
while text == "":
    text = input().strip()

# Creamos un Dicc para almacenar la cantidad 
# de substrings repetidos
freq_dic = {}
for i in range(len(text) - n + 1): #9-3+1=7
    # Recortamos de 3 en 3 (Tamaño en tamaño)
    substr = text[i:i+n] # text[0:3]
    if substr in freq_dic:
        # Si existe le sumamos 1
        freq_dic[substr] += 1
    # Si no existe le asignamos 1
    else:
        freq_dic[substr] = 1
# Usamos max para calcular el VALUE máximo de todos los ITEMS
# Usamos el atributo key - lambda para especificar el VALUE
key_max = max(freq_dic.keys(), key=(lambda k: freq_dic[k])) 
# imprimimos el resultado
print(key_max)