def verificacion_menu (opcion, lista):
    
    if opcion == 1:
        from carga_matriz import carga_matriz
        lista = carga_matriz(lista)
    elif opcion == 2:
        from baja_activo import eliminar
        ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        lista = eliminar(lista, ticker)
    elif opcion == 3: 
        from modificar_activo import modificar
        lista = modificar(lista)
    elif opcion == 4:
        from mostrar_matriz import mostrar_matriz
        mostrar_matriz(lista)
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")
    
    return lista
