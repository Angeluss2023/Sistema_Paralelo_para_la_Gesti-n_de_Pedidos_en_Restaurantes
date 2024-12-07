import tkinter as tk
from tkinter import messagebox
from clases.restaurante import Restaurante
from clases.pedido import Pedido

class Interfaz:
    def __init__(self):
        self.restaurante = Restaurante()

    def iniciar(self):
        # Crear la ventana principal
        root = tk.Tk()
        root.title("Gestión de Pedidos - Restaurante")

        # Título
        tk.Label(root, text="Sistema de Gestión de Pedidos", font=("Arial", 16)).pack(pady=10)

        # Entrada de pedido
        tk.Label(root, text="ID del Pedido:").pack()
        self.id_pedido = tk.Entry(root)
        self.id_pedido.pack()

        tk.Label(root, text="Items (ej. hamburguesa:2, papas:1):").pack()
        self.items_pedido = tk.Entry(root)
        self.items_pedido.pack()

        # Botón para agregar pedido
        tk.Button(root, text="Agregar Pedido", command=self.agregar_pedido).pack(pady=5)

        # Botón para procesar pedidos
        tk.Button(root, text="Procesar Pedidos", command=self.procesar_pedidos).pack(pady=5)

        # Botón para consultar inventario
        tk.Button(root, text="Consultar Inventario", command=self.consultar_inventario).pack(pady=5)

        # Ejecutar la ventana
        root.mainloop()

    def agregar_pedido(self):
        try:
            id_pedido = int(self.id_pedido.get())
            items_input = self.items_pedido.get()
            items = {item.split(":")[0]: int(item.split(":")[1]) for item in items_input.split(",")}
            pedido = Pedido(id_pedido, items)
            self.restaurante.gestor_pedidos.recibir_pedido([pedido])
            messagebox.showinfo("Éxito", f"Pedido {id_pedido} agregado.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar el pedido: {e}")

    def procesar_pedidos(self):
        try:
            self.restaurante.simular()
            messagebox.showinfo("Éxito", "Pedidos procesados exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar pedidos: {e}")

    def consultar_inventario(self):
        try:
            inventario = self.restaurante.inventario.consultar_inventario()
            inventario_str = "\n".join([f"{item}: {cantidad}" for item, cantidad in inventario.items()])
            messagebox.showinfo("Inventario", f"Estado actual del inventario:\n{inventario_str}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar el inventario: {e}")
