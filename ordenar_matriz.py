def ordenar_matriz(lista):

    for i in range(len(lista)-1):
        indice_max = i

        for j in range(i+1, len(lista)):
            if lista[j][6] > lista[indice_max][6]:
                indice_max = j
            
        lista[i], lista[indice_max] = lista[indice_max], lista[i]

    return lista
