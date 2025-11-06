from animal import Animal

class BaseDatos:
    def __init__(self):
        self.animales = []

    def crear_animal(self, codigo, raza, edad):
        if self.buscar_animal(codigo):
            print("Ya existe un animal con ese código.")
            return
        nuevo = Animal(codigo, raza, edad)
        self.animales.append(nuevo)
        print("Animal agregado correctamente.")

    def leer_animales(self):
        if not self.animales:
            print("No hay animales registrados.")
            return
        for a in self.animales:
            print(a)

    def buscar_animal(self, codigo):
        for a in self.animales:
            if a.codigo == codigo:
                return a
        return None

    def actualizar_animal(self, codigo, nueva_raza=None, nueva_edad=None):
        animal = self.buscar_animal(codigo)
        if not animal:
            print("Animal no encontrado.")
            return
        if nueva_raza:
            animal.raza = nueva_raza
        if nueva_edad:
            animal.edad = nueva_edad
        print("Datos actualizados correctamente.")

    def eliminar_animal(self, codigo):
        animal = self.buscar_animal(codigo)
        if animal:
            self.animales.remove(animal)
            print("Animal eliminado.")
        else:
            print("Animal no encontrado.")

    def registrar_produccion(self, codigo, semana, huevos):
        animal = self.buscar_animal(codigo)
        if not animal:
            print("No existe un animal con ese código.")
            return
        animal.registrar_produccion(semana, huevos)
        print("Producción registrada correctamente.")

    def consultar_produccion(self, codigo):
        animal = self.buscar_animal(codigo)
        if not animal:
            print("Animal no encontrado.")
            return
        print(f"\nProducción del animal {animal.codigo}:")
        for semana, huevos in animal.produccion:
            print(f"  Semana {semana}: {huevos} huevos")
        print(f"Total: {animal.produccion_total()} huevos\n")
