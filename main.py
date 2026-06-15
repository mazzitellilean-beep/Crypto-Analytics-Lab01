import funciones
import tablas

def main():
    
    catalogo = tablas.tabla_catalogo()
    matriz = tablas.tabla_cartera()

    opcion = funciones.menu_principal()

    while opcion != '8':
        funciones.verificacion_menu_principal(opcion, catalogo, matriz)
        opcion = funciones.menu_principal()   # siempre vuelve a pedir, el '8' corta el while

    print("\033[92mGracias por utilizar el sistema de gestion. Finalizando programa...\033[0m")

if __name__ == "__main__":
    main()
