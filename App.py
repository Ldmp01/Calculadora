import tkinter as tk
from tkinter import messagebox, ttk

def crear_matriz_vacia(filas, columnas):
    return [[0.0 for _ in range(columnas)] for _ in range(filas)]

def multiplicar_matrices(A, B):
    filas_A, columnas_A = len(A), len(A[0])
    columnas_B = len(B[0])
    C = crear_matriz_vacia(filas_A, columnas_B)
    for i in range(filas_A):
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            C[i][j] = suma
    return C

class CalculadoraMatricesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Matrices - Costos de Insumos vs Proveedores")
        self.root.geometry("850x700")
        self.root.configure(bg="#f4f6f9")

        self.productos = ["1. Telefonos", "2. Tablets", "3. Laptops"]
        self.componentes = ["1. Chips", "2. Pantallas", "3. Baterias"]
        self.proveedores = ["Samsung", "IBM", "TSMC"]

        titulo = tk.Label(root, text="Caso de Aplicación: Insumos vs Proveedores", font=("Arial", 16, "bold"), bg="#f4f6f9", fg="#2c3e50")
        titulo.pack(pady=15)

        frame_matrices = tk.Frame(root, bg="#f4f6f9")
        frame_matrices.pack(pady=10, padx=20, fill="x")

        self.frame_A = tk.LabelFrame(frame_matrices, text=" MATRIZ A: Componentes por Producto ", font=("Arial", 11, "bold"), fg="#2980b9", bg="white", padx=10, pady=10)
        self.frame_A.grid(row=0, column=0, padx=15, sticky="nsew")
        self.inputs_A = self.crear_interfaz_matriz(self.frame_A, self.productos, self.componentes)

        self.frame_B = tk.LabelFrame(frame_matrices, text=" MATRIZ B: Costos por Proveedor ($) ", font=("Arial", 11, "bold"), fg="#27ae60", bg="white", padx=10, pady=10)
        self.frame_B.grid(row=0, column=1, padx=15, sticky="nsew")
        self.inputs_B = self.crear_interfaz_matriz(self.frame_B, self.componentes, self.proveedores)

        frame_matrices.columnconfigure(0, weight=1)
        frame_matrices.columnconfigure(1, weight=1)

        btn_calcular = tk.Button(root, text="Calcular Multiplicación", font=("Arial", 12, "bold"), bg="#34495e", fg="white", activebackground="#2c3e50", activeforeground="white", bd=0, padx=20, pady=10, command=self.procesar_calculo)
        btn_calcular.pack(pady=20)

        self.frame_C = tk.LabelFrame(root, text=" MATRIZ C RESULTANTE: Costo Total por Producto ($) ", font=("Arial", 11, "bold"), fg="#8e44ad", bg="white", padx=15, pady=10)
        self.frame_C.pack(pady=10, padx=35, fill="both", expand=True)

        self.tabla_resultado = ttk.Treeview(self.frame_C, columns=["Producto"] + self.proveedores, show="headings")
        self.tabla_resultado.heading("Producto", text="Producto / Item")
        self.tabla_resultado.column("Producto", width=150, anchor="center")
        
        for prov in self.proveedores:
            self.tabla_resultado.heading(prov, text=prov)
            self.tabla_resultado.column(prov, width=120, anchor="center")
            
        self.tabla_resultado.pack(fill="both", expand=True)

    def crear_interfaz_matriz(self, frame, filas_nombres, columnas_nombres):
        for col_idx, col_name in enumerate(columnas_nombres):
            lbl = tk.Label(frame, text=col_name.split(". ")[-1], font=("Arial", 9, "bold"), bg="white", fg="#7f8c8d")
            lbl.grid(row=0, column=col_idx + 1, padx=5, pady=5)

        entradas = []
        for row_idx, row_name in enumerate(filas_nombres):
            # Nombre de la fila
            lbl_fila = tk.Label(frame, text=row_name.split(". ")[-1], font=("Arial", 9, "bold"), bg="white", anchor="w")
            lbl_fila.grid(row=row_idx + 1, column=0, padx=5, pady=5, sticky="w")
            
            fila_entradas = []
            for col_idx in range(len(columnas_nombres)):
                entry = tk.Entry(frame, width=10, font=("Arial", 10), justify="center", bd=1, relief="solid")
                entry.insert(0, "0.0")  # Valor por defecto
                entry.grid(row=row_idx + 1, column=col_idx + 1, padx=5, pady=5)
                fila_entradas.append(entry)
            entradas.append(fila_entradas)
        return entradas

    def obtener_valores_matriz(self, entradas):
        matriz = crear_matriz_vacia(len(entradas), len(entradas[0]))
        for i in range(len(entradas)):
            for j in range(len(entradas[i])):
                val_str = entradas[i][j].get().strip()
                try:
                    matriz[i][j] = float(val_str)
                except ValueError:
                    raise ValueError(f"Dato inválido detectado. Asegúrate de ingresar solo números.")
        return matriz

    def procesar_calculo(self):
        try:
            A = self.obtener_valores_matriz(self.inputs_A)
            B = self.obtener_valores_matriz(self.inputs_B)
            
            C = multiplicar_matrices(A, B)
            
            for item in self.tabla_resultado.get_children():
                self.tabla_resultado.delete(item)
                
            for i, prod in enumerate(self.productos):
                valores_fila = [f"$ {C[i][j]:.2f}" for j in range(len(self.proveedores))]
                self.tabla_resultado.insert("", "end", values=[prod.split(". ")[-1]] + valores_fila)
                
        except ValueError as e:
            messagebox.showerror("Error de entrada", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraMatricesApp(root)
    root.mainloop()