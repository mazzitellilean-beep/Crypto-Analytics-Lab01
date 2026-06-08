def carga_matriz(lista):


    nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ').upper()

    while nombre.lower() != 'fin':

        datos_validos = True

        ticker = input('Ingrese el ticker del activo: ').upper()
        valor_ref = float(input('Ingres el valor de referencia base (Ej: USD) del activo: '))
        vol_act = float(input('Ingrese el volumen de actividad de las ultimas 24hs: '))
        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL']
        met_op = int(input(f'Ingrese la metodologia de operacion asignada {metodos_validos}: '))
        unidades = float(input('Ingrese las unidades totales en tesoreria: '))
        punt_conf = int(input('Ingrese el puntaje de confianza del 1 al 10: '))

        if met_op < 1 or met_op > 4:
            datos_validos = False
            print('La metodología de operación debe ser un número entre 1 y 4. Intente nuevamente.')
            break

        #La variable activo podria eliminarse y directamente agregar los datos a la tabla, pero queda ordenado 
        activo = [
            nombre,
            ticker,
            valor_ref,
            vol_act,
            metodos_validos[met_op - 1],
            unidades,
            punt_conf
       ]

        if nombre == '':
            datos_validos = False
            print('El nombre del activo no puede estar vacío. Intente nuevamente.')
        if len(ticker) < 3 or ticker == '':
            datos_validos = False
            print('El ticker debe tener al menos 3 caracteres y no puede estar vacío. Intente nuevamente.')
        if valor_ref <= 0 or valor_ref == '':
            datos_validos = False
            print('El valor de referencia debe ser un número positivo y no puede estar vacío. Intente nuevamente.')
        if vol_act < 0 or vol_act == '':
            datos_validos = False
            print('El volumen de actividad no puede ser negativo y no puede estar vacío. Intente nuevamente.')
        if unidades < 0 or unidades == '':
            datos_validos = False
            print('Las unidades totales en tesorería no pueden ser negativas y no pueden estar vacías. Intente nuevamente.')
        if punt_conf < 1 or punt_conf > 10 or punt_conf == '':
            datos_validos = False
            print('El puntaje de confianza debe ser un número entre 1 y 10 y no puede estar vacío. Intente nuevamente.')

        if datos_validos:
            lista.append(activo)
            print('Datos del activo agregados correctamente.')
        else: 
            print('Datos inválidos. Intente nuevamente.')

        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
    
    return lista
