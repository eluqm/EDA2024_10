from Trie import Trie

class PlaylistAppLogic:
    def __init__(self, playlist):
        self.playlist = playlist
        self.trie = Trie()  # Instancia del trie para almacenar nombres de canciones

        # Insertar canciones en el trie
        for song in self.playlist.playlist.queue:
            self.trie.insert(song['track_name'].lower())

    def add_song(self, song_name):
        self.playlist.add_song({'track_name': song_name})
        self.trie.insert(song_name.lower())  # Insertar en el trie

    def remove_song(self, song_name):
        # Buscar y eliminar la canción
        found_song = None
        for song in self.playlist.playlist.queue:
            if song['track_name'].lower() == song_name.lower():
                found_song = song
                break

        if found_song:
            self.playlist.playlist.queue.remove(found_song)
            self.trie.delete(song_name.lower())  # Eliminar del trie

    def shuffle(self):
        self.playlist.shuffle()

    def sort_playlist(self, criteria, order):
        reverse = (order == 'desc')
        self.playlist.playlist.queue.sort(key=lambda x: x[criteria], reverse=reverse)

    def search_song(self, query):
        # Usar el trie para buscar coincidencias
        results = self.trie.autocomplete(query.lower())
        return results

    def get_playlist(self):
        return self.playlist.playlist.queue