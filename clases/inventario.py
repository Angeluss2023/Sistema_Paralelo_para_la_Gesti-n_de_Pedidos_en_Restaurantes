from multiprocessing import Lock

class Inventario:
    def __init__(self):
        self.stock = {
            'hamburguesa': 10,
            'papas': 20,
            'bebida': 15
        }
        self.lock = Lock()

    def actualizar_inventario(self, items):
        with self.lock:
            for item, cantidad in items.items():
                if self.stock.get(item, 0) < cantidad:
                    return False
            for item, cantidad in items.items():
                self.stock[item] -= cantidad
            return True

    def consultar_inventario(self):
        return self.stock
