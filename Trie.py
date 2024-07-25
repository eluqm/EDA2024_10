from TNode import TNode  # Asegúrate de importar TNode si aún no lo has hecho

class Trie:
    def __init__(self):
        self.root = TNode()

    def insert(self, song):
        curr = self.root
        title = song.get_track_name().lower()  # Obtener el título de la canción y convertir a minúsculas
        for c in title:
            if not curr.has_child(c):
                curr.add_child(c, TNode())
            curr = curr.get_child(c)
        curr.set_song_object(song)
        curr.set_end(True)

    def delete(self, title):
        self._remove(self.root, title.lower(), 0)

    def _remove(self, curr, title, idx):
        if idx == len(title):
            if not curr.is_end():
                return False
            curr.set_end(False)
            return not bool(curr.get_children())

        c = title[idx]
        child = curr.get_child(c)
        if child is None:
            return False

        delete_child = self._remove(child, title, idx + 1)

        if delete_child:
            del curr.get_children()[c]
            return not bool(curr.get_children()) and not curr.is_end()

        return False

    def replace(self, title, new_song):
        self.delete(title)
        self.insert(new_song)

    def search(self, title):
        curr = self.root
        title = title.lower()  # Convertir el título de búsqueda a minúsculas
        for c in title:
            if not curr.has_child(c):
                return None
            curr = curr.get_child(c)
        return curr.get_song_object() if curr.is_end() else None

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
            results.append(node.get_song_object())
        for c, child in node.get_children().items():
            self._collect_songs(child, results)

    def get_all_songs(self):
        results = []
        self._collect_all_songs(self.root, results)
        return results

    def _collect_all_songs(self, node, results):
        if node.is_end():
            results.append(node.get_song_object())
        for child in node.get_children().values():
            self._collect_all_songs(child, results)