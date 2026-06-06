def eliminar(tabla, nombre):

    for i in range(len(tabla)):

        if tabla[i][0].lower() == nombre.lower():
            
            tabla.pop(i)

            break
    
    print(f"\nActivo '{nombre}' eliminado exitosamente.")

    repetir = input("\n¿Desea eliminar otro activo? (s/n): ").strip().lower()
    if repetir == 's':
        nuevo_nombre = input("\nIngrese el nombre del siguiente activo a eliminar: ").strip()
        eliminar(tabla, nuevo_nombre)
    if repetir == 'n':
        salida = input("\nPresione Enter para volver al menú principal...")
        return tabla
    
    else:
        print("\nOpción no válida. Volviendo al menú principal.")

    salida = input("\nPresione Enter para volver al menú principal...")

    

    return tabla