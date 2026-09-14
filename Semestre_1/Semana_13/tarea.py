# Tarea Semana 13 - crear una función basada en un problema de la vida real
# Autor: Freire Shiguango Michael Daniel

def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

if __name__ == "__main__":
    precio = 10
    cantidad = 3
    resultado = calcular_total(precio, cantidad)
    print(f"El total de la compra es: {resultado}")