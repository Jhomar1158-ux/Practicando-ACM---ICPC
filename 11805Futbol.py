
cantidadDeCasos = int(input("Ingrese la cant. de casos: "))
# Iteramos la cantidad de casos que ingresamos
for i in range(cantidadDeCasos):
    # separamos 
    N, K, P = list(map(int, input().split()))
    print(N)
    print(K)
    print(P)
    # Definiendos variables explícitas
    cantidadDeJugadores=N 
    primerPaseDeParreira=K
    cantidadDePases=P
    # Calculamos el resto para indentificar
    # la posición del jugador que da el pase
    # final.
    suma=(primerPaseDeParreira + cantidadDePases)
    jugadorQueDioElPaseParreira = suma % cantidadDeJugadores
    # Si la cantidad de pases termina en
    # el último jugador, entonces este vale N
    if jugadorQueDioElPaseParreira == 0:
        jugadorQueDioElPaseParreira = cantidadDeJugadores # N 
    print(f'Case {i+1}: {jugadorQueDioElPaseParreira}')


