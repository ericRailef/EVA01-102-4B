from vehiculo import Vehiculo


class Auto(Vehiculo):

    def __init__(self, patente, marca, modelo, año, precio,
        numPuertas, combustible):

        super().__init__(patente, marca, modelo, año, precio)

        self.numPuertas = numPuertas
        self.combustible = combustible

    def abrirMaletero(self):
        print("El maletero está abierto.")

    def tieneAireAcondicionado(self):
        return True