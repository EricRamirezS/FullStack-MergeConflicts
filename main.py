def procesar_nombres(lista_nombres):

    procesados = []

    for nombre in lista_nombres:
        nombre_limpio = nombre.strip()
        if nombre_limpio:
            nombre_formateado = nombre_limpio.capitalize()
            procesados.append(nombre_formateado)

    return procesados


if __name__ == "__main__":
    nombres_sucios = ["  juan", "ALICIA", " ", "  rOberto  ", "", "   ", "cRisToBal ", "AgustinA"]
    resultado = procesar_nombres(nombres_sucios)
    print(f"Procesador de datos \nResultado final: {resultado}")