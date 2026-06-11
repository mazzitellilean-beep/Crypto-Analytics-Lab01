
#=======================================================
#                FUNCIONES FRONT
#=======================================================

def eliminar(matriz, ticker):

    '''Elimina activos según el ticker'''

    while ticker != 'fin':

        activo = busqueda_ticker(matriz, ticker)
        if activo != False:
            matriz.remove(activo)
        else:
            print("Activo no encontrado. Intente nuevamente.")

        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ')

    return matriz

def carga_activo(matriz, nombre):

    while nombre.lower() != 'fin':

        ticker = input('Ingrese el ticker del activo: ').upper()
        valor_ref = input('Ingres el valor de referencia base (Ej: USD) del activo: ')
        vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')
        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
        met_op = input(f'Ingrese la metodologia de operacion asignada {metodos_validos}: ')
        unidades = input('Ingrese las unidades totales en tesoreria: ')
        punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')

        #La variable activo podria eliminarse y directamente agregar los datos a la tabla, pero queda ordenado 
        activo = [nombre,ticker,valor_ref,vol_act,metodos_validos[int(met_op) - 1],unidades,punt_conf]

        if validacion(nombre, ticker, valor_ref, vol_act, met_op, unidades, punt_conf, matriz):
            matriz.append(activo)
            print('Datos del activo agregados correctamente.')
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
    
    return matriz

def modificar_activo(matriz, nombre):

    while nombre.lower() != 'fin':
        
        if busqueda_nombre(matriz, nombre):

            activo_encontrado = busqueda_nombre(matriz, nombre)
            menu_modificar()
            opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:

                print("Opción no válida. Intente nuevamente.")
                menu_modificar()
                opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while int(opcion) != 8:

                    if int(opcion) < 1 or int(opcion) > 8:
                        print("Opción no válida. Intente nuevamente.")

                    if int(opcion) == 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                        validacion(nuevo_nombre, activo_encontrado[1], activo_encontrado[2], activo_encontrado[3], 1, activo_encontrado[5], activo_encontrado[6], matriz)
                        matriz[activo_encontrado][0] = nuevo_nombre

                    elif int(opcion) == 2:
                        nuevo_ticker = input("Ingrese el nuevo ticker del activo: ")
                        validacion(activo_encontrado[1], nuevo_ticker, activo_encontrado[2], activo_encontrado[3], 1, activo_encontrado[5], activo_encontrado[6], matriz)
                        matriz[activo_encontrado][1] = nuevo_ticker

                    elif int(opcion) == 3:
                        nuevo_valor_ref = input("Ingrese el nuevo valor de referencia del activo: ")
                        validacion(activo_encontrado[0], activo_encontrado[1], nuevo_valor_ref, activo_encontrado[3], 1, activo_encontrado[5], activo_encontrado[6], matriz)
                        matriz[activo_encontrado][2] = float(nuevo_valor_ref)

                    elif int(opcion) == 4:
                        nuevo_vol_act = input("Ingrese el nuevo volumen de actividad del activo: ")
                        validacion(activo_encontrado[0], activo_encontrado[1], activo_encontrado[2], nuevo_vol_act, 1, activo_encontrado[5], activo_encontrado[6], matriz)
                        matriz[activo_encontrado][3] = float(nuevo_vol_act)

                    elif int(opcion) == 5:
                        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL'] 
                        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        nueva_met_op = input(f'Ingrese el numero de la nueva metodología de operación asignada: ')
                        validacion(activo_encontrado[0], activo_encontrado[1], activo_encontrado[2], activo_encontrado[3], nueva_met_op, activo_encontrado[5], activo_encontrado[6], matriz)
                        matriz[activo_encontrado][4] = metodos_validos[int(nueva_met_op) - 1]

                    elif int(opcion) == 6:
                        nuevas_unidades = input("Ingrese las nuevas unidades en tesorería del activo: ")
                        validacion(activo_encontrado[0], activo_encontrado[1], activo_encontrado[2], activo_encontrado[3], 1, nuevas_unidades, activo_encontrado[6], matriz)
                        matriz[activo_encontrado][5] = float(nuevas_unidades)

                    elif int(opcion) == 7:
                        nuevo_punt_conf = input("Ingrese el nuevo puntaje de confianza del activo (1-10): ")
                        validacion(activo_encontrado[0], activo_encontrado[1], activo_encontrado[2], activo_encontrado[3], 1, activo_encontrado[5], nuevo_punt_conf, matriz)
                        matriz[activo_encontrado][6] = int(nuevo_punt_conf)

                    elif int(opcion) == 8:
                        print("Saliendo del menú de modificación.")

                    if int(opcion) != 8:
                        menu_modificar()
                        opcion = input("Ingrese el número de la opción que desea modificar o 8 para salir: ")

                        while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:

                            print("Opción no válida. Intente nuevamente.")
                            menu_modificar()
                            opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")
    
    return matriz

def mostrar_matriz (matriz):

    matriz = ordenar_matriz(matriz)

    print("\n" + "=" * 105)

    print(f"{'NOMBRE':<25} {'TICKER':<8} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'UNIDADES':>12} {'PUNTAJE':>8}")
    
    print("=" * 105)

    for activo in matriz:
        print(f"{activo[0]:<25} {activo[1]:<8} {float(activo[2]):>12.2f} {int(activo[3]):>18,} {activo[4]:>15} {float(activo[5]):>12,} {int(activo[6]):>8}")
    
    print("=" * 105)

    salida = input("\nPresione Enter para volver al menú principal...")

#=======================================================
#                FUNCIONES BACK
#=======================================================

def busqueda_ticker(matriz, ticker):

    for i in matriz:
            
            if i[1].upper() == ticker.upper():

                activo_encontrado = i
                print(f"Activo encontrado: {i}")
                return activo_encontrado

    else:
        print("Activo no encontrado.")

def busqueda_nombre(matriz, nombre):

    for i in matriz:
            
            if i[0].upper() == nombre.upper():

                activo_encontrado = i
                print(f"Activo encontrado: {i}")
                return activo_encontrado
    else:
        return False

def validacion(nombre, ticker, valor_ref, vol_act, met_op, unidades, punt_conf, matriz):

    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']

    datos_validos = True

    if nombre == '' or not nombre.isalpha():
        print('El nombre del activo no puede estar vacío ni contener caracteres no alfabéticos. Intente nuevamente.')
        datos_validos = False

    if not ticker.isalpha() or len(ticker) < 3 or len(ticker) > 5 or ticker == '':
        print('El ticker debe tener entre 3 y 5 caracteres, no puede estar vacío, y solo puede contener caracteres alfabéticos. Intente nuevamente.')
        datos_validos = False

    if valor_ref == '' or not valor_ref.isnumeric() or int(valor_ref) <= 0 :
        print('El valor de referencia debe ser un número positivo, y no puede estar vacío. Intente nuevamente.')
        datos_validos = False

    if vol_act == '' or not vol_act.isnumeric() or int(vol_act) < 0 :
        print('El volumen de actividad debe ser un número positivo, y no puede estar vacío. Intente nuevamente.')
        datos_validos = False

    if not met_op.isnumeric() or int(met_op) > 4 or met_op == '' or int(met_op) < 1:
        print('La metodología de operación debe ser un número entre 1 y 4. Intente nuevamente.')
        datos_validos = False

    for i in matriz:
        if metodos_validos[int(met_op) - 1] == i[4] and nombre.upper() == i[0].upper() and ticker.upper() == i[1].upper():
            print('Activo ya existente en el sistema.')
            return False
  
    if unidades == '' or not unidades.isnumeric() or int(unidades) < 0 :
        print('Las unidades totales en tesorería deben ser un número positivo, y no pueden estar vacías. Intente nuevamente.')
        datos_validos = False

    if punt_conf == '' or not punt_conf.isnumeric() or int(punt_conf) < 1 or int(punt_conf) > 10 :
        print('El puntaje de confianza debe ser un número entre 1 y 10, y no puede estar vacío. Intente nuevamente.')
        datos_validos = False

    return datos_validos

def menu_modificar():

    print("1. Cambiar nombre del activo")
    print("2. Cambiar ticker")
    print("3. Cambiar valor de referencia")
    print("4. Cambiar volumen de actividad")
    print("5. Cambiar metodología de operación")
    print("6. Cambiar unidades en tesorería")
    print("7. Cambiar puntaje de confianza (1-10)")
    print("8. Salir")

def ordenar_matriz(matriz):

    for i in range(len(matriz)-1):
        indice_max = i

        for j in range(i+1, len(matriz)):
            if int(matriz[j][6]) > int(matriz[indice_max][6]):
                indice_max = j
            elif int(matriz[j][6]) == int(matriz[indice_max][6]):
                nombre_activo = matriz[j][0].upper()
                nombre_activo_max = matriz[indice_max][0].upper()
                if nombre_activo < nombre_activo_max:
                    indice_max = j
            
        matriz[i], matriz[indice_max] = matriz[indice_max], matriz[i]

    return matriz

#=======================================================
#                        MENU
#=======================================================

def menu():

    print('='*50)
    print(' '*2 + 'SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB')
    print('='*50)
    print("1. Registrar nuevo activo (Alta)")
    print("2. Eliminar activo del sistema (Baja)")
    print("3. Modificar valoracion o puntaje (Modificacion)")
    print("4. Informe General - Visualizacion de los datos")
    print("8. Salir")
    print('='*50)

    opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')
    while not opcion.isnumeric() or int(opcion) < 1 or (int(opcion) > 4 and int(opcion) != 8):
        print("Opción inválida. Intente nuevamente.")
        opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')

    return int(opcion)

def verificacion_menu (opcion, matriz):

    if opcion == 1:
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        matriz = carga_activo(matriz, nombre)

    elif opcion == 2:
        ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        matriz = eliminar(matriz, ticker)

    elif opcion == 3:
        nombre = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
        matriz = modificar_activo(matriz, nombre)

    elif opcion == 4:
        mostrar_matriz(matriz)

    elif opcion == 8:
        print("Saliendo del programa...")

    else:
        print("Opcion inválida. Por favor, ingrese una opcion del menu.")