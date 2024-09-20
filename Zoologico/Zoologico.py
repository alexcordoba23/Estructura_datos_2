class Animal:
    def __init__(nombre, edad, tipo):
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f'Animal: Edad: {self.edad}, Tipo: {self.tipo}'

class Nodo:
    def __init__(self, animal=None):
        self.animal = animal
        self.siguiente = None

class ListaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, nuevo_animal):
        if self.cabeza is None:
            self.cabeza = Nodo(nuevo_animal)
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.animal.nombre == nuevo_animal.nombre:  # Evitar duplicados
                    print("Este animal ya está en la lista.")
                    return
                actual = actual.siguiente
            if actual.animal.nombre != nuevo_animal.nombre:  # Verificar último nodo
                actual.siguiente = Nodo(nuevo_animal)
            else:
                print("Este animal ya está en la lista.")

    def mostrar_animales_iterativo(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.animal)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo):
        if nodo is None:
            return
        print(nodo.animal)
        self.mostrar_animales_recursivo(nodo.siguiente)


