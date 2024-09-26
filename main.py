# main.py
from utils import mensaje_bienvenida, mensaje_despedida, crear_barco, colocar_barcos, disparar
import numpy as np
import random

# Mostrar mensaje de bienvenida
mensaje_bienvenida()

# Crear el tablero
tablero = np.full((10,10), "_")

fila = random.randint(0,9)
columna = random.randint(0,9)
casilla_1 = (fila,columna)
orientacion = random.choice(["Vertical","Horizontal"])
print(casilla_1)
print(orientacion)

# Crear los barcos
mi_barco1 = crear_barco(2)
mi_barco2 = crear_barco(2)
mi_barco3 = crear_barco(2)
mi_barco4 = crear_barco(3)
mi_barco5 = crear_barco(3)
mi_barco6 = crear_barco(5)

lista_mis_barcos = [mi_barco1, mi_barco2, mi_barco3, mi_barco4, mi_barco5, mi_barco6]
lista_barcos_maquina = [mi_barco1, mi_barco2, mi_barco3, mi_barco4, mi_barco5, mi_barco6]

# Colocar los barcos en el tablero
tablero = colocar_barcos(lista_mis_barcos, tablero)

# Simulación de disparo (puedes cambiar las coordenadas según lo que necesites)
tablero = disparar((0, 0), tablero)
tablero = disparar((0, 1), tablero)
tablero = disparar((1, 1), tablero)

# Mostrar mensaje de despedida
mensaje_despedida()
