from BSTNode import BSTNode
class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, root, song):
        if not root:
            # Si el nodo raíz es None, creamos un nuevo nodo con el año de la canción
            return BSTNode(song.get_year())
        
        if song.get_year() < root.year:
            # Insertar en el subárbol izquierdo si el año es menor
            root.left = self.insert(root.left, song)
        elif song.get_year() > root.year:
            # Insertar en el subárbol derecho si el año es mayor
            root.right = self.insert(root.right, song)
        else:
            # Si el año ya existe en el nodo, agregamos la canción a la lista de canciones
            root.songs.append(song)
        
        return root

    def insert_song(self, song):
        self.root = self.insert(self.root, song)

    def in_order_traversal(self, root):
        result = []
        if root:
            # Recorrer el subárbol izquierdo
            result += self.in_order_traversal(root.left)
            # Agregar las canciones del nodo actual
            result.append((root.year, root.songs))
            # Recorrer el subárbol derecho
            result += self.in_order_traversal(root.right)
        return result
