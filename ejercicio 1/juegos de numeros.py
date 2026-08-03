import random

numero_secreto = random.randint(1, 50)
intentos_restantes = 5

print("juego de numeros adivina el numero")
print("escribe un numero entre 1 y 50 tienes solo 5 oportunidades\n")


while intentos_restantes > 0:
    print(f"solo te quedan {intentos_restantes} intentos")
    
    intento = int(input("Di un numero: "))

    if intento == numero_secreto:
        print(f"encontraste el numero secreto era {numero_secreto}. felicidades")
        break  
    elif intento < numero_secreto:
        print("numero muy pequeño, el numero secreto es mas grande")
    else:
        print("numero que es muy grande, el numero secreto es mas pequeño")
        
    intentos_restantes -= 1
    print("-" * 30)

if intentos_restantes == 0:
    print(f"se acabaron tus intentos el numero secreto era {numero_secreto}. fin del juego")