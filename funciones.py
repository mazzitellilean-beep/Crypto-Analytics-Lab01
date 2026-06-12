

#=======================================================
#                FUNCIONES FRONT
#=======================================================

def eliminar(matriz, ticker):
    """Elimina un activo de la matriz según su ticker. Repite hasta que el usuario ingrese 'fin'."""

    while ticker != 'fin':

        activos = busqueda_ticker(matriz, ticker)
        if activos != False:
            if len(activos) > 1:
                print(f"Activos con ticker {ticker} encontrados:")
                for i in range(len(activos)):
                    print(f"{i+1}.")
                    print(f"Nombre: \n", activos[i][0])
                    print(f"Metodologia: \n", activos[i][4])

                opcion = input("Escoja el ticker a eliminar por su metodologia: ")

                while not opcion.isnumeric() or int(opcion) > len(activos) or int(opcion) < 0:
                    print("Opción no válida. Intente nuevamente.")
                    opcion = input("Escoja el numero del ticker a eliminar por su metodologia: ")

                matriz.remove(activos[int(opcion)-1])
                print("Activo eliminado exitosamente")

            elif len(activos) == 1:
                for i in matriz:
                    if i[1] == activos[0][1]:
                        matriz.remove(i)
                        print("Activo eliminado exitosamente")

        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: \n')

def alta_activo(matriz, nombre):
    """Solicita los datos de un nuevo activo y lo agrega a la matriz. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.lower() != 'fin':

        if validar_nombre(nombre):
            ticker = input('Ingrese el ticker del activo: ').upper()
            if validar_ticker(ticker):
                valor_ref = input('Ingrese el valor de referencia base (Ej: USD) del activo: ')
                if validar_valor(valor_ref):
                    vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')
                    if validar_volumen(vol_act):
                        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
                        met_op = input(f'Ingrese la metodologia de operacion asignada {metodos_validos}: ')
                        if validar_metodologia(met_op):
                            unidades = input('Ingrese las unidades totales en tesoreria: ')
                            if validar_unidades(unidades):
                                punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')
                                if validar_puntaje(punt_conf):
                                    if validar_repetidos(nombre, ticker, met_op, matriz):
                                        activo = [nombre,ticker,valor_ref,vol_act,metodos_validos[int(met_op) - 1],unidades,punt_conf]
                                        matriz.append(activo)
                                        print('Datos del activo agregados correctamente.')

        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')

    if nombre.lower() == 'fin':
        print("\nVolviendo al menu principal...\n")
    

def modificar_activo(matriz, nombre):
    """Permite modificar los campos de un activo existente identificado por nombre. Repite hasta que el usuario ingrese 'fin'."""

    activo_encontrado = busqueda_nombre(matriz, nombre)

    while nombre.lower() != 'fin':

        if activo_encontrado:

            if len(activo_encontrado) > 1:
                print(f"Activos con nombre {nombre} encontrados:")
                for i in range(len(activo_encontrado)):
                    print(f"{i+1}.")
                    print(f"Nombre: \n", activo_encontrado[i][0])
                    print(f"Metodologia: \n", activo_encontrado[i][4])

                opcion = input("Escoja el nombre a eliminar por su metodologia: ")

                while not opcion.isnumeric() or int(opcion) > len(activo_encontrado) or int(opcion) < 0:
                    print("Opción no válida. Intente nuevamente.")
                    opcion = input("Escoja el numero del nombre a eliminar por su metodologia: ")
                activo_encontrado = activo_encontrado[int(opcion)-1]
        
            elif len(activo_encontrado) == 1:

                activo_encontrado = activo_encontrado[0]

            menu_modificar()
            opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:

                print("Opción inválida. Intente nuevamente.")
                menu_modificar()
                opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while int(opcion) != 8:

                if int(opcion) < 1 or int(opcion) > 8:
                    print("Opción no válida. Intente nuevamente.")

                if int(opcion) == 1:
                    nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                    if validar_nombre(nuevo_nombre):
                        activo_encontrado[0] = nuevo_nombre
                        print("Nombre del activo modificado exitosamente.")

                elif int(opcion) == 2:
                    nuevo_ticker = input("Ingrese el nuevo ticker del activo: ")
                    if validar_ticker(nuevo_ticker):
                        activo_encontrado[1] = nuevo_ticker
                        print("Ticker del activo modificado exitosamente.")

                elif int(opcion) == 3:
                    nuevo_valor_ref = input("Ingrese el nuevo valor de referencia del activo: ")
                    if validar_valor(nuevo_valor_ref):
                        activo_encontrado[2] = nuevo_valor_ref
                        print("Valor de referencia del activo modificado exitosamente.")

                elif int(opcion) == 4:
                    nuevo_vol_act = input("Ingrese el nuevo volumen de actividad del activo: ")
                    if validar_volumen(nuevo_vol_act):
                        activo_encontrado[3] = nuevo_vol_act
                        print("Volumen de actividad del activo modificado exitosamente.")

                elif int(opcion) == 5:
                    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL'] 
                    print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                    nueva_met_op = input('Ingrese el numero de la nueva metodología de operación asignada: ')
                    if validar_metodologia(nueva_met_op):
                        activo_encontrado[4] = metodos_validos[int(nueva_met_op) - 1]
                        print("Metodología de operación del activo modificada exitosamente.")

                elif int(opcion) == 6:
                    nuevas_unidades = input("Ingrese las nuevas unidades en tesorería del activo: ")
                    if validar_unidades(nuevas_unidades):
                        activo_encontrado[5] = nuevas_unidades
                        print("Unidades en tesorería del activo modificadas exitosamente.")                      

                elif int(opcion) == 7:
                    nuevo_punt_conf = input("Ingrese el nuevo puntaje de confianza del activo (1-10): ")
                    if validar_puntaje(nuevo_punt_conf):
                        activo_encontrado[6] = nuevo_punt_conf
                        print("Puntaje de confianza del activo modificado exitosamente.")

                if int(opcion) != 8:
                    menu_modificar()
                    opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

                    while not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:
                            
                        print("Opción no válida. Intente nuevamente.")
                        menu_modificar()
                        opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")
            
            print("Saliendo del activo...")

        nombre = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")

def mostrar_matriz(matriz):
    """Muestra todos los activos de la matriz ordenados por puntaje de confianza descendente."""

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
    """Busca activos por ticker en la matriz. Retorna la lista de coincidencias o False si no hay ninguna."""

    tickers_encontrados = []

    for i in matriz:

        if i[1].upper() == ticker.upper():

            tickers_encontrados.append(i)

    if len(tickers_encontrados) == 1:
        print(f"Activo encontrado: {tickers_encontrados[0][0]}")
        return tickers_encontrados
    
    elif len(tickers_encontrados) > 1:
        print("Se encontraron múltiples activos con el mismo ticker.")
        return tickers_encontrados
    
    elif len(tickers_encontrados) == 0:
        print("Activo no encontrado.")
        return False

def busqueda_nombre(matriz, nombre):
    """Busca activos por nombre en la matriz. Retorna la lista de coincidencias o False si no hay ninguna."""

    nombres_encontrados = []

    for i in matriz:

        if i[0].upper() == nombre.upper():

            nombres_encontrados.append(i)

    if len(nombres_encontrados) == 1:
        print(f"Activo encontrado: {i[0]}")
        return nombres_encontrados
    elif len(nombres_encontrados) > 1:
        print("Se encontraron múltiples activos con el mismo nombre.")
        return nombres_encontrados
    elif len(nombres_encontrados) == 0:
        print("Activo no encontrado.")
        return False

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y contenga solo caracteres alfabéticos. Retorna True si es válido."""
    if nombre == '' or not nombre.isalpha():
        print('El nombre del activo no puede estar vacío ni contener caracteres no alfabéticos. Intente nuevamente.')
        return False
    else:
        return True

def validar_ticker(ticker):
    """Valida que el ticker tenga entre 3 y 5 caracteres alfabéticos. Retorna True si es válido."""
    if ticker == '' or not ticker.isalpha() or len(ticker) < 3 or len(ticker) > 5:
        print('El ticker debe tener entre 3 y 5 caracteres, no puede estar vacío, y solo puede contener caracteres alfabéticos. Intente nuevamente.')
        return False
    else:
        return True

def validar_valor(valor_ref):
    """Valida que el valor de referencia sea un número decimal positivo. Retorna True si es válido."""
    if valor_ref == '' or valor_ref.count(".") > 1 or not valor_ref.replace(".", "").isnumeric() or float(valor_ref) <= 0:
        print('El valor de referencia debe ser un número positivo, y no puede estar vacío. Intente nuevamente.')
        return False
    else:
        return True

def validar_volumen(volumen):
    """Valida que el volumen de actividad sea un entero no negativo. Retorna True si es válido."""
    if volumen == '' or not volumen.isnumeric() or int(volumen) < 0 :
        print('El volumen de actividad debe ser un número positivo, y no puede estar vacío. Intente nuevamente.')
        return False
    else: 
        return True

def validar_metodologia(metodologia):
    """Valida que la metodología sea un número entre 1 y 4. Retorna True si es válido."""
    if  metodologia == '' or not metodologia.isnumeric() or int(metodologia) > 4 or int(metodologia) < 1:
        print('La metodología de operación debe ser un número entre 1 y 4. Intente nuevamente.')
        return False
    else:
        return True
    
def validar_unidades(unidades):
    """Valida que las unidades en tesorería sean un número no negativo. Retorna True si es válido."""
    if unidades == '' or unidades.count(".") <= 1 and not unidades.replace(".", "").isnumeric() or float(unidades) < 0 :
        print('Las unidades totales en tesorería deben ser un número positivo, y no pueden estar vacías. Intente nuevamente.')
        return False
    else:
        return True
    
def validar_puntaje(puntaje):
    """Valida que el puntaje de confianza sea un entero entre 1 y 10. Retorna True si es válido."""
    if puntaje == '' or not puntaje.isnumeric() or int(puntaje) < 1 or int(puntaje) > 10 :
        print('El puntaje de confianza debe ser un número entre 1 y 10, y no puede estar vacío. Intente nuevamente.')
        return False
    else:
        return True

def validar_repetidos(nombre, ticker, metodologia, matriz):
    """Verifica que no exista un activo con igual nombre o ticker y misma metodología. Retorna True si no hay duplicado."""
    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']

    for i in matriz:
        if metodos_validos[int(metodologia) - 1] == i[4] and nombre.upper() == i[0].upper():
            print('Activo ya existente en el sistema.')
            return False
        elif metodos_validos[int(metodologia) - 1] == i[4] and ticker.upper() == i[1].upper():
            print('Activo ya existente en el sistema.')
            return False
    else:
        return True

def menu_modificar():
    """Muestra el submenú de opciones para modificar los campos de un activo."""

    print("1. Cambiar nombre del activo")
    print("2. Cambiar ticker")
    print("3. Cambiar valor de referencia")
    print("4. Cambiar volumen de actividad")
    print("5. Cambiar metodología de operación")
    print("6. Cambiar unidades en tesorería")
    print("7. Cambiar puntaje de confianza (1-10)")
    print("8. Salir")

def ordenar_matriz(matriz):
    """Ordena la matriz por puntaje de confianza descendente; en caso de empate, ordena por nombre alfabéticamente."""

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
    """Muestra el menú principal y retorna la opción numérica seleccionada por el usuario."""

    print('='*50)
    print(' '*2 + 'SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB')
    print('='*50)
    print("1. Registrar nuevo activo (Alta)")
    print("2. Eliminar activo del sistema (Baja)")
    print("3. Modificar valoracion o puntaje (Modificacion)")
    print("4. Informe General - Visualizacion de los datos")
    print("8. Salir")
    print('='*50)

    opciones_validas = ['1', '2', '3', '4', '8']

    opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')

    if opcion in opciones_validas:
        while not opcion.isnumeric() or int(opcion) < 1 or (int(opcion) > 4 and int(opcion) != 8):
            print("Opción inválida. Intente nuevamente.\n")
            opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')
    else:
        print("Opción inválida. Intente nuevamente.\n")
        opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')
        while not opcion.isnumeric() or int(opcion) < 1 or (int(opcion) > 4 and int(opcion) != 8):
            print("Opción inválida. Intente nuevamente.\n")
            opcion = input('Ingrese el numero de la opcion que desea ejecutar: ') 

    return int(opcion)

def verificacion_menu(opcion, matriz):
    """Ejecuta la operación correspondiente a la opción elegida en el menú principal."""

    if opcion == 1:
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        if validar_nombre(nombre):
           alta_activo(matriz, nombre)

    elif opcion == 2:
        ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        if validar_ticker(ticker):
           eliminar(matriz, ticker)

    elif opcion == 3:
        nombre = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
        if validar_nombre(nombre):
           modificar_activo(matriz, nombre)

    elif opcion == 4:
        mostrar_matriz(matriz)

    elif opcion == 8:
        print("Saliendo del programa...")

    else:
        print("Opcion inválida. Por favor, ingrese una opcion del menu.")
