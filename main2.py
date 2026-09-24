"""Juego de tres en raya para dos jugadores en la consola."""


def mostrar_tablero(tablero):
	print("\n     |     |     ")
	print(f"  {tablero[0]}  |  {tablero[1]}  |  {tablero[2]}")
	print("_____|_____|_____")
	print("     |     |     ")
	print(f"  {tablero[3]}  |  {tablero[4]}  |  {tablero[5]}")
	print("_____|_____|_____")
	print("     |     |     ")
	print(f"  {tablero[6]}  |  {tablero[7]}  |  {tablero[8]}\n")


def hay_ganador(tablero, jugador):
	combinaciones = (
		(0, 1, 2), (3, 4, 5), (6, 7, 8),
		(0, 3, 6), (1, 4, 7), (2, 5, 8),
		(0, 4, 8), (2, 4, 6),
	)
	return any(all(tablero[posicion] == jugador for posicion in linea)
			   for linea in combinaciones)


def jugar():
	tablero = [str(numero) for numero in range(1, 10)]
	jugador = "X"

	print("=== TRES EN RAYA ===")
	print("Elige una posición del 1 al 9. Escribe 'q' para salir.")

	while True:
		mostrar_tablero(tablero)
		entrada = input(f"Turno de {jugador}: ").strip().lower()

		if entrada == "q":
			print("¡Hasta pronto!")
			return
		if not entrada.isdigit() or not 1 <= int(entrada) <= 9:
			print("Entrada no válida. Elige un número del 1 al 9.")
			continue

		posicion = int(entrada) - 1
		if tablero[posicion] in ("X", "O"):
			print("Esa posición ya está ocupada.")
			continue

		tablero[posicion] = jugador
		if hay_ganador(tablero, jugador):
			mostrar_tablero(tablero)
			print(f"¡Gana el jugador {jugador}!")
			return
		if all(casilla in ("X", "O") for casilla in tablero):
			mostrar_tablero(tablero)
			print("¡Empate!")
			return

		jugador = "O" if jugador == "X" else "X"


if __name__ == "__main__":
	jugar()
