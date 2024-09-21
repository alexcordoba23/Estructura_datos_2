class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento

    def __str__(self):
        return f'{self.descripcion} - Prioridad: {self.prioridad}, Vence: {self.fecha_vencimiento}'

class NodoTarea:
    def __init__(self, tarea=None):
        self.tarea = tarea
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, nueva_tarea):
        nuevo_nodo = NodoTarea(nueva_tarea)
        if self.cabeza is None or self.cabeza.tarea.prioridad > nueva_tarea.prioridad:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.tarea.prioridad <= nueva_tarea.prioridad:
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_tarea(self, descripcion):
        actual = self.cabeza
        anterior = None
        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente

    def mostrar_tareas(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.tarea)
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.cabeza
        while actual is not None:
            if actual.tarea.descripcion == descripcion:
                print(actual.tarea)
                return
            actual = actual.siguiente
        print("Tarea no encontrada")

    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)
