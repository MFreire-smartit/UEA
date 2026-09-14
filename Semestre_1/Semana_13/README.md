# Cálculo del Total de una Compra

**Estudiante:** Freire Shiguango Michael Daniel

## Objetivo del programa

Resolver un problema sencillo de la vida real mediante una función: calcular
el total que debe pagar un cliente en una tienda según el precio de un
producto y la cantidad de unidades que lleva.

La función `calcular_total(precio, cantidad)` recibe los dos parámetros,
multiplica el precio por la cantidad y devuelve el resultado con `return`.
El bloque principal (`if __name__ == "__main__":`) llama a la función y
muestra el resultado en consola con `print()`.

## Pseudocódigo

```
FUNCION calcularTotal(precio, cantidad)
    total <- precio * cantidad
    RETORNAR total
FIN FUNCION

precio <- 10
cantidad <- 3
resultado <- calcularTotal(precio, cantidad)
IMPRIMIR resultado
```

## Cómo ejecutarlo

1. Tener Python 3 instalado.
2. Ejecutar en la terminal:

   ```
   python tarea.py
   ```

3. El programa muestra en consola el total de la compra calculado.
