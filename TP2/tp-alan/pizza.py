# pizza.py
class Pizza:
    def __init__(self, var: str):
        self.variedad = var

    def establecerVariedad(self, var: str):
        self.variedad = var

    def obtenerVariedad(self) -> str:
        return self.variedad
