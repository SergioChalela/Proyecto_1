import numpy as np
import random

def mensaje_bienvenida():
    print("Bienvenidos al juego con fallos de Barcos!!!")

def crear_tablero(tamaño=10):
    return np.full((tamaño, tamaño), "_")

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

def crear_barco(eslora):
    orientacion = random.choice(["Vertical", "Horizontal"])
    
    if orientacion == "Vertical":
        fila_inicial = random.randint(0, 10 - eslora)
        columna_inicial = random.randint(0, 9)
        barco = [(fila_inicial + i, columna_inicial) for i in range(eslora)]
    else:
        fila_inicial = random.randint(0, 9)
        columna_inicial = random.randint(0, 10 - eslora)
        barco = [(fila_inicial, columna_inicial + i) for i in range(eslora)]

    return barco

def casillas_libres(barco, tablero):
    for casilla in barco:
        fila, columna = casilla 
        if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero):
            return False
        if tablero[fila, columna] != "_": 
            return False
    return True

def colocar_barco(barco, tablero):
    if casillas_libres(barco, tablero):
        for casilla in barco:
            fila, columna = casilla
            tablero[fila, columna] = "O"
        return True
    return False

def colocar_barcos(lista_barcos, tablero):
    for barco in lista_barcos:
        intentos = 0
        colocado = False
        while not colocado and intentos < 10:
            colocado = colocar_barco(barco, tablero)
            if not colocado:
                barco = crear_barco(len(barco))
            intentos += 1
        if not colocado:
            print("Error: No se pudo colocar el barco después de 10 intentos.")
    return tablero

def disparar(casilla, tablero):
    fila, columna = casilla
    if tablero[fila, columna] == "O":
        print("Tocado")
        tablero[fila, columna] = "X"
    else:
        print("Agua")
        tablero[fila, columna] = "A"
    return tablero

def turno_jugador(tablero):
    fila = int(input("Introduce la fila (0-9): "))
    columna = int(input("Introduce la columna (0-9): "))
    casilla = (fila, columna)
    disparar(casilla, tablero)

def turno_maquina(tablero):
    fila = random.randint(0, 9)
    columna = random.randint(0, 9)
    casilla = (fila, columna)
    print(f"La máquina dispara a {casilla}")
    disparar(casilla, tablero)

def mensaje_despedida():
    print("Gracias por jugar. Regresa en 12 semanas a jugar FIFA!!! con fallos")

