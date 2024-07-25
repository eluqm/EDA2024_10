from Cancion import Cancion
from BSTree import BSTree
from AVLTree_duracion import AVLTree_duracion
from Trie_autor import Trie_autor 
from AVLTree import AVLTree
from Trie import Trie  
import csv

class Logic:
    
    def __init__(self, archivo_csv):
        self.canciones = self.leer_canciones_desde_csv(archivo_csv)
        self.trie = Trie()
        self.trie_autor = Trie_autor()
        self.avl_popularidad = AVLTree()
        self.avl_duracion = AVLTree_duracion()
        self.bst_año = BSTree()
        self.root_popularidad = None  
        self.root_duracion = None 
        
        for cancion in self.canciones:
            self.trie.insert(cancion)
            self.trie_autor.insert(cancion)
            self.avl_popularidad.insert(self.root_popularidad, cancion)
            self.avl_duracion.insert(self.root_duracion, cancion)
            self.bst_año.insert_song(cancion)
    
    def leer_canciones_desde_csv(self, nombre_archivo):
        canciones = []
        with open(nombre_archivo, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cancion = Cancion(
                    row['artist_name'],
                    row['track_name'],
                    row['track_id'],
                    int(row['popularity']),
                    int(row['year']),
                    row['genre'],
                    float(row['danceability']),
                    float(row['energy']),
                    int(row['key']),
                    float(row['loudness']),
                    int(row['mode']),
                    float(row['speechiness']),
                    float(row['acousticness']),
                    float(row['instrumentalness']),
                    float(row['liveness']),
                    float(row['valence']),
                    float(row['tempo']),
                    int(row['duration_ms']),
                    int(row['time_signature'])
                )
                canciones.append(cancion)
        return canciones

    def busqueda_por_titulo(self, titulo_cancion):
        result = self.trie.search(titulo_cancion)
        return result 

    def busqueda_por_artista(self, artist_name):
        canciones_artista = self.trie_autor.search_by_artist(artist_name)
        return canciones_artista if canciones_artista else []

    def ordenar_por_popularidad(self):
        root = self.avl_popularidad.root
        return self.avl_popularidad.in_order_traversal(root) if root else []

    def ordenar_por_año(self):
        return self.bst_año.in_order_traversal(self.bst_año.root) if self.bst_año.root else []

    def prueba_avl_duracion(self):
        root = self.avl_duracion.root
        return self.avl_duracion.in_order_traversal(root) if root else []
    
    def retornarCanciones(self):
        canciones=[]
        canciones=self.trie.get_all_songs()
        return canciones
    
    def search_in_trie(self, prefix):
        songs = self.trie.autocomplete(prefix)  
        return songs