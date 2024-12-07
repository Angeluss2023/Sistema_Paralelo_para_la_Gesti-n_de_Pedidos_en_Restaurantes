class Pedido:
    def __init__(self, id_pedido, items):
        self.id_pedido = id_pedido
        self.items = items
        self.estado = 'pendiente'
