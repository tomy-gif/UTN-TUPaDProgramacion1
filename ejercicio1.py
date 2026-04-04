while True:
    nombre=input ("Ingrese el nombre del cliente: ")
    if nombre !="" and nombre.isalpha():
        break
    else:
        print("Error: el nombre debe contener solo letras y no estar vacío.")
while True:
    cantidad=input("Ingrese la cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad)>0:
        break
    else:
        print("Error: debe ingresar un numero entero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad +1):
    while True:
        precio=input(f"producto{i}-ingrese el precio: ")
        if precio.isdigit():
            precio=int(precio)
            break
        print("Error: el precio debe ser un número entero.")

        total_sin_descuento += precio
        
    while True:
        descuento = input(f"Producto {i} - ¿Tiene descuento? (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error: ingrese 'S' o 'N'.")

    if descuento == "s":
        precio_final = precio * 0.9  # 10% de descuento
    else:
        precio_final = precio

    total_con_descuento += precio_final

    ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESUMEN ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

