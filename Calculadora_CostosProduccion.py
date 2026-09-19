def crear_matriz_vacia(filas, columnas):
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def solicitar_matriz(nombre, filas, columnas, descripciones_filas):
    print(f"\nConfiguracion de la {nombre} ({filas}x{columnas}) ---")
    matriz = crear_matriz_vacia(filas, columnas)
    for i in range(filas):
        print(f"\nIngrese los datos para: {descripciones_filas[i]}")
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"  Columna/Dato {j+1}: "))
                    matriz[i][j] = valor
                    break
                except ValueError:
                    print("Ingrese un número válido.")
    return matriz

def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    
    C = crear_matriz_vacia(filas_A, columnas_B)
    
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma
    return C

def mostrar_matriz(matriz, titulo, nombres_filas, nombres_columnas):
    print(f"\n{titulo}")
    encabezado = f"{'':<20}" + "".join([f"{col:<15}" for col in nombres_columnas])
    print(encabezado)
    print("-" * len(encabezado))
    
    for i in range(len(matriz)):
        fila_texto = f"{nombres_filas[i]:<20}"
        for j in range(len(matriz[i])):
            fila_texto += f"{matriz[i][j]:<15.2f}"
        print(fila_texto)

def ejecutar_calculadora():
    print("Calculadora de producto de matrices (3x3 minimo)")
    print("Caso de Aplicación: Costos de Insumos vs Proveedores")
    
    productos = ["1. Telefonos", "2. Tablets", "3. Laptops"]
    componentes = ["1. Chips", "2. Pantallas", "3. Baterias"]
    proveedores = ["Samsung", "IBM", "TSMC"]
    
    print("\nMATRIZ A: Cantidad de componentes requeridos por cada producto.")
    A = solicitar_matriz("MATRIZ A (Productos x Componentes)", 3, 3, productos)
    
    print("\nMATRIZ B: Costo de cada componente con cada proveedor.")
    B = solicitar_matriz("MATRIZ B (Componentes x Proveedores)", 3, 3, componentes)
    
    C = multiplicar_matrices(A, B)
    
    mostrar_matriz(A, "MATRIZ A: REQUERIMIENTOS DE COMPONENTES", productos, componentes)
    mostrar_matriz(B, "MATRIZ B: COSTOS POR PROVEEDOR ($)", componentes, proveedores)
    mostrar_matriz(C, "MATRIZ C RESULTANTE: COSTO TOTAL POR PRODUCTO ($)", productos, proveedores)

if __name__ == "__main__":
    ejecutar_calculadora()