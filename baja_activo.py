def eliminar(lista, ticker):

    while ticker != 'fin':
        for i in lista: 

            if lista[i][1].upper() == ticker.upper() and lista[i][5] == 0:
                lista.remove(lista[i])
            elif lista[i][1].upper() != ticker.upper():
                print('El ticker ingresado no coincide con ningún activo en la tabla. Intente nuevamente')
        
        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ')

    return lista
