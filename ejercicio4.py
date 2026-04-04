energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0  # para la regla anti-spam

while True:
    agente = input("Ingrese nombre del agente: ")
    if agente != "" and agente.isalpha():
        break
    else:
        print("Error: solo letras.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("\n⚠️ Sistema bloqueado por alarma. DERROTA.")
        break

    print("\n--- ESTADO ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error: opción inválida.")
        continue

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            print("⚠️ Forzaste demasiadas veces seguidas. La cerradura se trabó.")
            alarma = True
            racha_forzar = 0
            continue

        if energia < 40:
            while True:
                riesgo = input("Riesgo! Elegí un número (1-3): ")
                if riesgo.isdigit() and int(riesgo) in [1, 2, 3]:
                    riesgo = int(riesgo)
                    break
                else:
                    print("Error: número inválido.")

            if riesgo == 3:
                print("⚠️ Se activó la alarma!")
                alarma = True

        if not alarma:
            cerraduras_abiertas += 1
            print("🔓 Cerradura abierta!")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("🔓 Hackeo exitoso! Cerradura abierta.")

    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0

        if alarma:
            energia -= 10
            print("⚠️ Descansar con alarma activa consume energía extra.")

        print("Recuperaste energía.")

print("\n--- RESULTADO ---")

if cerraduras_abiertas == 3:
    print("🎉 VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA. Te quedaste sin recursos.")