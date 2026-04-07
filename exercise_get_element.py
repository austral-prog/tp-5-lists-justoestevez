# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    # Verificamos si el índice está en el rango permitido (positivo o negativo)
    if indice < len(lista) and indice >= -len(lista):
        return lista[indice]
    
    # Si no está en rango, devolvemos None
    return None
