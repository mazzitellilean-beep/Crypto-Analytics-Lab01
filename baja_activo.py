def eliminar(lista, ticker):

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
