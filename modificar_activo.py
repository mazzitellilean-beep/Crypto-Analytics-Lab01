def modificar(lista):

    activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")

    while activo_a_cambiar.lower() != 'fin':
        
        activo_encontrado = False

        for i in lista:
            if i[0].upper() == activo_a_cambiar.upper():
                activo_encontrado = True
                print(f"Activo encontrado: {i}")
                print("1. Cambiar nombre del activo")
                print("2. Cambiar ticker")
                print("3. Cambiar valor de referencia")
                print("4. Cambiar volumen de actividad")
                print("5. Cambiar metodología de operación")
                print("6. Cambiar unidades en tesorería")
                print("7. Cambiar puntaje de confianza (1-10)")
                print("8. Salir")

                opcion_modificar = int(input("Ingrese el número de la opción que desea modificar: "))

                while opcion_modificar != 8:
                    if opcion_modificar == 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                        if nuevo_nombre == '':
                            print('Error: El nombre no puede estar vacio. No se realizaron modificaciones')
                            break
                        else:
                            i[0] = nuevo_nombre
                    elif opcion_modificar == 2:
                        nuevo_ticker = input("Ingrese el nuevo ticker del activo: ")
                        if nuevo_ticker == '' or len(nuevo_ticker) < 3:
                            print('Error: El ticker no puede estar vacio y debe tener al menos 3 caracteres. No se realizaron modificaciones')
                            break
                        else:
                            i[1] = nuevo_ticker
                    elif opcion_modificar == 3:
                        nuevo_valor_ref = float(input("Ingrese el nuevo valor de referencia del activo: "))
                        if nuevo_valor_ref <= 0:
                            print('Error: El valor de referencia debe ser un número positivo. No se realizaron modificaciones')
                            break
                        else:
                            i[2] = nuevo_valor_ref
                    elif opcion_modificar == 4:
                        nuevo_vol_act = float(input("Ingrese el nuevo volumen de actividad del activo: "))
                        if nuevo_vol_act < 0:
                            print('Error: El volumen de actividad no puede ser negativo. No se realizaron modificaciones')
                            break
                        else:
                            i[3] = nuevo_vol_act
                    elif opcion_modificar == 5:
                        nuevos_metodos_validos = ['1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL']
                        nueva_met_op = int(input(f'Ingrese el numero de la nueva metodología de operación asignada: '))
                        if nueva_met_op < 1 or nueva_met_op > 4:
                            print('Error: La metodología de operación debe ser un número entre 1 y 4. No se realizaron modificaciones')
                            break
                        else:
                            i[4] = nuevos_metodos_validos[nueva_met_op - 1]
                    elif opcion_modificar == 6:
                        nuevas_unidades = float(input("Ingrese las nuevas unidades en tesorería del activo: "))
                        if nuevas_unidades < 0:
                            print('Error: Las unidades en tesorería no pueden ser negativas. No se realizaron modificaciones')
                            break
                        else:
                            i[5] = nuevas_unidades
                    elif opcion_modificar == 7:
                        nuevo_punt_conf = int(input("Ingrese el nuevo puntaje de confianza del activo (1-10): "))
                        if nuevo_punt_conf < 1 or nuevo_punt_conf > 10:
                            print('Error: El puntaje de confianza debe ser un número entre 1 y 10. No se realizaron modificaciones')
                            break
                        else:
                            i[6] = nuevo_punt_conf
                    elif opcion_modificar == 8:
                        print("Saliendo del menú de modificación.")
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")
                
                if opcion_modificar != 8:
                    print("1. Cambiar nombre del activo")
                    print("2. Cambiar ticker")
                    print("3. Cambiar valor de referencia")
                    print("4. Cambiar volumen de actividad")
                    print("5. Cambiar metodología de operación")
                    print("6. Cambiar unidades en tesorería")
                    print("7. Cambiar puntaje de confianza (1-10)")
                    print("8. Salir")

                    opcion_modificar = int(input("Ingrese el número de la opción que desea modificar o 8 para salir: "))
        
        if not activo_encontrado:
            print("Activo no encontrado. Intente nuevamente.")

        activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
    
    return lista
