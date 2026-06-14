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
        
        met_op = predecir_metodologia()
                    
        unidades = input('Ingrese las unidades totales en tesoreria: ')

        while not validar_unidades(unidades):
            unidades = input('Ingrese las unidades totales en tesoreria: ')
                           
        punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')

        while not validar_puntaje(punt_conf):
            punt_conf = input('Ingrese el puntaje de confianza del 1 al 10: ')
        
        if validar_repetidos(nombre, ticker, met_op, matriz):

            activo = [nombre,ticker.upper(),float(valor_ref),int(vol_act), met_op, float(unidades),int(punt_conf)]
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
                    nueva_met_op = predecir_metodologia()
                    activo_encontrado[4] = nueva_met_op
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

def predecir_metodologia():
    """Solicita al usuario una metodología (texto, mín. 3 letras) y la valida contra metodos_validos,
    permitiendo coincidencias parciales con confirmación. Retorna el nombre completo y válido de la metodología."""

    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']      
    print(metodos_validos)
    met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()

    while not validar_metodologia(met_op):
        print(metodos_validos)
        met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()
    
    while validar_metodologia(met_op):
 
        coincidencias_parciales = []
        
        for i in metodos_validos:
            if i.replace(' ', '').lower() == met_op.replace(' ', '').lower():
                return i
            elif met_op.replace(' ', '').lower() in i.replace(' ', '').lower():
                coincidencias_parciales.append(i)
     
        if len(coincidencias_parciales) == 1:
            confirmacion = input(f'¿Quiso decir {coincidencias_parciales[0]}? (s/n): ').lower()
            if confirmacion == 's':
                return coincidencias_parciales[0]
            elif confirmacion == 'n': met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()
            else: 
                print('Opcion invalida. Intente nuevamente')
                met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()
        elif len(coincidencias_parciales) > 1:
            print(f'Coincide con varias opciones: {coincidencias_parciales}')
            print('Sea mas especifico. Intente nuevamente.')
            met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()
        else:
            print('No se encontraron coincidencias de metodologias. Intente nuevamente.')
            met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()
        
        while not validar_metodologia(met_op):
            met_op = input('Ingrese la metodología de operación (min. 3 letras): ').replace(' ', '').lower()

def volumen_superior_al_promedio(matriz):

    """Calcula el promedio de volumen de todos los activos y muestra los que superan el promedio."""
    volumen = 0

    for i in range(len(matriz)):
        volumen += matriz[i][3]

    promedio = volumen / len(matriz)

    print(f"\nEl promedio de volumen es: {promedio}")
    
    print("\n" + "=" * 80)
    print(f"{'NOMBRE':<25} {'VOLUMEN':>18} {'DIFERENCIA':>25}")
    print("=" * 80)

    for i in range(len(matriz)):
        if matriz[i][3] > promedio:
            print(f"{matriz[i][0]:<25} {float(matriz[i][3]):>18,.2f} {float(matriz[i][3] - promedio):>25,.2f}")
    
    print("=" * 80)

    input("\nPresione Enter para volver al menú principal...")      

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
    if nombre == '' or nombre.replace(' ', '').isnumeric():
        print('El nombre del activo no puede estar vacío ni contener caracteres no alfabéticos. Intente nuevamente.')
        return False
    else:
        return True

def validar_ticker(ticker):
    """Valida que el ticker tenga entre 3 y 5 caracteres alfabéticos. Retorna True si es válido."""
    if ticker == '' or not ticker.replace('.', '').isalpha() or ticker.count('.') > 1 or len(ticker) < 3 or len(ticker) > 5 or ticker.upper() == 'FIN':
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
    if metodologia == '' or not metodologia.replace(' ', '').isalpha() or len(metodologia) < 3:
        print('Error. Debe ingresar al menos 3 letras. Intente nuevamente.')
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
    metodos_validos = ['Scalping', 'DayTrading', 'SwingTrading', 'HODL']  

    for i in matriz:
        if metodologia == i[4] and nombre.upper() == i[0].upper():
            print('Activo ya existente en el sistema.')
            return False
        elif metodologia == i[4] and ticker.upper() == i[1].upper():
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
    print("5. Informe Activos con Volumen superior al promedio")
    print("8. Salir")
    print('='*50)

    opcion = input('Ingrese el numero de la opcion que desea ejecutar: ')

    return opcion

def verificacion_menu (opcion, matriz):
    """Valida la opcion elegida por el usuario y ejecuta la operación correspondiente."""

    opciones_validas = ['1', '2', '3', '4', '5', '8']

    while opcion not in opciones_validas:

        print("Opción inválida. Intente nuevamente.\n")
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
    
    elif int(opcion) == 5:
        volumen_superior_al_promedio(matriz)

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
