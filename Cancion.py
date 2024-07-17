import csv

class Cancion:
    def __init__(self, artist_name, track_name, track_id, popularity, year, genre,
                 danceability, energy, key, loudness, mode, speechiness,
                 acousticness, instrumentalness, liveness, valence, tempo,
                 duration_ms, time_signature):
        self.artist_name = artist_name
        self.track_name = track_name
        self.track_id = track_id
        self.popularity = popularity
        self.year = year
        self.genre = genre
        self.danceability = danceability
        self.energy = energy
        self.key = key
        self.loudness = loudness
        self.mode = mode
        self.speechiness = speechiness
        self.acousticness = acousticness
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.valence = valence
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.time_signature = time_signature

    # Getters
    def get_artist_name(self):
        return self.artist_name

    def get_track_name(self):
        return self.track_name

    def get_track_id(self):
        return self.track_id

    def get_popularity(self):
        return self.popularity

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def get_danceability(self):
        return self.danceability

    def get_energy(self):
        return self.energy

    def get_key(self):
        return self.key

    def get_loudness(self):
        return self.loudness

    def get_mode(self):
        return self.mode

    def get_speechiness(self):
        return self.speechiness

    def get_acousticness(self):
        return self.acousticness

    def get_instrumentalness(self):
        return self.instrumentalness

    def get_liveness(self):
        return self.liveness

    def get_valence(self):
        return self.valence

    def get_tempo(self):
        return self.tempo

    def get_duration_ms(self):
        return self.duration_ms

    def get_time_signature(self):
        return self.time_signature

    # Setters (optional depending on your use case)
    def set_artist_name(self, artist_name):
        self.artist_name = artist_name

    def set_track_name(self, track_name):
        self.track_name = track_name

    def set_track_id(self, track_id):
        self.track_id = track_id

    def set_popularity(self, popularity):
        self.popularity = popularity

    def set_year(self, year):
        self.year = year

    def set_genre(self, genre):
        self.genre = genre

    def set_danceability(self, danceability):
        self.danceability = danceability

    def set_energy(self, energy):
        self.energy = energy

    def set_key(self, key):
        self.key = key

    def set_loudness(self, loudness):
        self.loudness = loudness

    def set_mode(self, mode):
        self.mode = mode

    def set_speechiness(self, speechiness):
        self.speechiness = speechiness

    def set_acousticness(self, acousticness):
        self.acousticness = acousticness

    def set_instrumentalness(self, instrumentalness):
        self.instrumentalness = instrumentalness

    def set_liveness(self, liveness):
        self.liveness = liveness

    def set_valence(self, valence):
        self.valence = valence

    def set_tempo(self, tempo):
        self.tempo = tempo

    def set_duration_ms(self, duration_ms):
        self.duration_ms = duration_ms

    def set_time_signature(self, time_signature):
        self.time_signature = time_signature
    ''''Objetos de canciones , String nobr , n'''
    ''' Sber si se ordena la playlis o todas las cacnciones '''