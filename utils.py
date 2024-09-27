import numpy as np
import random

def mensaje_bienvenida():
    print("Bienvenidos al juego con fallos de Barcos!!!")
mensaje_bienvenida()

mensaje_bienvenida()

tablero = np.full((10,10), "_")

fila = random.randint(0,9)
columna = random.randint(0,9)
casilla_1 = (fila,columna)
orientacion = random.choice(["Vertical","Horizontal"])
print(casilla_1)
print(orientacion)

def crear_barco(eslora):
    casilla_0 = (random.randint(0, 9), random.randint(0, 9))
    orientacion = random.choice(["Vertical", "Horizontal"])

    barco = [casilla_0]
    casilla = casilla_0
    
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0] + 1, casilla[1])  # Vertical
            barco.append(casilla)
        else:
            casilla = (casilla[0], casilla[1] + 1)  # Horizontal
            barco.append(casilla)
    
    return barco

mi_barco1 = crear_barco(2)
mi_barco2 = crear_barco(2)
mi_barco3 = crear_barco(2)
mi_barco4 = crear_barco(3)
mi_barco5 = crear_barco(3)
mi_barco6 = crear_barco(5)

lista_mis_barcos = [mi_barco1, mi_barco2, mi_barco3, mi_barco4, mi_barco5, mi_barco6]
lista_barcos_maquina = [mi_barco1, mi_barco2, mi_barco3, mi_barco4, mi_barco5, mi_barco6]

def casillas_libres(barco, tablero):
    for casilla in barco:
        fila, columna = casilla 
        if fila < 0:    
            return False
        elif fila >= len(tablero):  
            return False
        elif columna < 0:   
            return False
        elif columna >= len(tablero):  
            return False
        if tablero [fila, columna] != "_": 
            return False
        tablero[fila,columna] = "O"
    return True

def colocar_barcos(lista_mis_barcos, tablero):
    for barco in lista_mis_barcos:
        if casillas_libres(barco,tablero):
            print("Casilla libre")
            for casilla in barco:
                fila,columna = casilla
                tablero[fila,columna] = "O"
        else:
            print("Casilla no libre, generando nuevo barco")
            nuevo_barco = crear_barco(len(barco))

            if casillas_libres(nuevo_barco, tablero):
                print("Nuevo barco")
                for casilla in nuevo_barco:
                    fila,columna = casilla
                    tablero[fila,columna] = "O"
            else:
                print("Nuevo barco no puede proceder")
    return tablero 

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero

def mensaje_despedida():
    print("Gracias por jugar. Regresa en 12 semanas a jugar FIFA!!! con fallos")
mensaje_despedida()