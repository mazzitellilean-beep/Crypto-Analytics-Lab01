# ============================================
# CRYPTO-ANALYTICS LAB - Fase 1
# Gestion de Activos Digitales
 
# --- VECTORES INICIALES ---
nombres      = ["Bitcoin", "Ethereum", "Solana"]
tickers      = ["BTC",     "ETH",      "SOL"]
valores      = [105000.0,  3200.0,     150.0]
volumenes    = [1200000.0, 850000.0,   300000.0]
metodologias = ["HODL",    "Swing Trading", "Day Trading"]
unidades     = [2.5,       15.0,       300.0]
puntajes     = [10,        9,          3]
 
# ============================================
# FUNCIONES
 
def mostrar_menu():
    print("\n" + "=" * 44)
    print("   SISTEMA DE GESTION: CRYPTO-ANALYTICS LAB")
    print("=" * 44)
    print("1. Registrar nuevo activo (Alta)")
    print("2. Eliminar activo del sistema (Baja)")
    print("3. Modificar valoracion o puntaje (Modificacion)")
    print("4. Informe General - Visualizacion de los datos")
    print("8. Salir")
    print("=" * 44)
 
# -----------------------------------------------
def buscar_por_ticker(ticker_buscar):  
    indice = -1
    for i in range(len(tickers)):
        if tickers[i] == ticker_buscar:
            indice = i
            break
    return indice
 
# -----------------------------------------------
def buscar_por_nombre(nombre_buscar): 
    indice = -1
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre_buscar.lower():
            indice = i
            break
    return indice
 
# -----------------------------------------------
def validar_metodologia(metodo):
    # Devuelve true si es valido y si no devuelve False
    opciones = ["Scalping", "Day Trading", "Swing Trading", "HODL"]
    return metodo in opciones
 
# -----------------------------------------------
def alta_activo():
    print("\n--- REGISTRAR NUEVO ACTIVO ---")
 
    # Nombre si o si
    nombre = input("Nombre del activo: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return
    #tickerrr
    ticker=input("ticker(3-5 letras):").strip().upper()
    if not(3<= len (ticker)<=5)or not ticker.isalpha():
        print("Error: el ticker debe tener entre 3 y 5 letras")
        return
    #valores num 
    try:
        valor=float(input("valor actual (USD):"))
        volumen=float(input("volumen de actividade 24hs:"))
        unidad=float(input("unidades poseidas:"))
        puntaje=int(input("puntaje de riesgo (1-10):"))
    except ValueError:
        print("Error: valores invalidos.")
        return
    #PUNTAJEEEEE
    if not (1<=puntaje<=10):
        print("error: el puntaje debe ser entre 1 y 10")
        return
    #metodologia
    print("Metodologias validas: Scalping / Day Trading / Swing Trading / HODL")
    metodo = input("Metodologia: ").strip()
    if not validar_metodologia(metodo):
        print("Error: metodologia no valida.")
        return
    #agregados a los vectores 
    nombres.append(nombre)
    tickers.append(ticker)
    valores.append(valor)
    volumenes.append(volumen)
    metodologias.append(metodo)
    unidades.append(unidad)
    puntajes.append(puntaje)
    print(f"Activo {nombre} registrado exitosamente.")
    #============================================
def baja_activo():
    print("\n--- ELIMINAR ACTIVO ---")
 
    ticker_buscar = input("Ticker del activo a eliminar: ").strip().upper()
    indice = buscar_por_ticker(ticker_buscar)
 
    if indice == -1:
        print("Error: no se encontro ese ticker.")
        return
    # Elimina el indice en los 7 vectoeres
    nombres.pop(indice)
    tickers.pop(indice)
    valores.pop(indice)
    volumenes.pop(indice)
    metodologias.pop(indice)
    unidades.pop(indice)
    puntajes.pop(indice)
 
    print(f"Activo '{ticker_buscar}' eliminado correctamente.")
 
# -----------------------------------------------
def modificar_activo():
    print("\n--- MODIFICAR ACTIVO ---")
 
    nombre_buscar = input("Nombre del activo a modificar: ").strip()
 
    # Funcion bn
    indice = buscar_por_nombre(nombre_buscar)
 
    if indice == 1:
        print("Error: activo no encontrado.")
        return
 
    print(f"\nActivo encontrado: {nombres[indice]} ({tickers[indice]})")
    print("Que deseas modificar?")
    print("1. Valor de referencia")
    print("2. Puntaje de confianza")
    print("3. Unidades en tesoreria")
    print("4. Metodologia de operacion")
 
    opcion = input("Opcion: ").strip()
 
    if opcion == "1":
        try:
            valores[indice] = float(input("Nuevo valor en USD: "))
            print("Valor actualizado.")
        except ValueError:
            print("Error: valor no valido.")
 
    elif opcion == "2":
        try:
            nuevo = int(input("Nuevo puntaje (1-10): "))
            if 1 <= nuevo <= 10:
                puntajes[indice] = nuevo
                print("Puntaje actualizado.")
            else:
                print("Error: debe ser entre 1 y 10.")
        except ValueError:
            print("Error: ingresa un numero entero.")
 
    elif opcion == "3":
        try:
            nuevo = float(input("Nuevas unidades (>= 0): "))
            if nuevo >= 0:
                unidades[indice] = nuevo
                print("Unidades actualizadas.")
            else:
                print("Error: no puede ser negativo.")
        except ValueError:
            print("Error: valor no valido.")
 
    elif opcion == "4":
        print("Opciones: Scalping / Day Trading / Swing Trading / HODL")
        nuevo = input("Nueva metodologia: ").strip()
        if validar_metodologia(nuevo):
            metodologias[indice] = nuevo
            print("Metodologia actualizada.")
        else:
            print("Error: metodologia no valida.")
 
    else:
        print("Opcion no reconocida.")
    #============================================
def ordenar_indices():
    indices= list(range(len(nombres)))
    for j in range(len(indices)-1-1):
       puntaje_actual=puntajes[indices[j]]
    puntaje_siguiente = puntajes[indices[j + 1]]
    nombre_actual    = nombres[indices[j]]
    nombre_siguiente = nombres[indices[j + 1]]
    if puntaje_actual<puntaje_siguiente:
     indices[j], indices[j+1]=indices[j+1], indices[j]
    elif puntaje_actual == puntaje_siguiente:
                if nombre_actual > nombre_siguiente:
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]
    return indices
# -----------------------------------------------
def informe_general():
    print("\n--- INFORME GENERAL ---")
 
    if len(nombres) == 0:
        print("No hay activos registrados.")
        return
 
    # Obtenemos los indices ordenados con Bubble Sort
    indices = ordenar_indices()
 
    # Encabezado con f-string
    print(f"\n{'Activo':<20} {'Ticker':<8} {'Valor USD':>12} {'Metodologia':<16} {'Unidades':>10} {'Puntaje':>8}")
    print("-" * 76)
 
    for idx in indices:
        print(f"{nombres[idx]:<20} {tickers[idx]:<8} {valores[idx]:>12,.2f} {metodologias[idx]:<16} {unidades[idx]:>10.2f} {puntajes[idx]:>8}")
 
    print("-" * 76)
    print(f"Total de activos registrados: {len(nombres)}")

# ============================================
#  PROGRAMA PRINCIPAL
# ============================================
while True:
    mostrar_menu()
    opcion= input("selecciona una opcion (1-4, 8 para salir):").strip()
    if opcion=="1":
        alta_activo()
    elif opcion=="2":
        baja_activo()
    elif opcion=="3":
        modificar_activo()
    elif opcion=="4":
        informe_general()
    elif opcion=="8":
        print("Saliendo del sistema. ¡Hasta pronto!")
        break
    else:
        print("Opcion no invalida, intenta de nuevo.")