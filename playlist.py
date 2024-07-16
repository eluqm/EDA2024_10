import random
from queue import Queue

class Playlist:
    def __init__(self):
        self.playlist = Queue()

    def add_song(self, song):
        self.playlist.enqueue(song)

    def remove_song(self, index):
        if 0 <= index < len(self.playlist.queue):
            self.playlist.queue.pop(index)
        else:
            raise IndexError("Index out of range")

    def shuffle(self):
        random.shuffle(self.playlist.queue)

    def change_order(self, from_index, to_index):
        if from_index < 0 or from_index >= len(self.playlist.queue) or to_index < 0 or to_index >= len(self.playlist.queue):
            raise IndexError("index out of range")
        self.playlist.queue.insert(to_index, self.playlist.queue.pop(from_index))

    def get_playlist(self):
        return self.playlist.queue