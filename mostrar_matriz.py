def mostrar_matriz (lista): 

    print('Nombre del activo | Ticker | Valor de referencia | Volumen de actividad | Metodología de operación | Unidades totales en tesorería | Puntaje de confianza')

    for i in lista:
        print(i[0], '|', i[1], '|', i[2], '|', i[3], '|', i[4], '|', i[5], '|', i[6])
