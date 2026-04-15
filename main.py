def procesar_nombres(lista_nombres):
    """
    Recibe una lista de nombres y debe devolver una lista 
    con los nombres limpios (sin espacios extra) y en formato correcto.
    """
    procesados = []

    for nombre in lista_nombres:
        # TODO: Implementar la lógica de limpieza y formato
        # 1. Eliminar espacios en blanco al inicio y final
        nombres_limpios = nombre.strip()
        # 2. Poner la primera letra en mayúscula
        pr_letra_may= nombres_limpios.capitalize()
        # 3. Solo agregar a la lista si el nombre no está vacío
        if nombres_limpios:
            procesados.append(pr_letra_may)
        pass

    return procesados


if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Resultado final: {resultado}")