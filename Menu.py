from alta_activos import alta
from eliminar_activos import eliminar
from modificar_activo import modificar
from mostrar_tabla import mostrar


def mostrar_menu():
    print("\n" + "=" * 48)
    print("   SISTEMA DE GESTIÓN: CRYPTO-ANALYTICS LAB")
    print("=" * 48)
    print("\n1. Registrar nuevo activo (Alta)")
    print("2. Eliminar activo del sistema (Baja)")
    print("3. Modificar valoración o puntaje (Modificación)")
    print("4. Informe General – Visualización de los datos")
    print("\n8. Salir")
    print("\n" + "=" * 48)

def menu_principal(tabla):
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4 o 8 para salir): ").strip()

        if opcion == "1":
            alta(tabla)        
        elif opcion == "2":
            nombre = input("\nIngrese el nombre del activo a eliminar: ").strip()
            eliminar(tabla, nombre)         
        elif opcion == "3":
            modificar(tabla)        
        elif opcion == "4":
            mostrar(tabla)
        elif opcion == "8":
            print("\n¡Hasta luego!\n")
            break
        else:
            print("\n⚠ Opción inválida. Intente nuevamente.")


