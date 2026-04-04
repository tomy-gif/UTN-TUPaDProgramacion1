# Turnos (sin listas)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Ingrese nombre del operador: ")
    if operador != "" and operador.isalpha():
        break
    else:
        print("Error: solo letras y no vacío.")

while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia not in ["1", "2"]:
            print("Error: día inválido.")
            continue

        while True:
            nombre = input("Nombre del paciente: ")
            if nombre != "" and nombre.isalpha():
                break
            else:
                print("Error: solo letras.")

        if dia == "1":
            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print("Error: paciente ya tiene turno ese día.")
            elif lunes1 == "":
                lunes1 = nombre
                print("Turno asignado (Lunes 1).")
            elif lunes2 == "":
                lunes2 = nombre
                print("Turno asignado (Lunes 2).")
            elif lunes3 == "":
                lunes3 = nombre
                print("Turno asignado (Lunes 3).")
            elif lunes4 == "":
                lunes4 = nombre
                print("Turno asignado (Lunes 4).")
            else:
                print("No hay turnos disponibles en Lunes.")

        else:
            if nombre in (martes1, martes2, martes3):
                print("Error: paciente ya tiene turno ese día.")
            elif martes1 == "":
                martes1 = nombre
                print("Turno asignado (Martes 1).")
            elif martes2 == "":
                martes2 = nombre
                print("Turno asignado (Martes 2).")
            elif martes3 == "":
                martes3 = nombre
                print("Turno asignado (Martes 3).")
            else:
                print("No hay turnos disponibles en Martes.")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia not in ["1", "2"]:
            print("Error: día inválido.")
            continue

        while True:
            nombre = input("Nombre del paciente: ")
            if nombre != "" and nombre.isalpha():
                break
            else:
                print("Error: solo letras.")

        encontrado = False

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True

        else:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("No se encontró ese turno.")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("\n--- LUNES ---")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia == "2":
            print("\n--- MARTES ---")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")
        else:
            print("Error: día inválido.")

    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("\n--- RESUMEN ---")
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate en cantidad de turnos.")

    # 5. SALIR
    elif opcion == 5:
        print("Sistema cerrado.")
        break