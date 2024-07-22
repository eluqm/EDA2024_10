class Node:
    def __init__(self, song):
        self.song = song            # Objeto Cancion
        self.left = None            # Hijo izquierdo
        self.right = None           # Hijo derecho
        self.height = 1             # Altura del nodo
