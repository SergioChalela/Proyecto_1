from utils import mensaje_bienvenida, mensaje_despedida, crear_tablero, colocar_barcos, mostrar_tablero, turno_jugador, turno_maquina

def main():
    mensaje_bienvenida()

    # Crear los tableros
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()

    # Colocar los barcos
    print("Colocando barcos del jugador...")
    colocar_barcos(lista_mis_barcos, tablero_jugador)
    mostrar_tablero(tablero_jugador)

    print("Colocando barcos de la máquina...")
    colocar_barcos(lista_barcos_maquina, tablero_maquina)

    # Turnos de disparo
    for _ in range(5):
        print("Turno del jugador:")
        turno_jugador(tablero_maquina)
        mostrar_tablero(tablero_maquina)

        print("Turno de la máquina:")
        turno_maquina(tablero_jugador)
        mostrar_tablero(tablero_jugador)

    mensaje_despedida()

if __name__ == "__main__":
    main()
