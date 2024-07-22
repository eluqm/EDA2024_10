class AVLNode_duracion:
    def __init__(self, duration):
        self.duration = duration
        self.songs = []  # Lista para almacenar canciones con la misma duración
        self.left = None
        self.right = None
        self.height = 1  # Altura inicial del nodo
