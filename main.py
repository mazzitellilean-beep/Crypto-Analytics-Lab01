import funciones
from tabla_original import tabla_original

def main():
    
    tabla_activos = tabla_original()

    opcion = funciones.menu()

    while opcion != '8': 
        funciones.verificacion_menu(opcion, tabla_activos)
        if opcion != '8':
            opcion = funciones.menu()

    print("Gracias por utilizar el sistema de gestion. Finalizando programa...")

if __name__ == "__main__":
    main() 
