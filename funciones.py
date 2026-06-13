
#=======================================================
#                FUNCIONES FRONT
#=======================================================

def eliminar(matriz, ticker):

    """Elimina un activo de la matriz según su ticker. Repite hasta que el usuario ingrese 'fin'."""

    while ticker.upper() != 'FIN':

        activos = busqueda_ticker(matriz, ticker)

        if activos != False:
            if len(activos) > 1:
                menu_repetidos(activos)

                opcion = input("Escoja el numero del ticker a eliminar por su metodologia: ")

                while not validar_opcion_repetidos(opcion, activos):
                    opcion = input("Escoja el numero del ticker a eliminar por su metodologia: ")

                matriz.remove(activos[int(opcion)-1])
                print("Activo eliminado exitosamente")

            elif len(activos) == 1:
                matriz.remove(activos[0])
                print("Activo eliminado exitosamente")

        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ').upper()
        while not validar_ticker(ticker) and ticker.upper() != 'FIN':
            ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ').upper()

    print("\nVolviendo al menu principal...\n")

def alta_activo(matriz, nombre):

    """Solicita los datos de un nuevo activo y lo agrega a la matriz. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        ticker = input('Ingrese el ticker del activo: ').upper()

        while not validar_ticker(ticker):
            ticker = input('Ingrese el ticker del activo: ').upper()

        valor_ref = input('Ingrese el valor de referencia base (Ej: USD) del activo: ')

        while not validar_valor(valor_ref):
            valor_ref = input('Ingrese el valor de referencia base (Ej: USD) del activo: ')

        vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')

        while not validar_volumen(vol_act):
            vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')
                    
        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
        met_op = input(f'Ingrese la metodologia de operacion asignada {metodos_validos}: ')
        
        while not validar_metodologia(met_op):
            print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
            met_op = input(f'Ingrese la metodologia de operacion asignada {metodos_validos}: ')
                        
        unidades = input('Ingrese las unidades totales en tesoreria: ')
        while not validar_unidades(unidades):
            unidades = input('Ingrese las unidades totales en tesoreria: ')
                           
        punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')
        while not validar_puntaje(punt_conf):
            punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')
        
        if validar_repetidos(nombre, ticker, met_op, matriz):

            activo = [nombre,ticker.upper(),float(valor_ref),int(vol_act),metodos_validos[int(met_op) - 1],float(unidades),int(punt_conf)]
            matriz.append(activo)
            print('Datos del activo agregados correctamente.')

        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')

    if nombre.upper() == 'FIN':
        print("\nVolviendo al menu principal...\n")
    

def modificar_activo(matriz, nombre):
    """Permite modificar los campos de un activo existente identificado por nombre. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        activo_encontrado = busqueda_nombre(matriz, nombre)

        if activo_encontrado:

            if len(activo_encontrado) > 1:
                menu_repetidos(activo_encontrado)

                opcion = input("Escoja el nombre a eliminar por su metodologia: ")

                while not validar_opcion_repetidos(opcion, activo_encontrado):
                    opcion = input("Escoja el nombre a eliminar por su metodologia: ")

                activo_encontrado = activo_encontrado[int(opcion)-1]

            elif len(activo_encontrado) == 1:

                activo_encontrado = activo_encontrado[0]

            menu_modificar()
            opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while not validar_opcion_modificar(opcion):
                menu_modificar()
                opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            while int(opcion) != 8:

                if int(opcion) == 1:
                    nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                    while not validar_nombre(nuevo_nombre):
                        nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")

                    activo_encontrado[0] = nuevo_nombre
                    print("Nombre del activo modificado exitosamente.")

                elif int(opcion) == 2:
                    nuevo_ticker = input("Ingrese el nuevo ticker del activo: ").upper()
                    while not validar_ticker(nuevo_ticker):
                        nuevo_ticker = input("Ingrese el nuevo ticker del activo: ").upper()

                    activo_encontrado[1] = nuevo_ticker
                    print("Ticker del activo modificado exitosamente.")

                elif int(opcion) == 3:
                    nuevo_valor_ref = input("Ingrese el nuevo valor de referencia del activo: ")
                    while not validar_valor(nuevo_valor_ref):
                        nuevo_valor_ref = input("Ingrese el nuevo valor de referencia del activo: ")

                    activo_encontrado[2] = float(nuevo_valor_ref)
                    print("Valor de referencia del activo modificado exitosamente.")

                elif int(opcion) == 4:
                    nuevo_vol_act = input("Ingrese el nuevo volumen de actividad del activo: ")
                    while not validar_volumen(nuevo_vol_act):
                        nuevo_vol_act = input("Ingrese el nuevo volumen de actividad del activo: ")

                    activo_encontrado[3] = int(nuevo_vol_act)
                    print("Volumen de actividad del activo modificado exitosamente.")

                elif int(opcion) == 5:
                    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
                    print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                    nueva_met_op = input('Ingrese el numero de la nueva metodología de operación asignada: ')
                    while not validar_metodologia(nueva_met_op):
                        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        nueva_met_op = input('Ingrese el numero de la nueva metodología de operación asignada: ')

                    activo_encontrado[4] = metodos_validos[int(nueva_met_op) - 1]
                    print("Metodología de operación del activo modificada exitosamente.")

                elif int(opcion) == 6:
                    nuevas_unidades = input("Ingrese las nuevas unidades en tesorería del activo: ")
                    while not validar_unidades(nuevas_unidades):
                        nuevas_unidades = input("Ingrese las nuevas unidades en tesorería del activo: ")

                    activo_encontrado[5] = float(nuevas_unidades)
                    print("Unidades en tesorería del activo modificadas exitosamente.")

                elif int(opcion) == 7:
                    nuevo_punt_conf = input("Ingrese el nuevo puntaje de confianza del activo (1-10): ")
                    while not validar_puntaje(nuevo_punt_conf):
                        nuevo_punt_conf = input("Ingrese el nuevo puntaje de confianza del activo (1-10): ")

                    activo_encontrado[6] = int(nuevo_punt_conf)
                    print("Puntaje de confianza del activo modificado exitosamente.")

                menu_modificar()
                opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

                while not validar_opcion_modificar(opcion):
                    opcion = input("Ingrese el número de la opción que desea modificar u 8 para salir: ")

            print("Saliendo del activo...")

        nombre = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")

def mostrar_matriz(matriz):
    """Muestra todos los activos de la matriz ordenados por puntaje de confianza descendente."""

    ordenar_matriz(matriz)

    print("\n" + "=" * 110)

    print(f"{'NOMBRE':<25} {'TICKER':<8} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'UNIDADES':>14} {'PUNTAJE':>8}")
    
    print("=" * 110)

    for activo in matriz:
        print(f"{activo[0]:<25} {activo[1]:<8} {float(activo[2]):>12.2f} {int(activo[3]):>18,} {activo[4]:>15} {float(activo[5]):>14,.2f} {int(activo[6]):>8}")
    
    print("=" * 110)

    salida = input("\nPresione Enter para volver al menú principal...")

#=======================================================
#                FUNCIONES BACK
#=======================================================

def busqueda_ticker(matriz, ticker):
    """Busca activos por ticker en la matriz. Retorna la lista de coincidencias o False si no hay ninguna."""

    tickers_encontrados = []

    for i in matriz:

        if i[1].upper() == ticker.upper() and float(i[5]) == 0:

            tickers_encontrados.append(i)

    if len(tickers_encontrados) == 1:
        print(f"Activo encontrado: {tickers_encontrados[0][0]}")
        return tickers_encontrados
    
    elif len(tickers_encontrados) > 1:
        print("Se encontraron múltiples activos con el mismo ticker.")
        return tickers_encontrados
    
    elif len(tickers_encontrados) == 0:
        print("Activo no encontrado. Asegúrese que tenga 0 unidades en tesorería.")
        return False

def busqueda_nombre(matriz, nombre):
    """Busca activos por nombre en la matriz. Retorna la lista de coincidencias o False si no hay ninguna."""

    nombres_encontrados = []

    for i in matriz:

        if i[0].upper() == nombre.upper():

            nombres_encontrados.append(i)

    if len(nombres_encontrados) == 1:
        print(f"Activo encontrado: {nombres_encontrados[0][0]}")
        return nombres_encontrados
    elif len(nombres_encontrados) > 1:
        print("Se encontraron múltiples activos con el mismo nombre.")
        return nombres_encontrados
    elif len(nombres_encontrados) == 0:
        print("Activo no encontrado.")
        return False

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío y contenga solo caracteres alfabéticos. Retorna True si es válido."""
    if nombre == '' or nombre.isnumeric():
        print('El nombre del activo no puede estar vacío ni contener caracteres no alfabéticos. Intente nuevamente.')
        return False
    else:
        return True

def validar_ticker(ticker):
    """Valida que el ticker tenga entre 3 y 5 caracteres alfabéticos. Retorna True si es válido."""
    if ticker == '' or ticker.isnumeric() or len(ticker) < 3 or len(ticker) > 5 or ticker.upper() == 'FIN':
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
    if unidades == '' or unidades.count(".") > 1 or not unidades.replace(".", "").isnumeric() or float(unidades) < 0 :
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
    
def validar_opcion_repetidos(opcion, activos):
    '''Valida la opción elegida en el menú para seleccionar el activo que desea el usuario en caso de que hayan varios con el mismo nombre o ticker'''

    if opcion == '' or not opcion.isnumeric() or int(opcion) > len(activos) or int(opcion) <= 0:
        print("Opción no válida. Intente nuevamente.")
        return False
    else: return True

def validar_opcion_modificar(opcion):
    '''Valida la opción elegida en el menú de modificar activos'''

    if opcion == '' or not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:
        print("Opción inválida. Intente nuevamente.")
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
    """Ordena la matriz mediante selección por puntaje de confianza descendente; en caso de empate, ordena por nombre alfabéticamente."""

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

#=======================================================
#                        MENU
#=======================================================

def menu():
    """Muestra el menú principal y retorna la opción seleccionada por el usuario."""

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

    return opcion

def verificacion_menu (opcion, matriz):
    """Valida la opcion elegida por el usuario y ejecuta la operación correspondiente."""

    opciones_validas = ['1', '2', '3', '4', '8']

    while opcion not in opciones_validas:

        print("mOpción inválida. Intente nuevamente.\n")
        opcion = menu()

    if int(opcion) == 1:
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        if nombre.upper() != 'FIN':
            alta_activo(matriz, nombre)

    elif int(opcion) == 2:
        ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        while not validar_ticker(ticker) and ticker.upper() != 'FIN':
            ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        
        eliminar(matriz, ticker)

    elif int(opcion) == 3:
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        if nombre.upper() != 'FIN':
            modificar_activo(matriz, nombre)

    elif int(opcion) == 4:
        mostrar_matriz(matriz)

    elif int(opcion) == 8:
        print("Saliendo del programa...")

def menu_repetidos(activos_repetidos):
    '''Menú mostrado cuando hay múltiples activos que cumplen los requisitos de búsqueda'''

    print(f"Activos encontrados: ")
    for i in range(len(activos_repetidos)):
        print(f"{i+1}.")
        print(f"Nombre: \n", activos_repetidos[i][0])
        print(f"Metodologia: \n", activos_repetidos[i][4])

#=================================================================================
#             FUNCION MODIFICAR ORIGINAL (solicitado por el docente)
#=================================================================================

#def modificar(lista):

    #activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")

    #while activo_a_cambiar.upper() != 'FIN':
        
        #activo_encontrado = False

        #for i in lista:
            #if i[0].upper() == activo_a_cambiar.upper():
                #activo_encontrado = True
                #print(f"Activo encontrado: {i}")
                #print("1. Cambiar nombre del activo")
                #print("2. Cambiar ticker")
                #print("3. Cambiar valor de referencia")
                #print("4. Cambiar volumen de actividad")
                #print("5. Cambiar metodología de operación")
                #print("6. Cambiar unidades en tesorería")
                #print("7. Cambiar puntaje de confianza (1-10)")
                #print("8. Salir")

                #opcion_modificar = int(input("Ingrese el número de la opción que desea modificar: "))

                #if opcion_modificar < 1 or opcion_modificar > 8:
                    #print("Opción no válida. Intente nuevamente.")
                    #continue

                #while opcion_modificar != 8:
                    #if opcion_modificar == 1:
                        #nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                        #if nuevo_nombre == '':
                            #print('Error: El nombre no puede estar vacio. No se realizaron modificaciones')
                        #else:
                            #i[0] = nuevo_nombre
                    #elif opcion_modificar == 2:
                        #nuevo_ticker = input("Ingrese el nuevo ticker del activo: ")
                        #if nuevo_ticker == '' or len(nuevo_ticker) < 3:
                            #print('Error: El ticker no puede estar vacio y debe tener al menos 3 caracteres. No se realizaron modificaciones')
                        #else:
                            #i[1] = nuevo_ticker
                    #elif opcion_modificar == 3:
                        #nuevo_valor_ref = float(input("Ingrese el nuevo valor de referencia del activo: "))
                        #if nuevo_valor_ref <= 0:
                            #print('Error: El valor de referencia debe ser un número positivo. No se realizaron modificaciones')
                        #else:
                            #i[2] = nuevo_valor_ref
                    #elif opcion_modificar == 4:
                        #nuevo_vol_act = float(input("Ingrese el nuevo volumen de actividad del activo: "))
                        #if nuevo_vol_act < 0:
                            #print('Error: El volumen de actividad no puede ser negativo. No se realizaron modificaciones')
                        #else:
                            #i[3] = nuevo_vol_act
                    #elif opcion_modificar == 5:
                        #nuevos_metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL'] 
                        #print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        #nueva_met_op = int(input(f'Ingrese el numero de la nueva metodología de operación asignada: '))
                        #if nueva_met_op < 1 or nueva_met_op > 4:
                            #print('Error: La metodología de operación debe ser un número entre 1 y 4. No se realizaron modificaciones')
                        #else:
                            #i[4] = nuevos_metodos_validos[nueva_met_op - 1]
                    #elif opcion_modificar == 6:
                        #nuevas_unidades = float(input("Ingrese las nuevas unidades en tesorería del activo: "))
                        #if nuevas_unidades < 0:
                            #print('Error: Las unidades en tesorería no pueden ser negativas. No se realizaron modificaciones')
                        #else:
                            #i[5] = nuevas_unidades
                    #elif opcion_modificar == 7:
                        #nuevo_punt_conf = int(input("Ingrese el nuevo puntaje de confianza del activo (1-10): "))
                        #if nuevo_punt_conf < 1 or nuevo_punt_conf > 10:
                            #print('Error: El puntaje de confianza debe ser un número entre 1 y 10. No se realizaron modificaciones')
                        #else:
                            #i[6] = nuevo_punt_conf
                    #elif opcion_modificar == 8:
                        #print("Saliendo del menú de modificación.")
                    #else:
                        #print("Opción no válida. Intente nuevamente.")
                
                    #if opcion_modificar != 8:
                       #print("1. Cambiar nombre del activo")
                       #print("2. Cambiar ticker")
                       #print("3. Cambiar valor de referencia")
                       #print("4. Cambiar volumen de actividad")
                       #print("5. Cambiar metodología de operación")
                       #print("6. Cambiar unidades en tesorería")
                       #print("7. Cambiar puntaje de confianza (1-10)")
                       #print("8. Salir")

                       #opcion_modificar = int(input("Ingrese el número de la opción que desea modificar o 8 para salir: "))
        
        #if not activo_encontrado:
            #print("Activo no encontrado. Intente nuevamente.")

        #activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
    
    #return lista


#=======================================================
#               RF05 - GESTION DE ACTIVOS
#=======================================================

def alta_catalogo(catalogo):
    """Registra un nuevo activo en el catalogo.
    No permite activos con el mismo nombre.
    Repite hasta que el usuario ingrese 'fin'."""

    nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
    while not validar_nombre(nombre) and nombre.upper() != 'FIN':
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')

    while nombre.upper() != 'FIN':

        if busqueda_nombre_catalogo(catalogo, nombre):
            print('Error: ya existe un activo con ese nombre en el catalogo.')

        else:
            ticker = input('Ingrese el ticker del activo: ').upper()
            while not validar_ticker(ticker):
                ticker = input('Ingrese el ticker del activo: ').upper()

            valor_ref = input('Ingrese el valor de referencia en USD del activo: ')
            while not validar_valor(valor_ref):
                valor_ref = input('Ingrese el valor de referencia en USD del activo: ')

            vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')
            while not validar_volumen(vol_act):
                vol_act = input('Ingrese el volumen de actividad de las ultimas 24hs: ')

            print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
            metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
            met_op = input(f'Ingrese la metodologia de operacion asignada: ')
            while not validar_metodologia(met_op):
                print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                met_op = input(f'Ingrese la metodologia de operacion asignada: ')

            punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')
            while not validar_puntaje(punt_conf):
                punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')

        
            activo = [nombre, ticker, float(valor_ref), int(vol_act),
                      metodos_validos[int(met_op) - 1], int(punt_conf)]
            catalogo.append(activo)
            print('Activo agregado al catalogo correctamente.')

        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')

    print("\nVolviendo al menu...\n")


def baja_catalogo(catalogo, cartera):
    """Elimina un activo del catalogo por nombre.
    No permite eliminar si el activo tiene unidades en cartera.
    Repite hasta que el usuario ingrese 'fin'."""

    nombre = input('Ingrese el nombre del activo a eliminar o fin para finalizar: ')
    while not validar_nombre(nombre) and nombre.upper() != 'FIN':
        nombre = input('Ingrese el nombre del activo a eliminar o fin para finalizar: ')

    while nombre.upper() != 'FIN':

        activo = busqueda_nombre_catalogo(catalogo, nombre)

        if not activo:
            print('Activo no encontrado en el catalogo.')
        else:
            posicion = busqueda_nombre_cartera(cartera, nombre)
            if posicion:
                print('Error: el activo tiene unidades en cartera. Primero retire las unidades.')
            else:
                catalogo.remove(activo)
                print('Activo eliminado del catalogo exitosamente.')

        nombre = input('Ingrese el nombre del activo a eliminar o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre del activo a eliminar o fin para finalizar: ')

    print("\nVolviendo al menu...\n")


def modificar_catalogo(catalogo):
    """Permite modificar valor, volumen, metodologia o puntaje de un activo del catalogo.
    El nombre es el identificador y no puede modificarse.
    Repite hasta que el usuario ingrese 'fin'."""

    nombre = input('Ingrese el nombre del activo a modificar o fin para finalizar: ')
    while not validar_nombre(nombre) and nombre.upper() != 'FIN':
        nombre = input('Ingrese el nombre del activo a modificar o fin para finalizar: ')

    while nombre.upper() != 'FIN':

        activo = busqueda_nombre_catalogo(catalogo, nombre)

        if not activo:
            print('Activo no encontrado en el catalogo.')
        else:
            menu_modificar_catalogo()
            opcion = input('Ingrese el numero de la opcion o 5 para salir: ')
            while not validar_opcion_modificar_catalogo(opcion):
                opcion = input('Ingrese el numero de la opcion o 5 para salir: ')

            while int(opcion) != 5:

                if int(opcion) == 1:
                    nuevo_valor = input('Ingrese el nuevo valor de referencia en USD: ')
                    while not validar_valor(nuevo_valor):
                        nuevo_valor = input('Ingrese el nuevo valor de referencia en USD: ')
                    activo[2] = float(nuevo_valor)
                    print('Valor de referencia modificado exitosamente.')

                elif int(opcion) == 2:
                    nuevo_vol = input('Ingrese el nuevo volumen de actividad: ')
                    while not validar_volumen(nuevo_vol):
                        nuevo_vol = input('Ingrese el nuevo volumen de actividad: ')
                    activo[3] = int(nuevo_vol)
                    print('Volumen de actividad modificado exitosamente.')

                elif int(opcion) == 3:
                    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
                    print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                    nueva_met = input('Ingrese el numero de la nueva metodologia: ')
                    while not validar_metodologia(nueva_met):
                        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        nueva_met = input('Ingrese el numero de la nueva metodologia: ')
                    activo[4] = metodos_validos[int(nueva_met) - 1]
                    print('Metodologia modificada exitosamente.')

                elif int(opcion) == 4:
                    nuevo_puntaje = input('Ingrese el nuevo puntaje de confianza (1-10): ')
                    while not validar_puntaje(nuevo_puntaje):
                        nuevo_puntaje = input('Ingrese el nuevo puntaje de confianza (1-10): ')
                    activo[5] = int(nuevo_puntaje)
                    print('Puntaje de confianza modificado exitosamente.')

                menu_modificar_catalogo()
                opcion = input('Ingrese el numero de la opcion o 5 para salir: ')
                while not validar_opcion_modificar_catalogo(opcion):
                    opcion = input('Ingrese el numero de la opcion o 5 para salir: ')

            print('Saliendo del activo...')

        nombre = input('Ingrese el nombre del activo a modificar o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre del activo a modificar o fin para finalizar: ')

    print("\nVolviendo al menu...\n")


def mostrar_catalogo(catalogo):
    """Muestra todos los activos del catalogo ordenados por puntaje de confianza descendente."""

    if len(catalogo) == 0:
        print('El catalogo esta vacio.')
        input('\nPresione Enter para volver al menu...')
        return

    for i in range(len(catalogo) - 1):
        indice_max = i
        for j in range(i + 1, len(catalogo)):
            if int(catalogo[j][5]) > int(catalogo[indice_max][5]):
                indice_max = j
            elif int(catalogo[j][5]) == int(catalogo[indice_max][5]):
                if catalogo[j][0].upper() < catalogo[indice_max][0].upper():
                    indice_max = j
        catalogo[i], catalogo[indice_max] = catalogo[indice_max], catalogo[i]

    print("\n" + "=" * 100)
    print(f"{'NOMBRE':<25} {'TICKER':<7} {'VALOR USD':>12} {'VOLUMEN 24H':>18} {'METODOLOGIA':<16} {'PUNTAJE':>7}")
    print("=" * 100)

    for activo in catalogo:
        print(f"{activo[0]:<25} {activo[1]:<7} {activo[2]:>12.2f} {activo[3]:>18,} {activo[4]:<16} {activo[5]:>7}")

    print("=" * 100)
    input('\nPresione Enter para volver al menu...')


#=======================================================
#               RF05 - GESTION DE CARTERA
#=======================================================

def alta_cartera(cartera, catalogo):
    """Agrega un activo a la cartera.
    RESTRICCION RF05: solo permite activos previamente dados de alta en el catalogo.
    Repite hasta que el usuario ingrese 'fin'."""

    nombre = input('Ingrese el nombre del activo a agregar a la cartera o fin para finalizar: ')
    while not validar_nombre(nombre) and nombre.upper() != 'FIN':
        nombre = input('Ingrese el nombre del activo a agregar a la cartera o fin para finalizar: ')

    while nombre.upper() != 'FIN':

        if not busqueda_nombre_catalogo(catalogo, nombre):
            print('Error: el activo no esta registrado en el catalogo.')
            print('Primero debe darlo de alta en Gestion de Activos.')

        elif busqueda_nombre_cartera(cartera, nombre):
            print('Error: el activo ya tiene una posicion en la cartera.')

        else:
            unidades = input('Ingrese la cantidad de unidades iniciales: ')
            while not validar_unidades(unidades):
                unidades = input('Ingrese la cantidad de unidades iniciales: ')

            cartera.append([nombre, float(unidades)])
            print('Activo agregado a la cartera exitosamente.')

        nombre = input('Ingrese el nombre del activo a agregar a la cartera o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre del activo a agregar a la cartera o fin para finalizar: ')

    print("\nVolviendo al menu...\n")


def baja_cartera(cartera):
    """Elimina una posicion de la cartera por nombre del activo.
    Repite hasta que el usuario ingrese 'fin'."""

    nombre = input('Ingrese el nombre del activo a retirar de la cartera o fin para finalizar: ')
    while not validar_nombre(nombre) and nombre.upper() != 'FIN':
        nombre = input('Ingrese el nombre del activo a retirar de la cartera o fin para finalizar: ')

    while nombre.upper() != 'FIN':

        posicion = busqueda_nombre_cartera(cartera, nombre)

        if not posicion:
            print('El activo no se encuentra en la cartera.')
        else:
            cartera.remove(posicion)
            print('Activo retirado de la cartera exitosamente.')

        nombre = input('Ingrese el nombre del activo a retirar de la cartera o fin para finalizar: ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('Ingrese el nombre del activo a retirar de la cartera o fin para finalizar: ')

    print("\nVolviendo al menu...\n")


def mostrar_cartera(cartera, catalogo):
    """Muestra todas las posiciones de la cartera con informacion del catalogo y valor total."""

    if len(cartera) == 0:
        print('La cartera esta vacia.')
        input('\nPresione Enter para volver al menu...')
        return

    print("\n" + "=" * 85)
    print(f"{'NOMBRE':<25} {'TICKER':<7} {'UNIDADES':>12} {'VALOR USD':>12} {'TOTAL USD':>14}")
    print("=" * 85)

    for posicion in cartera:
        activo = busqueda_nombre_catalogo(catalogo, posicion[0])
        if activo:
            ticker = activo[1]
            valor  = activo[2]
        else:
            ticker = '???'
            valor  = 0
        total = posicion[1] * valor
        print(f"{posicion[0]:<25} {ticker:<7} {posicion[1]:>12,.2f} {valor:>12.2f} {total:>14,.2f}")

    print("=" * 85)
    input('\nPresione Enter para volver al menu...')


#=======================================================
#          RF05 - FUNCIONES BACK DE BUSQUEDA
#=======================================================

def busqueda_nombre_catalogo(catalogo, nombre):
    """Busca un activo en el catalogo por nombre exacto usando for-else.
    Retorna el activo si lo encuentra, None si no existe."""

    for activo in catalogo:
        if activo[0].upper() == nombre.upper():
            return activo
    else:
        return None


def busqueda_nombre_cartera(cartera, nombre):
    """Busca una posicion en la cartera por nombre de activo usando for-else.
    Retorna la posicion si existe, None si no."""

    for posicion in cartera:
        if posicion[0].upper() == nombre.upper():
            return posicion
    else:
        return None


def validar_opcion_modificar_catalogo(opcion):
    """Valida que la opcion del menu de modificar catalogo sea un numero entre 1 y 5.
    Retorna True si es valido."""

    if opcion == '' or not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 5:
        print('Opcion invalida. Intente nuevamente.')
        return False
    return True


#=======================================================
#          RF05 - MENUS NUEVOS
#=======================================================

def menu_principal():
    """Muestra el menu principal con las dos secciones y retorna la opcion seleccionada."""

    print('=' * 50)
    print('  SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB')
    print('=' * 50)
    print('1. Gestion de Activos')
    print('2. Gestion de Cartera')
    print('8. Salir')
    print('=' * 50)

    opcion = input('Ingrese el numero de la opcion: ')
    return opcion


def menu_gestion_activos():
    """Muestra el submenu de gestion del catalogo de activos y retorna la opcion seleccionada."""

    print('=' * 50)
    print('         GESTION DE ACTIVOS')
    print('=' * 50)
    print('1. Alta de activo')
    print('2. Baja de activo')
    print('3. Modificar activo')
    print('4. Ver catalogo completo')
    print('8. Volver al menu principal')
    print('=' * 50)

    opcion = input('Ingrese el numero de la opcion: ')
    return opcion


def menu_gestion_cartera():
    """Muestra el submenu de gestion de cartera y retorna la opcion seleccionada."""

    print('=' * 50)
    print('          GESTION DE CARTERA')
    print('=' * 50)
    print('1. Agregar activo a la cartera')
    print('2. Retirar activo de la cartera')
    print('3. Ver cartera')
    print('8. Volver al menu principal')
    print('=' * 50)

    opcion = input('Ingrese el numero de la opcion: ')
    return opcion


def menu_modificar_catalogo():
    """Muestra el submenu de modificacion de un activo del catalogo."""

    print('\n--- Que desea modificar? ---')
    print('1. Valor de referencia en USD')
    print('2. Volumen de actividad')
    print('3. Metodologia de operacion')
    print('4. Puntaje de confianza')
    print('5. Salir')