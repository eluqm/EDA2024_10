class TNode_autor:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.songs = []  # Lista de objetos Cancion

    def add_child(self, character, child):
        self.children[character] = child

    def get_children(self):
        return self.children

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

    def set_end(self, end):
        self.isEnd = end

    def is_end(self):
        return self.isEnd

    def get_child(self, c):
        return self.children.get(c)

    def has_child(self, character):
        return character in self.children