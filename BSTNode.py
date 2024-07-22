class BSTNode:
    def __init__(self, year):
        self.year = year  # Año del nodo
        self.songs = []   # Lista de canciones del año específico
        self.left = None  # Hijo izquierdo
        self.right = None # Hijo derecho