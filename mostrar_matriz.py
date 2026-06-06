def mostrar_matriz (lista):

    print('Nombre del activo | Ticker | Valor de referencia | Volumen de actividad | Metodología de operación | Unidades totales en tesorería | Puntaje de confianza')

    for i in lista:
        print(f'{lista[i][0]} | {lista[i][1]} | {lista[i][2]} | {lista[i][3]} | {lista[i][4]} | {lista[i][5]} | {lista[i][6]}')