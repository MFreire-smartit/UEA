# Tarea Semana 12 - Reserva de asiento en sala de cine
# Autor: Freire Shiguango Michael Daniel

# Matriz de asientos: 3 filas por 4 columnas, todos libres (0)
asientos = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

# Pedimos al usuario la fila y columna del asiento que quiere reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Marcamos el asiento como reservado (1)
asientos[fila][columna] = 1

# Mostramos el estado de la sala usando dos bucles anidados
print("Estado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
