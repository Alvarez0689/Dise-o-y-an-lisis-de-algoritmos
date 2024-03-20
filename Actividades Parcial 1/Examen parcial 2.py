def crear_matriz_cuadrada(n):
    matriz = [[0] * n for _ in range(n)]
    valor = 1
    tope = n * n
    min_fila = 0
    max_fila = n-1
    min_col = 0
    max_col = n-1

    while valor <= tope:
        for col in range(min_col, max_col + 1):
            matriz[min_fila][col] = valor
            valor += 1
        min_fila += 1

        for fila in range(min_fila, max_fila + 1):
            matriz[fila][max_col] = valor
            valor += 1
        max_col -= 1

        for col in range(max_col, min_col - 1, -1):
            matriz[max_fila][col] = valor
            valor += 1
        max_fila -= 1

        for fila in range(max_fila, min_fila - 1, -1):
            matriz[fila][min_col] = valor
            valor += 1
        min_col += 1

    return matriz

try:
    x = int(input("Ingrese un número positivo para el tamaño de la matriz: "))
    if x <= 0:
        raise ValueError("Debe ingresar un número positivo.")
    else:
        matriz_resultante = crear_matriz_cuadrada(x)
        for fila in matriz_resultante:
            print(" ".join(map(str, fila)))
except ValueError as ve:
    print(ve)
