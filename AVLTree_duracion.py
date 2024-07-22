from AVLNode_duracion import AVLNode_duracion

class AVLTree_duracion:
    def insert(self, root, song):
        if not root:
            # Crear un nuevo nodo si no hay nodo
            return AVLNode_duracion(song.get_duration_ms())
        
        if song.get_duration_ms() > root.duration:
            # Insertar en el subárbol izquierdo si la duración es mayor (orden descendente)
            root.left = self.insert(root.left, song)
        elif song.get_duration_ms() < root.duration:
            # Insertar en el subárbol derecho si la duración es menor
            root.right = self.insert(root.right, song)
        else:
            # Si la duración ya existe, agregar la canción a la lista del nodo
            root.songs.append(song)
        
        # Actualizar la altura del nodo actual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # Obtener el factor de equilibrio
        balance = self.get_balance(root)
        
        # Rotaciones para mantener el equilibrio
        # Rotación a la derecha
        if balance > 1 and song.get_duration_ms() < root.left.duration:
            return self.rotate_right(root)
        
        # Rotación a la izquierda
        if balance < -1 and song.get_duration_ms() > root.right.duration:
            return self.rotate_left(root)
        
        # Rotación a la izquierda y luego a la derecha
        if balance > 1 and song.get_duration_ms() > root.left.duration:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Rotación a la derecha y luego a la izquierda
        if balance < -1 and song.get_duration_ms() < root.right.duration:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root

    def rotate_left(self, z):
        y = z.right
        if y is None:
            return z  # No se puede realizar una rotación a la izquierda si no hay un subárbol derecho

        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        if y is None:
            return z  # No se puede realizar una rotación a la derecha si no hay un subárbol izquierdo

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
            # Recorrer el subárbol derecho (para mayor duración primero)
            result += self.in_order_traversal(root.right)
            # Agregar las canciones del nodo actual
            result.append((root.duration, root.songs))
            # Recorrer el subárbol izquierdo
            result += self.in_order_traversal(root.left)
        return result
