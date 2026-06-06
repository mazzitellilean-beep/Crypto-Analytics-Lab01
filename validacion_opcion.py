def verificacion_menu (opcion, lista):
    
    if opcion == 1:
        from carga_matriz import carga_matriz
        carga_matriz()
    elif opcion == 2:
        from baja_activo import eliminar
        eliminar()
    elif opcion == 3:
        from modificar_activo import modificar
        modificar()
    elif opcion == 4:
        from mostrar_matriz import mostrar_matriz
        mostrar_matriz(lista)
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")