class Automotora:

    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregarVehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarVehiculos(self):
        print("Automotora:", self.nombre)
        print("Vehículos registrados:")

        for vehiculo in self.vehiculos:
            vehiculo.mostrarInfo()
            print("--------------------")