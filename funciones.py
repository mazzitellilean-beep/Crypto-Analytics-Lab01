
#=======================================================
#                FUNCIONES PRINCIPALES
#=======================================================

def eliminar(lista, ticker):

    '''Elimina activos'''

    while ticker != 'fin':
        ticker_no_encontrado = False
        for i in lista: 

            if i[1].upper() == ticker.upper() and i[5] == 0:
                lista.remove(i)
                ticker_no_encontrado = False
                print('El activo fue correctamente eliminado')  
                break
            elif i[1].upper() != ticker.upper() or i[5] > 0:
                ticker_no_encontrado = True

        if ticker_no_encontrado:
            print('Ticker no encontrado o el activo tiene unidades en tesorería. Intente nuevamente.')      
        
        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ')

    return lista
    
def carga_activo(lista):

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

        #La variable activo podria eliminarse y directamente agregar los datos a la tabla, pero queda ordenado 
        activo = [nombre,ticker,valor_ref,vol_act,metodos_validos[met_op - 1],unidades,punt_conf]

        if validacion(nombre, ticker, valor_ref, vol_act, met_op, unidades, punt_conf):
            lista.append(activo)
            print('Datos del activo agregados correctamente.')
        
        nombre = input('Ingrese el nombre oficial del activo o fin para finalizar: ')
    
    return lista



def modificar(lista):

    activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")

    while activo_a_cambiar.lower() != 'fin':
        
        activo_encontrado = False

        for i in lista:
            if i[0].upper() == activo_a_cambiar.upper():
                activo_encontrado = True
                print(f"Activo encontrado: {i}")
                menu_modificar()

                opcion_modificar = int(input("Ingrese el número de la opción que desea modificar: "))

                if opcion_modificar < 1 or opcion_modificar > 8:
                    print("Opción no válida. Intente nuevamente.")
                    continue

                while opcion_modificar != 8:
                    if opcion_modificar == 1:
                        nuevo_nombre = input("Ingrese el nuevo nombre del activo: ")
                        i[0] = nuevo_nombre
                    elif opcion_modificar == 2:
                        nuevo_ticker = input("Ingrese el nuevo ticker del activo: ")
                        i[1] = nuevo_ticker
                    elif opcion_modificar == 3:
                        nuevo_valor_ref = float(input("Ingrese el nuevo valor de referencia del activo: "))
                        i[2] = nuevo_valor_ref
                    elif opcion_modificar == 4:
                        nuevo_vol_act = float(input("Ingrese el nuevo volumen de actividad del activo: "))
                        i[3] = nuevo_vol_act
                    elif opcion_modificar == 5:
                        metodos_validos = ['Scalping', 'Day Trading', 'Swing Trading', 'HODL'] 
                        print('1: Scalping', '2: Day Trading', '3: Swing Trading', '4: HODL')
                        nueva_met_op = int(input(f'Ingrese el numero de la nueva metodología de operación asignada: '))
                        i[4] = metodos_validos[nueva_met_op - 1]
                    elif opcion_modificar == 6:
                        nuevas_unidades = float(input("Ingrese las nuevas unidades en tesorería del activo: "))
                        i[5] = nuevas_unidades
                    elif opcion_modificar == 7:
                        nuevo_punt_conf = int(input("Ingrese el nuevo puntaje de confianza del activo (1-10): "))
                        i[6] = nuevo_punt_conf
                    elif opcion_modificar == 8:
                        print("Saliendo del menú de modificación.")

                    validacion(i[0], i[1], i[2], i[3], nueva_met_op, i[5], i[6])
                    if opcion_modificar != 8:
                       menu_modificar()
                       opcion_modificar = int(input("Ingrese el número de la opción que desea modificar o 8 para salir: "))
        
        if not activo_encontrado:
            print("Activo no encontrado. Intente nuevamente.")

        activo_a_cambiar = input("Ingrese el nombre del activo que desea modificar o fin para finalizar: ")
    
    return lista

def mostrar_matriz (lista):

    lista = ordenar_matriz(lista)

    print("\n" + "=" * 105)
    print(f"{'NOMBRE':<25} {'TICKER':<8} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'UNIDADES':>10} {'PUNTAJE':>8}")
    print("=" * 105)
    for activo in lista:
        print(f"{activo[0]:<25} {activo[1]:<8} {activo[2]:>12.2f} {activo[3]:>18,} {activo[4]:>15} {activo[5]:>10,} {activo[6]:>8}")
    print("=" * 105)
    salida = input("\nPresione Enter para volver al menú principal...")

#=======================================================
#                FUNCIONES SECUNDARIAS
#=======================================================

def validacion(nombre, ticker, valor_ref, vol_act, met_op, unidades, punt_conf):
    datos_validos = True
    if nombre == '':
        print('El nombre del activo no puede estar vacío. Intente nuevamente.')
        datos_validos = False
    if len(ticker) < 3 or len(ticker) > 5 or ticker == '':
        print('El ticker debe tener entre 3 y 5 caracteres y no puede estar vacío. Intente nuevamente.')
        datos_validos = False
    if valor_ref <= 0 or valor_ref == '':
        print('El valor de referencia debe ser un número positivo y no puede estar vacío. Intente nuevamente.')
        datos_validos = False
    if vol_act < 0 or vol_act == '':
        print('El volumen de actividad no puede ser negativo y no puede estar vacío. Intente nuevamente.')
        datos_validos = False
    if met_op < 1 or met_op > 4 and met_op == '':
        print('La metodología de operación debe ser un número entre 1 y 4. Intente nuevamente.')
        datos_validos = False

    if unidades < 0 or unidades == '':
        print('Las unidades totales en tesorería no pueden ser negativas y no pueden estar vacías. Intente nuevamente.')
        datos_validos = False

    if punt_conf < 1 or punt_conf > 10 or punt_conf == '':
        print('El puntaje de confianza debe ser un número entre 1 y 10 y no puede estar vacío. Intente nuevamente.')
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

def ordenar_matriz(lista):

    for i in range(len(lista)-1):
        indice_max = i

        for j in range(i+1, len(lista)):
            if lista[j][6] > lista[indice_max][6]:
                indice_max = j
            elif lista[j][6] == lista[indice_max][6]:
                nombre_activo = lista[j][0].upper()
                nombre_activo_max = lista[indice_max][0].upper()
                if nombre_activo < nombre_activo_max:
                    indice_max = j
            
        lista[i], lista[indice_max] = lista[indice_max], lista[i]

    return lista

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

    opcion = int(input('Ingrese el numero de la opcion que desea ejecutar: '))

    return opcion

def verificacion_menu (opcion, lista):
    
    if opcion == 1:
        
        lista = carga_activo(lista)
    elif opcion == 2:
        
        ticker = input('Ingrese el ticker del activo que desea eliminar: ').upper()
        lista = eliminar(lista, ticker)
    elif opcion == 3: 
        
        lista = modificar(lista)
    elif opcion == 4:
        
        mostrar_matriz(lista)
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")
    
    return lista