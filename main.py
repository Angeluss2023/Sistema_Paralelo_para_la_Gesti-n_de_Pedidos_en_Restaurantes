from clases.restaurante import Restaurante
from interfaz.interfaz import Interfaz
if __name__ == "__main__":
    app = Interfaz()
    app.iniciar()
    restaurante = Restaurante()
    restaurante.simular()
