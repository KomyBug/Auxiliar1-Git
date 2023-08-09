class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
<<<<<<< HEAD

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
                print(f"La tarea {tarea.obtenerNombre()} está lista")
            else: 
                print(f"La tarea {tarea.obtenerNombre()} no está lista")
=======
>>>>>>> 4739ad426341031bb7697b701e8639ebde433039
