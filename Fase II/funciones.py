
#=======================================================
#                FUNCIONES FRONT
#=======================================================

def eliminar_activo(matriz, ticker):

    """Elimina un activo de la matriz según su ticker. Repite hasta que el usuario ingrese 'fin'."""

    while ticker.upper() != 'FIN':

        activos = busqueda_ticker(matriz, ticker)

        if activos != False:
            if len(activos) > 1:
                menu_repetidos(activos)

                opcion = input("\033[93mEscoja el numero del ticker a eliminar por su metodologia:\033[0m ")

                while not validar_opcion_repetidos(opcion, activos):
                    opcion = input("\033[93mEscoja el numero del ticker a eliminar por su metodologia:\033[0m  ")

                matriz.remove(activos[int(opcion)-1])
                print("\033[92mActivo eliminado exitosamente\033[0m")

            elif len(activos) == 1:
                matriz.remove(activos[0])
                print("\033[92mActivo eliminado exitosamente\033[0m")

        ticker = input('\033[93mIngrese el ticker del activo que desea eliminar o fin para finalizar:\033[0m ').upper()
        while not validar_ticker(ticker) and ticker.upper() != 'FIN':
            ticker = input('\033[93mIngrese el ticker del activo que desea eliminar o fin para finalizar:\033[0m ').upper()

    print("\n\033[92mVolviendo al menu principal...\033[0m")

def eliminar_activo_catalogo(catalogo, nombre, matriz):
    """Elimina un activo del catálogo y sus ocurrencias en cartera. Repite hasta 'fin'."""

    while nombre.upper() != 'FIN':

        activos = busqueda_nombre(catalogo, nombre)

        if activos != False:
            catalogo.remove(activos[0])

            activos_cartera = busqueda_nombre(matriz, nombre)
            if activos_cartera != False:
                for activo in activos_cartera:
                    matriz.remove(activo)

            print("\033[92mActivo eliminado exitosamente\033[0m")

        nombre = input('\033[93mIngrese el nombre del activo que desea eliminar o fin para finalizar:\033[0m ').upper()
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre del activo que desea eliminar o fin para finalizar:\033[0m ').upper()

    print("\n\033[92mVolviendo al menu principal...\033[0m")

def alta_activo(matriz, nombre, catalogo):

    """Solicita los datos de un nuevo activo y lo agrega a la matriz. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        ticker = input('\033[93mIngrese el ticker del activo:\033[0m ').upper()

        while not validar_ticker(ticker):
            ticker = input('\033[93mIngrese el ticker del activo:\033[0m ').upper()
       
        met_op = ingreso_metodologia()
                    
        unidades = input('\033[93mIngrese las unidades totales en tesoreria:\033[0m ')

        while not validar_unidades_alta(unidades):
            unidades = input('\033[93mIngrese las unidades totales en tesoreria:\033[0m ')
        
        if activo_en_catalogo(nombre, catalogo):
            for i in catalogo:
                if i[0].upper() == nombre.upper():
                    punt_conf = i[4]
                    vol_act = i[2]
                    valor_ref = i[1]
                                  
            if validar_repetidos(nombre, ticker, met_op, matriz) and activo_en_catalogo(nombre, catalogo):

               activo = [nombre,ticker.upper(),float(valor_ref),int(vol_act), met_op, float(unidades),int(punt_conf)]
               matriz.append(activo)
               print('\033[92mDatos del activo agregados correctamente.\033[0m ')

        else: 
            print('\033[91mEl activo no se encuentra en el catalogo. Intente otra vez.\033[0m')

        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m  ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')

    if nombre.upper() == 'FIN':
        print("\n\033[92mVolviendo al menu principal...\033[0m \n")
    
def alta_activo_catalogo(matriz, nombre):

    """Registra un nuevo activo en el catalogo.
    No permite activos con el mismo nombre.
    Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        valor_ref = input('\033[93mIngrese el valor de referencia base (Ej: USD) del activo:\033[0m ')

        while not validar_valor(valor_ref):
            valor_ref = input('\033[93mIngrese el valor de referencia base (Ej: USD) del activo:\033[0m ')

        vol_act = input('\033[93mIngrese el volumen de actividad de las ultimas 24hs:\033[0m ')

        while not validar_volumen(vol_act):
            vol_act = input('\033[93mIngrese el volumen de actividad de las ultimas 24hs:\033[0m ')
        
        met_op = ingreso_metodologia()

        punt_conf = input('\033[93mIngrese el puntaje de confianza del 1 al 10:\033[0m ')

        while not validar_puntaje(punt_conf):
            punt_conf = input('\033[93mIngrese el puntaje de confianza del 1 al 10:\033[0m ')
        
        if validar_repetidos_catalogo(nombre, matriz):

            activo = [nombre, float(valor_ref), int(vol_act), met_op, int(punt_conf)]
            matriz.append(activo)
            print('\033[92mDatos del activo agregados correctamente.\033[0m ')

        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m  ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')

    if nombre.upper() == 'FIN':
        print("\n\033[92mVolviendo al menu principal...\033[0m \n")

def modificar_activo(matriz, nombre):
    """Permite modificar los campos de un activo existente identificado por nombre. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        activo_encontrado = busqueda_nombre(matriz, nombre)

        if activo_encontrado:

            if len(activo_encontrado) > 1:
                menu_repetidos(activo_encontrado)

                opcion = input("\033[93mEscoja el nombre a modificar por su metodologia:\033[0m ")

                while not validar_opcion_repetidos(opcion, activo_encontrado):
                    opcion = input("\033[93mEscoja el nombre a modificar por su metodologia:\033[0m ")

                activo_encontrado = activo_encontrado[int(opcion)-1]

            elif len(activo_encontrado) == 1:

                activo_encontrado = activo_encontrado[0]

            menu_modificar()
            opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            while not validar_opcion_modificar(opcion):
                menu_modificar()
                opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            while int(opcion) != 8:

                if int(opcion) == 1:
                    nuevo_ticker = input("\033[93mIngrese el nuevo ticker del activo:\033[0m ").upper()
                    while not validar_ticker(nuevo_ticker):
                        nuevo_ticker = input("\033[93mIngrese el nuevo ticker del activo:\033[0m ").upper()

                    activo_encontrado[1] = nuevo_ticker
                    print("\n\033[92mTicker del activo modificado exitosamente.\033[0m")

                elif int(opcion) == 2:
                    nueva_met_op = ingreso_metodologia()
                    activo_encontrado[4] = nueva_met_op
                    print("\n\033[92mMetodología de operación del activo modificada exitosamente.\033[0m")                   

                elif int(opcion) == 3:
                    nuevas_unidades = input("\033[93mIngrese las nuevas unidades en tesorería del activo:\033[0m ")
                    while not validar_unidades(nuevas_unidades, activo_encontrado):
                        nuevas_unidades = input("\033[93mIngrese las nuevas unidades en tesorería del activo:\033[0m ")

                    activo_encontrado[5] += float(nuevas_unidades)
                    print("\n\033[92mUnidades en tesorería del activo modificadas exitosamente.\033[0m")

                menu_modificar()
                opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

                while not validar_opcion_modificar(opcion):
                    opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            print("\n\033[92mSaliendo del activo...\033[0m")

        nombre = input("\033[93mIngrese el nombre del activo que desea modificar o fin para finalizar:\033[0m ")
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input("\033[93mIngrese el nombre del activo que desea modificar o fin para finalizar:\033[0m ")

def modificar_activo_catalogo(matriz, nombre, cartera):
    """Permite modificar los campos de un activo existente identificado por nombre. Repite hasta que el usuario ingrese 'fin'."""

    while nombre.upper() != 'FIN':

        activo_encontrado = busqueda_nombre(matriz, nombre)
        activo_cartera = busqueda_nombre(cartera, nombre)

        if activo_encontrado:

            activo_encontrado = activo_encontrado[0]

            menu_modificar_catalogo()
            opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            while not validar_opcion_modificar_catalogo(opcion):
                menu_modificar_catalogo()
                opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            while int(opcion) != 5:

                if int(opcion) == 1:
                    nuevo_valor_ref = input("\033[93mIngrese el nuevo valor de referencia del activo:\033[0m ")
                    while not validar_valor(nuevo_valor_ref):
                        nuevo_valor_ref = input("\033[93mIngrese el nuevo valor de referencia del activo:\033[0m ")

                    activo_encontrado[1] = float(nuevo_valor_ref)

                    if activo_cartera != False:
                        for i in activo_cartera:
                            if i[0] == activo_encontrado[0]:
                                i[2] = float(nuevo_valor_ref)

                    print("\n\033[92mValor de referencia del activo modificado exitosamente.\033[0m")

                elif int(opcion) == 2:
                    nuevo_vol_act = input("\033[93mIngrese el nuevo volumen de actividad del activo:\033[0m ")
                    while not validar_volumen(nuevo_vol_act):
                        nuevo_vol_act = input("\033[93mIngrese el nuevo volumen de actividad del activo:\033[0m ")

                    activo_encontrado[2] = int(nuevo_vol_act)
                    
                    if activo_cartera != False:
                        for i in activo_cartera:
                           if i[0] == activo_encontrado[0]:
                              i[3] = float(nuevo_vol_act)
                    print("\n\033[92mVolumen de actividad del activo modificado exitosamente.\033[0m")
                
                elif int(opcion) == 3:
                    nueva_met_op = ingreso_metodologia()
                    activo_encontrado[3] = nueva_met_op
                    print("\n\033[92mMetodología de operación del activo modificada exitosamente.\033[0m")

                elif int(opcion) == 4:
                    nuevo_punt_conf = input("\033[93mIngrese el nuevo puntaje de confianza del activo (1-10):\033[0m ")
                    while not validar_puntaje(nuevo_punt_conf):
                        nuevo_punt_conf = input("\033[93mIngrese el nuevo puntaje de confianza del activo (1-10):\033[0m ")

                    activo_encontrado[4] = int(nuevo_punt_conf)

                    if activo_cartera != False:
                        for i in activo_cartera:
                           if i[0] == activo_encontrado[0]:
                              i[6] = float(nuevo_punt_conf)
                    print("\n\033[92mPuntaje de confianza del activo modificado exitosamente.\033[0m")

                menu_modificar_catalogo()
                opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

                while not validar_opcion_modificar_catalogo(opcion):
                    opcion = input("\033[93mIngrese el número de la opción que desea modificar u 8 para salir:\033[0m ")

            print("\n\033[92mSaliendo del activo...\033[0m")

        nombre = input("\033[93mIngrese el nombre del activo que desea modificar o fin para finalizar:\033[0m ")
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input("\033[93mIngrese el nombre del activo que desea modificar o fin para finalizar:\033[0m ")

def mostrar_matriz(matriz):
    """Muestra todos los activos de la matriz ordenados por puntaje de confianza descendente."""

    ordenar_matriz(matriz)

    print("\n" + "=" * 110)

    print(f"{'NOMBRE':<25} {'TICKER':<8} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'UNIDADES':>14} {'PUNTAJE':>8}")
    
    print("=" * 110)

    for activo in matriz:
        print(f"{activo[0]:<25} {activo[1]:<8} {float(activo[2]):>12.2f} {int(activo[3]):>18,} {activo[4]:>15} {float(activo[5]):>14,.2f} {int(activo[6]):>8}")
    
    print("=" * 110)

    input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")

def mostrar_catalogo(matriz):
    """Muestra todos los activos de la matriz ordenados por puntaje de confianza descendente."""

    ordenar_catalogo(matriz)

    print("\n" + "=" * 110)

    print(f"{'NOMBRE':<25} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'PUNTAJE':>8}")
    
    print("=" * 110)

    for activo in matriz:
        print(f"{activo[0]:<25} {float(activo[1]):>12.2f} {int(activo[2]):>18,} {activo[3]:>15} {int(activo[4]):>8}")
    
    print("=" * 110)

    input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")

def ingreso_metodologia():
    """Solicita al usuario una metodología (texto, mín. 3 letras) y la valida contra metodos_validos,
    permitiendo coincidencias parciales con confirmación. Retorna el nombre completo y válido de la metodología."""

    metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
    
    menu_metodologia(metodos_validos)

    met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()

    while not validar_metodologia(met_op):
        menu_metodologia(metodos_validos)
        met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()
    
    while validar_metodologia(met_op):
 
        coincidencias_parciales = []
        
        for i in metodos_validos:
            if i.replace(' ', '').lower() == met_op.lower():
                return i
            elif met_op.lower() in i.replace(' ', '').lower():
                coincidencias_parciales.append(i)
     
        if len(coincidencias_parciales) == 1:
            confirmacion = input(f'\033[93m¿Quiso decir {coincidencias_parciales[0]}? (s/n):\033[0m ').lower()
            if confirmacion == 's':
                return coincidencias_parciales[0]
            
            elif confirmacion == 'n': 
                menu_metodologia(metodos_validos)
                met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()
            
            else: 
                print('\033[91mOpcion inválida. Intente nuevamente\033[0m')
                menu_metodologia(metodos_validos)
                met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()
        
        elif len(coincidencias_parciales) > 1:
            menu_metodologias_repetidas(coincidencias_parciales)
            confirmacion = input("\033[93mIngrese el número de una de estas metodologías o 'n' si ninguna es la deseada: \033[0m ")
            
            if confirmacion.lower() != 'n':

                while not validar_opcion_repetidos(confirmacion, coincidencias_parciales):
                    confirmacion = input("\033[93mIngrese el número de una de estas metodologías o 'n' si ninguna es la deseada: \033[0m ")   

            if confirmacion.lower() == 'n':
                menu_metodologia(metodos_validos)
                met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()
            
            elif validar_opcion_repetidos(confirmacion, coincidencias_parciales):
                return coincidencias_parciales[int(confirmacion)-1]

        else:
            print('\033[91mNo se encontraron coincidencias de metodologias. Intente nuevamente.\033[0m')
            menu_metodologia(metodos_validos)
            met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()
        
        while not validar_metodologia(met_op):
            menu_metodologia(metodos_validos)
            met_op = input('\033[93mIngrese la metodología de operación (min. 3 letras):\033[0m ').replace(' ', '').lower()

def volumen_superior_al_promedio(matriz):

    """Calcula el promedio de volumen de todos los activos y muestra los que superan el promedio."""

    if not matriz:
        print('\033[91mNo hay activos registrados en el sistema.\033[0m')
        input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")
        return None

    volumen = 0

    for i in range(len(matriz)):
        volumen += matriz[i][3]

    promedio = volumen / len(matriz)

    print(f"\nEl promedio de volumen es: {promedio}")
    
    print("\n" + "=" * 80)
    print(f"{'NOMBRE':<25} {'VOLUMEN':>18} {'DIFERENCIA':>25}")
    print("=" * 80)

    superiores_promedio = False
 
    for i in range(len(matriz)):
        if matriz[i][3] > promedio:
            print(f"{matriz[i][0]:<25} {float(matriz[i][3]):>18,.2f} {float(matriz[i][3] - promedio):>25,.2f}")
            superiores_promedio = True
    
    if not superiores_promedio:
        print(f'\033[91mNo hay activos cuyo volumen sea superior al promedio\033[0m')
    
    print("=" * 80)

    input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")      

def volumen_superior_al_promedio_catalogo(catalogo):
    """Calcula el promedio de volumen del catálogo y muestra los activos que lo superan.
    
    Parámetros:
        catalogo (list): lista de activos del catálogo [nombre, valor_ref, vol_act, met_op, punt_conf].
    """

    if not catalogo:
        print('\033[91mNo hay activos registrados en el sistema.\033[0m')
        input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")
        return None

    volumen = 0

    for i in range(len(catalogo)):
        volumen += catalogo[i][2]

    promedio = volumen / len(catalogo)

    print(f"\nEl promedio de volumen es: {promedio:,.2f}")

    print("\n" + "=" * 80)
    print(f"{'NOMBRE':<25} {'VOLUMEN':>18} {'DIFERENCIA':>25}")
    print("=" * 80)

    superiores_promedio = False

    for i in range(len(catalogo)):
        if catalogo[i][2] > promedio:
            print(f"{catalogo[i][0]:<25} {float(catalogo[i][2]):>18,.2f} {float(catalogo[i][2] - promedio):>25,.2f}")
            superiores_promedio = True

    if not superiores_promedio:
        print('\033[91mNo hay activos cuyo volumen sea superior al promedio\033[0m')

    print("=" * 80)

    input("\n\033[93mPresione Enter para volver al menú principal...\033[0m")

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
        print("\033[91mActivo no encontrado. Asegúrese que tenga 0 unidades en tesorería.\033[0m")
        return False

def busqueda_nombre(matriz, nombre):
    """Busca activos por nombre en la matriz. Retorna la lista de coincidencias o False si no hay ninguna."""

    nombres_encontrados = []

    for i in matriz:

        if i[0].upper() == nombre.upper():

            nombres_encontrados.append(i)

    if len(nombres_encontrados) == 1:
        print(f"\033[93mActivo encontrado: {nombres_encontrados[0][0]}\033[0m")
        return nombres_encontrados
    elif len(nombres_encontrados) > 1:
        print("\033[93mSe encontraron múltiples activos con el mismo nombre.\033[0m")
        return nombres_encontrados
    elif len(nombres_encontrados) == 0:
        print("\033[91mActivo no encontrado.\033[0m")
        return False

def validar_nombre(nombre):
    """Valida que el nombre no esté vacío ni sea puramente numérico. Retorna True si es válido."""
    if nombre == '' or nombre.replace(' ', '').isnumeric():
        print('\033[91mEl nombre del activo no puede estar vacío ni ser puramente numérico. Intente nuevamente.\033[0m')
        return False
    else:
        return True

def validar_ticker(ticker):
    """Valida que el ticker tenga entre 3 y 5 caracteres alfabéticos. Retorna True si es válido."""
    if ticker == '' or not ticker.replace('.', '').isalpha() or ticker.count('.') > 1 or len(ticker) < 3 or len(ticker) > 5 or ticker.upper() == 'FIN':
        print('\033[91mEl ticker debe tener entre 3 y 5 caracteres, no puede estar vacío, y solo puede contener caracteres alfabéticos. Intente nuevamente.\033[0m')
        return False
    else:
        return True

def validar_valor(valor_ref):
    """Valida que el valor de referencia sea un número decimal positivo. Retorna True si es válido."""
    if valor_ref == '' or valor_ref.count(".") > 1 or not valor_ref.replace(".", "").isnumeric() or float(valor_ref) < 0:
        print('\033[91mEl valor de referencia debe ser un número positivo, y no puede estar vacío. Intente nuevamente.\033[0m')
        return False
    else:
        return True

def validar_volumen(volumen):
    """Valida que el volumen de actividad sea un entero no negativo. Retorna True si es válido."""
    if volumen == '' or not volumen.isnumeric() or int(volumen) < 0 :
        print('\033[91mEl volumen de actividad debe ser un número positivo, y no puede estar vacío. Intente nuevamente.\033[0m')
        return False
    else: 
        return True

def validar_metodologia(metodologia):
    """Valida que la metodología tenga al menos 3 letras y solo caracteres alfabéticos (espacios permitidos). Retorna True si es válido."""
    if metodologia == '' or not metodologia.replace(' ', '').isalpha() or len(metodologia) < 3:
        print('\033[91mError. Debe ingresar al menos 3 letras. Intente nuevamente.\033[0m')
        return False
    else:
        return True
    
def validar_unidades(unidades, cartera):
    """Valida que las unidades en tesorería sean un número no negativo. Retorna True si es válido."""
    if unidades == '' or unidades.count(".") > 1 or not unidades.replace(".", "").replace("-", "").isnumeric() or float(unidades) < -(float(cartera[5])):
        print('\033[91mLa compra/venta debe ser un número (puede tener .), si desea vender asegúrese de tener la cantidad deseada en tesorería\033[0m')
        return False
    else:
        return True

def validar_unidades_alta(unidades):
    """Valida que las unidades iniciales al dar de alta sean un número positivo. Retorna True si es válido."""
    if unidades == '' or unidades.count(".") > 1 or not unidades.replace(".", "").isnumeric() or float(unidades) < 0:
        print('\033[91mLas unidades deben ser un número positivo. Intente nuevamente.\033[0m')
        return False
    else:
        return True
    
def validar_puntaje(puntaje):
    """Valida que el puntaje de confianza sea un entero entre 1 y 10. Retorna True si es válido."""
    if puntaje == '' or not puntaje.isnumeric() or int(puntaje) < 1 or int(puntaje) > 10 :
        print('\033[91mEl puntaje de confianza debe ser un número entre 1 y 10, y no puede estar vacío. Intente nuevamente.\033[0m')
        return False
    else:
        return True

def validar_repetidos(nombre, ticker, metodologia, matriz):
    """Verifica que no exista un activo con igual nombre o ticker y misma metodología. Retorna True si no hay duplicado."""

    for i in matriz:
        if metodologia == i[4] and nombre.upper() == i[0].upper():
            print('\033[91mActivo ya existente en el sistema.\033[0m')
            return False
        elif metodologia == i[4] and ticker.upper() == i[1].upper():
            print('\033[91mActivo ya existente en el sistema.\033[0m')
            return False
    else:
        return True

def validar_repetidos_catalogo(nombre, matriz):
    """Verifica que no exista un activo con igual nombre o ticker y misma metodología. Retorna True si no hay duplicado."""

    for i in matriz:
        if nombre.upper() == i[0].upper():
            print('\033[91mActivo ya existente en el sistema.\033[0m')
            return False
    else:
        return True
    
def validar_opcion_repetidos(opcion, activos):
    '''Valida la opción elegida en el menú para seleccionar el activo que desea el usuario en caso de que hayan varios con el mismo nombre o ticker'''

    if opcion == '' or not opcion.isnumeric() or int(opcion) > len(activos) or int(opcion) <= 0:
        print("\033[91mOpción no válida. Intente nuevamente.\033[0m")
        return False
    else: 
        return True

def validar_opcion_modificar(opcion):
    '''Valida la opción elegida en el menú de modificar activos'''

    if opcion == '' or not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 8:
        print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
        return False
    else: 
        return True

def validar_opcion_modificar_catalogo(opcion):
    '''Valida la opción elegida en el menú de modificar activos'''

    if opcion == '' or not opcion.isnumeric() or int(opcion) < 1 or int(opcion) > 5:
        print("\033[91mOpción inválida. Intente nuevamente.\033[0m")
        return False
    else: 
        return True

def activo_en_catalogo(nombre, catalogo):
    """Verifica si un activo existe en el catálogo por nombre (sin distinción de mayúsculas). Retorna True si existe, False si no."""

    for i in catalogo:
        if i[0].upper() == nombre.upper():
            return True
    else: return False

def menu_modificar():
    """Muestra el submenú de opciones para modificar los campos de un activo."""

    print("\033[92m1. Cambiar ticker\033[0m")
    print("\033[92m2. Cambiar metodología de operación\033[0m")
    print("\033[92m3. Cambiar unidades en tesorería\033[0m")
    print("\033[92m8. Salir\033[0m")

def menu_modificar_catalogo():
    """Muestra el submenú de opciones para modificar los campos de un activo en el catálogo."""

    print("\033[92m1. Cambiar valor de referencia\033[0m")
    print("\033[92m2. Cambiar volumen de actividad\033[0m")
    print("\033[92m3. Cambiar metodología\033[0m")
    print("\033[92m4. Cambiar puntaje de confianza (1-10)\033[0m")
    print("\033[92m5. Salir\033[0m")

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

def ordenar_catalogo(catalogo):
    """Ordena el catálogo por puntaje de confianza descendente; empate por nombre alfabético."""
    for i in range(len(catalogo) - 1):
        indice_max = i
        for j in range(i + 1, len(catalogo)):
            if int(catalogo[j][4]) > int(catalogo[indice_max][4]):
                indice_max = j
            elif int(catalogo[j][4]) == int(catalogo[indice_max][4]):
                if catalogo[j][0].upper() < catalogo[indice_max][0].upper():
                    indice_max = j
        catalogo[i], catalogo[indice_max] = catalogo[indice_max], catalogo[i]

def menu_metodologia(metodologias):
    """Muestra las metodologías de operación disponibles en el sistema."""
    print("\033[93mMetodologías disponibles:\033[0m")
    for i in metodologias[0:3]:
        print(f"\033[93m{i}, \033[0m", end='')
    print(f"\033[93m{metodologias[3]}\033[0m")

def menu_metodologias_repetidas(coincidencias):
    """Muestra las metodologías que coinciden parcialmente con el texto ingresado por el usuario."""
    print('\033[91mCoincide con varias opciones:\033[0m')
    for i in range(len(coincidencias)):
        print(f"\033[93m{i+1}. {coincidencias[i]} \033[0m", end='')
    print()

def menu_repetidos(activos_repetidos):
    """Muestra una lista numerada de activos cuando hay múltiples coincidencias en la búsqueda, para que el usuario seleccione uno."""

    print(f"\033[93mActivos encontrados: \033[0m")
    for i in range(len(activos_repetidos)):
        print(f"\033[93m{i+1}.\033[0m")
        print(f"\033[93mNombre:\n {activos_repetidos[i][0]}\033[0m")
        print(f"\033[93mMetodologia:\n {activos_repetidos[i][4]}\033[0m")

#=======================================================
#                        MENU
#=======================================================

def menu_gestion_cartera():
    """Muestra el menú de gestion de cartera y retorna la opción seleccionada por el usuario."""

    print('\033[92m' + '='*50 + '\033[0m')
    print('\033[92m' + ' '*2 + 'SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB' + '\033[0m')
    print('\033[92m' + '='*50 + '\033[0m')
    print("\033[92m1. Registrar nuevo activo (Alta)\033[0m")
    print("\033[92m2. Eliminar activo del sistema (Baja)\033[0m")
    print("\033[92m3. Modificar valoracion o puntaje (Modificacion)\033[0m")
    print("\033[92m4. Informe General - Visualizacion de los datos\033[0m")
    print("\033[92m5. Informe Activos con Volumen superior al promedio\033[0m")
    print("\033[92m8. Salir\033[0m")
    print('\033[92m' + '='*50 + '\033[0m')

    opcion = input('\033[93mIngrese el numero de la opcion que desea ejecutar:\033[0m ')

    return opcion

def menu_gestion_catalogo():
    """Muestra el menú de gestion de catalogo y retorna la opción seleccionada por el usuario."""

    print('\033[92m' + '='*50 + '\033[0m')
    print('\033[92m' + ' '*2 + 'SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB' + '\033[0m')
    print('\033[92m' + '='*50 + '\033[0m')
    print("\033[92m1. Registrar nuevo activo (Alta)\033[0m")
    print("\033[92m2. Eliminar activo del sistema (Baja)\033[0m")
    print("\033[92m3. Modificar valoracion o puntaje (Modificacion)\033[0m")
    print("\033[92m4. Informe General - Visualizacion de los datos\033[0m")
    print("\033[92m5. Informe Activos con Volumen superior al promedio\033[0m")
    print("\033[92m8. Salir\033[0m")
    print('\033[92m' + '='*50 + '\033[0m')

    opcion = input('\033[93mIngrese el numero de la opcion que desea ejecutar:\033[0m ')

    return opcion

def menu_principal():
    """Muestra el menú de gestión de catálogo y retorna la opción seleccionada por el usuario."""

    print('\033[92m' + '='*50 + '\033[0m')
    print('\033[92m' + ' '*2 + 'SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB' + '\033[0m')
    print('\033[92m' + '='*50 + '\033[0m')
    print("\033[92m1. Gestión catálogo\033[0m")
    print("\033[92m2. Gestión cartera\033[0m")
    print("\033[92m8. Salir\033[0m")
    print('\033[92m' + '='*50 + '\033[0m')

    opcion = input('\033[93mIngrese el numero de la opcion que desea ejecutar:\033[0m ')

    return opcion


def verificacion_menu_cartera (opcion, matriz, catalogo):
    """Valida la opción elegida por el usuario y ejecuta la operación correspondiente."""

    opciones_validas = ['1', '2', '3', '4', '5', '8']

    while opcion not in opciones_validas:

        print("\033[91mOpción inválida. Intente nuevamente.\033[0m\n")
        opcion = menu_gestion_cartera()

    if int(opcion) == 1:
        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        if nombre.upper() != 'FIN':
            alta_activo(matriz, nombre, catalogo)

    elif int(opcion) == 2:
        ticker = input('\033[93mIngrese el ticker del activo que desea eliminar:\033[0m ').upper()
        while not validar_ticker(ticker) and ticker.upper() != 'FIN':
            ticker = input('\033[93mIngrese el ticker del activo que desea eliminar:\033[0m ').upper()
        
        eliminar_activo(matriz, ticker)

    elif int(opcion) == 3:
        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        if nombre.upper() != 'FIN':
            modificar_activo(matriz, nombre)

    elif int(opcion) == 4:
        mostrar_matriz(matriz)
    
    elif int(opcion) == 5:
        volumen_superior_al_promedio(matriz)

    elif int(opcion) == 8:
        print("Volviendo al menú principal...")

def verificacion_menu_catalogo (opcion, catalogo, matriz):
    """Valida la opcion elegida por el usuario y ejecuta la operación correspondiente."""

    opciones_validas = ['1', '2', '3', '4', '5', '8']

    while opcion not in opciones_validas:

        print("\033[91mOpción inválida. Intente nuevamente.\033[0m\n")
        opcion = menu_gestion_catalogo()

    if int(opcion) == 1:
        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        if nombre.upper() != 'FIN':
            alta_activo_catalogo(catalogo, nombre)

    elif int(opcion) == 2:
        nombre = input('\033[93mIngrese el nombre del activo que desea eliminar:\033[0m ').upper()
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre del activo que desea eliminar:\033[0m ').upper()
        
        eliminar_activo_catalogo(catalogo, nombre, matriz)

    elif int(opcion) == 3:
        nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        while not validar_nombre(nombre) and nombre.upper() != 'FIN':
            nombre = input('\033[93mIngrese el nombre oficial del activo o fin para finalizar:\033[0m ')
        if nombre.upper() != 'FIN':
            modificar_activo_catalogo(catalogo, nombre, matriz)

    elif int(opcion) == 4:
        mostrar_catalogo(catalogo)
    
    elif int(opcion) == 5:
        volumen_superior_al_promedio_catalogo(catalogo)

    elif int(opcion) == 8:
        print("Volviendo al menú principal...")

def verificacion_menu_principal(opcion, catalogo, matriz):
    """Valida la opción del menú principal y deriva al submenú correspondiente.
    
    Parámetros:
        opcion (str): opción ingresada por el usuario.
        catalogo (list): lista de activos del catálogo.
        matriz (list): lista de activos en cartera."""

    opciones_validas = ['1', '2', '8']

    while opcion not in opciones_validas:
        print("\033[91mOpción inválida. Intente nuevamente.\033[0m\n")
        opcion = menu_principal()

    if int(opcion) == 1:
        opcion_catalogo = menu_gestion_catalogo()
        verificacion_menu_catalogo(opcion_catalogo, catalogo, matriz)

    elif int(opcion) == 2:
        opcion_cartera = menu_gestion_cartera()
        verificacion_menu_cartera(opcion_cartera, matriz, catalogo)

    elif int(opcion) == 8:
        print("\033[92mSaliendo del programa...\033[0m")

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