class TNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.song_object = None  # Aquí almacenaremos el objeto Cancion

    def add_child(self, character, child):
        self.children[character] = child

    def get_children(self):
        return self.children

    def set_song_object(self, song_object):
        self.song_object = song_object

    def get_song_object(self):
        return self.song_object

    def set_end(self, end):
        self.isEnd = end

    def is_end(self):
        return self.isEnd

    def get_child(self, c):
        return self.children.get(c)

    def has_child(self, character):
        return character in self.children