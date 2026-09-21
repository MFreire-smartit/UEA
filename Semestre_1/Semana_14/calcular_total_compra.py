IVA = 0.15

def calcular_total_compra(precio_unitario, cantidad):
    subtotal = precio_unitario * cantidad
    valor_iva = subtotal* IVA
    total = subtotal + valor_iva
    return total

producto = input("Nombre del Producto; ")
precio = float(input("Precio unitario ($): "))
unidades = int(input("Cantidad de unidades: "))

total_a_pagar = calcular_total_compra(precio, unidades)

print(f"Compra: {unidades} * {producto}")
print(f"Total a pagar (con IVA): ${total_a_pagar:.2f}")