CUPOS_MAXIMOS = 56
giros_para_hoy = [] 

def revisar_dinero(texto_dinero):
    """1. Revisar el monto de dinero sea valor positivo y que sea un número"""
    try:
# Intentara pasar dinero a decimal, si no puede, mostrara un mensaje de error y retornara None
        numero = float(texto_dinero)
        if numero > 0:
            return numero
        else:
            print("Monto menor a 0 no esta disponible, agregue un monto mayor a 0.")
            return None
    except ValueError:
# Si no puede convertir el texto a número, mostrara un mensaje de error y retornara None
        print("Caracter equivocado, la terminal solo funciona con números.")
        return None

def agregar_nuevo_giro():
    """2. Agrega un nuevo giro a la lista de giros, si hay espacio"""
# Verifica si hay espacio para agregar un nuevo giro, si no hay espacio, mostrara un mensaje de error y retornara None
    if len(giros_para_hoy) >= CUPOS_MAXIMOS:
        print(f" LLevas {CUPOS_MAXIMOS} giros, ya alcanzaste el limite de de giros de dia de hoy .")
        return 
        
    quien_recibe = input("¿A que persona vas a enviar el dinero?: ")
    valor_dinero_enviado = input("¿Cuánto dinero vas a enviar?: ")
    
    dinero_enviado = revisar_dinero(valor_dinero_enviado)
    if dinero_enviado is not None:
        giros_para_hoy.append([quien_recibe, dinero_enviado])
        print("Listo, se ha guardado el giro.")

def ver_valor_total():
    """3. Muestra la suma usando la función recursiva"""
# Llama a la función recursiva suma_recursiva para calcular la suma de todos los giros en la lista giros_para_hoy y luego imprime el valor total acumulado
    la_suma = suma_recursiva(giros_para_hoy, 0)
    print(f"Valor total acumulado: ${la_suma:,.2f}")

def rastrear_por_nombre():
    """4. Busca giros usando lower y strip"""
# Pedira al usuario el nombre a buscar, y buscara en la lista de giros si hay coincidencias, si las hay, las mostrara, si no, mostrara un mensaje de que no encontro registros que coincidan con el nombre buscado
    nombre_a_buscar = input("¿A quién busca?: ").lower().strip()
    coincidencias = []
    
    for un_giro in giros_para_hoy:
        if nombre_a_buscar in un_giro[0].lower():
            coincidencias.append(un_giro)
            
    if coincidencias:
        print("Registro encontrado:")
        for coincidencia in coincidencias:
            print(f"• {coincidencia[0]}: ${coincidencia[1]:,.2f}")
    else:
        print("No encontré registros de giros con ese nombre.")

def suma_recursiva(la_lista, posicion):
    """5. Función recursiva para sumar todo lo que hay en la lista de giros"""
# Si llega al final de la lista retornara a 0 si no, sumara el valor del giro en la posicion actual y llamara a la funcion con la siguiente posicion (Recursividad)
    if posicion >= len(la_lista):
        return 0 
# Si la suma del dinero en la posicion actual es mayor a 0, sumara el valor del giro en la posicion actual y llamara a la funcion con la siguiente posicion (Recursividad)
    if la_lista[posicion][1] > 0:
        return la_lista[posicion][1] + suma_recursiva(la_lista, posicion + 1)
    else:
        return suma_recursiva(la_lista, posicion + 1)

def ver_todos_los_giros():
    """Lista todo lo que hemos registrado hasta el momento"""
    if not giros_para_hoy:
        print("La lista está vacía.")
        return
        
    print("Lista de giros registrados:")
    for posicion, un_giro in enumerate(giros_para_hoy):
        print(f"Giro #{posicion+1} -> Para: {un_giro[0]} | Cuánto: ${un_giro[1]:,.2f}")

while True:
    print("\n------------------------------------------")
    print("SISTEMA DE GIROS: Terminal de ROLDANILLO")
    print("------------------------------------------")
# Muestra las opciones disponibles para el usuario
    print("1. Registre un nuevo giro")
    print("2. Ver dinero total acumulado")
    print("3. Lista de los giros anotados")
    print("4. Buscar giro por nombre")
    print("5. Cerrar programa")
    print("------------------------------------------")
    
    lo_que_eligio = input("Escribe el numero de la opcion: ").strip()
    
    if lo_que_eligio == "1":
        agregar_nuevo_giro()
    elif lo_que_eligio == "2":
        ver_valor_total()
    elif lo_que_eligio == "3":
        ver_todos_los_giros()
    elif lo_que_eligio == "4":
        rastrear_por_nombre()
    elif lo_que_eligio == "5":
        print("Opcion 5 selecionada el programa se cerrara")
        break
    else:
        print("El numero de opcion elegida no es valida.")