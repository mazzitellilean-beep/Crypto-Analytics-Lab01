from mostrar_menu import menu

opcion = menu()

while opcion != 8:
    from validacion_opcion import verificacion_menu
    verificacion_menu(opcion)
    opcion = int(input('Ingrese el numero de la opcion que desea ejecutar: '))

print("Gracias por utilizar el sistema de gestion. Finalizando programa...")