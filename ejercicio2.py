usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1
if not acceso:
    print("Cuenta bloqueada.")
else:
    
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    
        opcion = input("Opción: ")
       
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            while True:
                nueva_clave = input("Nueva clave: ")
                
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue

                confirmar = input("Confirmar clave: ")

                if nueva_clave != confirmar:
                    print("Error: las claves no coinciden.")
                else:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                    break
        elif opcion == 3:
            print("¡Seguí adelante, estás aprendiendo Python!")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break