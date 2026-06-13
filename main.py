import funciones
from tabla_original import tabla_original, tabla_cartera


def main():
    """Punto de entrada del programa.
    Inicializa el catalogo de activos y la cartera, y ejecuta el loop principal del menu."""

    
    catalogo = tabla_original()
    cartera  = tabla_cartera()

    opcion = funciones.menu_principal()

    while opcion != '8':

        # --- GESTION DE ACTIVOS ---
        if opcion == '1':

            sub = funciones.menu_gestion_activos()

            while sub != '8':

                if sub == '1':
                    funciones.alta_catalogo(catalogo)

                elif sub == '2':
                    funciones.baja_catalogo(catalogo, cartera)

                elif sub == '3':
                    funciones.modificar_catalogo(catalogo)

                elif sub == '4':
                    funciones.mostrar_catalogo(catalogo)

                else:
                    print('Opcion invalida. Intente nuevamente.')

                sub = funciones.menu_gestion_activos()

        # --- GESTION DE CARTERA ---
        elif opcion == '2':

            sub = funciones.menu_gestion_cartera()

            while sub != '8':

                if sub == '1':
                    funciones.alta_cartera(cartera, catalogo)

                elif sub == '2':
                    funciones.baja_cartera(cartera)

                elif sub == '3':
                    funciones.mostrar_cartera(cartera, catalogo)

                else:
                    print('Opcion invalida. Intente nuevamente.')

                sub = funciones.menu_gestion_cartera()

        else:
            print('Opcion invalida. Intente nuevamente.')

        opcion = funciones.menu_principal()

    print('\nGracias por utilizar el sistema de gestion. Finalizando programa...')


if __name__ == '__main__':
    main()
