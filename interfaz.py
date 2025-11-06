from base_datos import BaseDatos

def menu():
    bd = BaseDatos()

    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar animal")
        print("2. Ver animales")
        print("3. Actualizar datos de animal")
        print("4. Eliminar animal")
        print("5. Registrar producción semanal")
        print("6. Consultar producción de un animal")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del animal: ")
            raza = input("Raza: ")
            edad = int(input("Edad: "))
            bd.crear_animal(codigo, raza, edad)

        elif opcion == "2":
            bd.leer_animales()

        elif opcion == "3":
            codigo = input("Código del animal: ")
            raza = input("Nueva raza (dejar vacío si no cambia): ")
            edad = input("Nueva edad (dejar vacío si no cambia): ")
            nueva_edad = int(edad) if edad else None
            bd.actualizar_animal(codigo, raza if raza else None, nueva_edad)

        elif opcion == "4":
            codigo = input("Código del animal a eliminar: ")
            bd.eliminar_animal(codigo)

        elif opcion == "5":
            codigo = input("Código del animal: ")
            semana = int(input("Número de semana: "))
            huevos = int(input("Huevos producidos: "))
            bd.registrar_produccion(codigo, semana, huevos)

        elif opcion == "6":
            codigo = input("Código del animal: ")
            bd.consultar_produccion(codigo)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
