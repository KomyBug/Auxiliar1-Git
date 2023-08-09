class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.listo = False

    def obtenerNombre(self):
        return self.nombre

    def estaLista(self):
        return self.listo

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"[X] {tarea.obtenerNombre()}" )
            else:
                print(f"[ ] {tarea.obtenerNombre()}" )