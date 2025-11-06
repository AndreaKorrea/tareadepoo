class Animal:
    def __init__(self, codigo, raza, edad):
        self.codigo = codigo
        self.raza = raza
        self.edad = edad
        self.produccion = []

    def registrar_produccion(self, semana, huevos):
        for i, (sem, _) in enumerate(self.produccion):
            if sem == semana:
                self.produccion[i] = (semana, huevos)
                return
        self.produccion.append((semana, huevos))

    def produccion_total(self):
        return sum(huevos for _, huevos in self.produccion)

    def __str__(self):
        return f"Código: {self.codigo}, Raza: {self.raza}, Edad: {self.edad}, Producción total: {self.produccion_total()} huevos"
