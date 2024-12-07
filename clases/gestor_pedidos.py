from multiprocessing import Queue, Barrier
import time

class GestorPedidos:
    def __init__(self, inventario):
        self.cola_pedidos = Queue()
        self.inventario = inventario
        self.barrier = Barrier(2)  # Sincroniza dos procesos

    def recibir_pedido(self, pedidos):
        for pedido in pedidos:
            self.cola_pedidos.put(pedido)
            print(f"Pedido {pedido.id_pedido} recibido.")

    def procesar_pedido(self):
        while not self.cola_pedidos.empty():
            pedido = self.cola_pedidos.get()
            print(f"Procesando pedido {pedido.id_pedido}...")
            pedido.estado = 'en preparación'
            time.sleep(1)
            
            self.barrier.wait()
            
            if self.inventario.actualizar_inventario(pedido.items):
                pedido.estado = 'completado'
                print(f"Pedido {pedido.id_pedido} completado.")
            else:
                pedido.estado = 'no procesado'
                print(f"Pedido {pedido.id_pedido} no procesado por falta de inventario.")
