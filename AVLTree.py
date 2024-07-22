from AVLNode import Node

class AVLTree:
    def insert(self, root, song):
        if not root:
            return Node(song)
        
        # Insertar en el subárbol izquierdo o derecho basado en popularidad
        if song.get_popularity() < root.song.get_popularity():
            root.left = self.insert(root.left, song)
        elif song.get_popularity() > root.song.get_popularity():
            root.right = self.insert(root.right, song)
        else:
            # Popularidades duplicadas no se permiten
            return root
        
        # Actualizar la altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Obtener el factor de equilibrio
        balance = self.get_balance(root)
        
        # Rotaciones para mantener el equilibrio
        # Rotación a la derecha
        if balance > 1 and song.get_popularity() < root.left.song.get_popularity():
            return self.rotate_right(root)
        
        # Rotación a la izquierda
        if balance < -1 and song.get_popularity() > root.right.song.get_popularity():
            return self.rotate_left(root)
        
        # Rotación a la izquierda y luego a la derecha
        if balance > 1 and song.get_popularity() > root.left.song.get_popularity():
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Rotación a la derecha y luego a la izquierda
        if balance < -1 and song.get_popularity() < root.right.song.get_popularity():
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def in_order_traversal(self, root):
        result = []
        if root:
            # Recorrer el subárbol derecho primero
            result += self.in_order_traversal(root.right)
            # Agregar el nodo actual
            result.append(root.song)
            # Luego recorrer el subárbol izquierdo
            result += self.in_order_traversal(root.left)
        return result