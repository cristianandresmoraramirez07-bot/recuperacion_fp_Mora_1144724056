ventas = [150000, 200000, 0, 350000, 400000, 120000, 250000]
total = 0
dias = 0

# Primer cambio: primero el rango era de (1, 8) asi que iniciaba en 1 en lugar de 0 lo que causaba que terminara en 7 salteando el primer elemento de la lista 0 (150000) lo que dejaba en error fuera de rango (IndexError) al intentar acceder a ventas[7]. se cambio por range(0, len(ventas)), la lista se recorre correctamente.

for i in range(0, len(ventas)):
    if ventas[i] > 0:
        total = total + ventas[i]
        dias = dias + 1

# Segundo cambio: se agrego un codigo que verifique el funcionamiento correcto antes de calcular el promedio para evitar que falle al intentar dividir 0.

if dias > 0:
    promedio = total / dias
# Tercer cambio: se encierra promedio en int() para eliminar el .0 decimal al ejecurar la terminal
    print("el promedio de ventas es:", int(promedio))
else:
    print("no hubo dias con ventas.")