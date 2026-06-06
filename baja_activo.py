def eliminar(lista, ticker):

    while ticker != 'fin':
        for i in lista: 

            if i[1].upper() == ticker.upper() and i[5] == 0:
                lista.remove(i)
            elif i[1].upper() != ticker.upper():
                print('El ticker ingresado no coincide con ningún activo en la tabla. Intente nuevamente')
        
        ticker = input('Ingrese el ticker del activo que desea eliminar o fin para finalizar: ')

    return lista
