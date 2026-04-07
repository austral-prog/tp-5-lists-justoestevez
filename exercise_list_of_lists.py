# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    sub_1 = lista[0][:2]    
    sub_2 = lista[1][1:4]    
    sub_3 = lista[2][-2:]    
    

    resultado = [sub_1, sub_2, sub_3]
    
    return resultado
