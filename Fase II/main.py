import funciones
from tabla_original import tabla_original

def main():
    """Punto de entrada del programa: inicializa la tabla de activos y ejecuta el loop principal del menú."""

    tabla_activos = tabla_original()

    opcion = funciones.menu()

    while opcion != "8":
        funciones.verificacion_menu(opcion, tabla_activos)
        opcion = funciones.menu()

    print("Gracias por utilizar el sistema de gestion. Finalizando programa...")

if __name__ == "__main__":
    main()
