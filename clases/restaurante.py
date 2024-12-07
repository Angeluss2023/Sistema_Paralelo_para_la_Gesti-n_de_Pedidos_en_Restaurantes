from multiprocessing import Process
from clases.pedido import Pedido
from clases.gestor_pedidos import GestorPedidos
from clases.inventario import Inventario

class Restaurante:
    def __init__(self):
        self.inventario = Inventario()
        self.gestor_pedidos = GestorPedidos(self.inventario)

    def simular(self):
        pedidos = [
            Pedido(1, {'hamburguesa': 2, 'papas': 1}),
            Pedido(2, {'hamburguesa': 1, 'bebida': 2}),
            Pedido(3, {'hamburguesa': 3, 'papas': 5, 'bebida': 1}),
        ]

        proceso_recepcion = Process(target=self.gestor_pedidos.recibir_pedido, args=(pedidos,))
        proceso_preparacion = Process(target=self.gestor_pedidos.procesar_pedido)

        proceso_recepcion.start()
        proceso_preparacion.start()

        proceso_recepcion.join()
        proceso_preparacion.join()

        self.generar_reporte()

    def generar_reporte(self):
        print("\nReporte final:")
        print("Inventario final:", self.inventario.consultar_inventario())
