def seleccion(lista):

    for i in range(len(lista)-1):
        indice_min = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_min]:
                indice_min = j
            
        lista[i], lista[indice_min] = lista[indice_min], lista[i]

def burbujeo(lista):

    for i in range(len(lista)-1):

        for j in range(len(lista)-1 - i):

            if lista[j] > lista[j+1]:

                lista[j], lista[j+1] = lista[j+1], lista[j]

def insercion(lista):

    for i in range(1, len(lista)):

        valor_insertar = lista[i]

        j = i

        while j > 0 and lista[j-1] > valor_insertar:

            lista[j] = lista[j-1]

            j -= 1
        
        lista[j] = valor_insertar

        


