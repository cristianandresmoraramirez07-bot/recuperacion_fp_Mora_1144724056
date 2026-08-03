## Bug 1:
- ¿Qué intentaba hacer? Validar que el monto fuera número
- ¿Qué error apareció? ValueError al ingresar letras
- ¿Cómo lo soluciono? Usé try/except en la función validar_monto
- ¿Cuánto tiempo le tomó? me tomo un tiempo cercano a los 4 minutos mientras trata de evitar que los numeros se refundieran con las letras

## Bug 2:
- ¿Qué intentaba hacer? Que el menú se repitiera
- ¿Qué error apareció? El programa se cerraba después de 1 opción
- ¿Cómo lo soluciono? Puse el menú dentro de while True
- ¿Cuánto tiempo le tomó? me tomo aproximadamente 4 minutos lograr que no se cerra solo al cambiar mi metodo para el menu

## Bug 3:
- ¿Qué intentaba hacer? Sumar total
- ¿Qué error apareció? El total siempre daba 0
- ¿Cómo lo soluciono? Me faltaba el caso base en la función recursiva
- ¿Cuánto tiempo le tomó? me tomo un tiempo aproximado de 6 minutos revisando donde estaba el error de recursividad al ser un tema aun no domino

## Bug 4:
- ¿Qué intentaba hacer? hacer que se guardaran los nuevos giros con lo_que_eligio()
- ¿Qué error apareció? SintaxError
- ¿Cómo lo soluciono? en la linea que era de un elif cuyo valor era 2 al corresponder la opcion 2 del programa pero solo puse un = y no 2 iguales (==)
- ¿Cuánto tiempo le tomó? me tomo 2 miniutos mientras revisa que habia hecho mal y me di cuenta que coloque solo un signo igual y no 2
