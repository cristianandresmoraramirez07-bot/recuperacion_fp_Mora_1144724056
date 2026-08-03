# Tabla de Seguimiento
- **Estudiante: Cristian Mora** 

- **Cédula: 1144724056**

| Iteración | i | ventas[i] | total | dias |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 200000 | 200000 | 1 |
| 2 | 2 | 0 | 200000 | 1 |
| 3 | 3 | 350000 | 550000 | 2 |
| 4 | 4 | 400000 | 950000 | 3 |
| 5 | 5 | 120000 | 1070000 | 4 |
| 6 | 6 | 250000 | 1320000 | 5 |
| 7 | 7 | **Error (IndexError)** | - | - |

# Codigo sin correciones:
```
ventas = [150000, 200000, 0, 350000, 400000, 120000, 250000]
total = 0
dias = 0
for i in range(1, 8):
 if ventas[i] > 0:
 total = total + ventas[i]
 dias = dias + 1
promedio = total / dias
print("El promedio de ventas es: ", promedio)
```


## Error identficado
- **El error identificado en el codigo es:** Las listas se indexan desde la oposicion 0. al iniciar en 1, se  ignora el primer valor(ventas[0] = 150000).



## Ciclo reescrito con while:
```
ventas = [150000, 200000, 0, 350000, 400000, 120000, 250000]
total = 0
dias = 0
i = 0

while i < len(ventas):
    if ventas[i] > 0:
        total = total + ventas[i]
        dias = dias + 1
    i = i + 1 

if dias > 0:
    promedio = total / dias
    print("El promedio de ventas: ", promedio)
else:
    print("No hay dias sin ventas")
```