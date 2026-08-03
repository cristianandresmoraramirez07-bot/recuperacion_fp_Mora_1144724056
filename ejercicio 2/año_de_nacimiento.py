año_nacimiento = int(input("Pon tu año de nacimiento:"))

edad = 2026 - año_nacimiento

print(f"Tu edad es de {edad} años.")

if edad >= 18:
    print("Cumples con la edad mínima, puedes pasar")
else:
    print("No tienes edad suficiente, tu paso está prohibido.")