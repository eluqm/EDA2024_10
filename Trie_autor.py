from TNode_autor import TNode_autor

class Trie_autor:
    def __init__(self):
        self.root = TNode_autor()

    def insert(self, song):
        curr = self.root
        artist = song.get_artist_name().lower()  # Obtener el nombre del artista y convertir a minúsculas
        for c in artist:
            if not curr.has_child(c):
                curr.add_child(c, TNode_autor())
            curr = curr.get_child(c)
        curr.add_song(song)
        curr.set_end(True)

    def search_by_artist(self, artist):
        curr = self.root
        artist = artist.lower()  # Convertir el nombre del artista a minúsculas
        for c in artist:
            if not curr.has_child(c):
                return None
            curr = curr.get_child(c)
        return curr.get_songs() if curr.is_end() else None

    def autocomplete(self, prefix):
        results = []
        node = self._find_node(prefix.lower())  # Convertir el prefijo a minúsculas
        if node:
            self._collect_songs(node, results)
        return results

    def _find_node(self, prefix):
        curr = self.root
        for c in prefix:
            if not curr.has_child(c):
                return None
            curr = curr.get_child(c)
        return curr

    def _collect_songs(self, node, results):
        if node.is_end():
            results.extend(node.get_songs())
        for c, child in node.get_children().items():
            self._collect_songs(child, results)