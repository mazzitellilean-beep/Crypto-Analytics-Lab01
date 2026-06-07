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
