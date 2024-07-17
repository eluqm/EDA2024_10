from Cancion import Cancion
from Trie_autor import Trie_autor 
from Trie import Trie  # Asegúrate de tener la implementación de Trie y TNode correctamente
import csv

def leer_canciones_desde_csv(nombre_archivo):
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

def ejemplo_busqueda_por_titulo():
    archivo_csv = 'spotify_data.csv'  # Reemplaza con tu archivo CSV real
    canciones = leer_canciones_desde_csv(archivo_csv)

    trie = Trie()

    # Insertar todas las canciones en el trie por título
    for cancion in canciones:
        trie.insert(cancion)

    # Ejemplo de búsqueda por título
    titulo_cancion = 'I\'m Yours'  # Reemplaza con el título de la canción que desees buscar
    cancion_encontrada = trie.search(titulo_cancion)

    if cancion_encontrada:
        print("Canción:", cancion_encontrada.get_track_name())
        print("Artista:", cancion_encontrada.get_artist_name())
        print("Popularidad:", cancion_encontrada.get_popularity())
        print("Año:", cancion_encontrada.get_year())
        print("Género:", cancion_encontrada.get_genre())
        print("-----")
    else:
        print(f"No se encontró la canción con el título {titulo_cancion}")

# Ejecutar ejemplo de búsqueda por título
#ejemplo_busqueda_por_titulo()
def ejemplo_busqueda_por_artista():
    archivo_csv = 'spotify_data.csv'  # Reemplaza con tu archivo CSV real
    canciones = leer_canciones_desde_csv(archivo_csv)

    trie = Trie_autor()

    # Insertar todas las canciones en el trie
    for cancion in canciones:
        trie.insert(cancion)

    # Ejemplo de búsqueda por artista
    artist_name = 'Jason Mraz'  # Reemplaza con el nombre del artista que desees buscar
    canciones_artista = trie.search_by_artist(artist_name)

    if canciones_artista:
        for cancion in canciones_artista:
            print("Canción:", cancion.get_track_name())
            print("Artista:", cancion.get_artist_name())
            print("Popularidad:", cancion.get_popularity())
            print("Año:", cancion.get_year())
            print("Género:", cancion.get_genre())
            print("-----")
    else:
        print(f"No se encontraron canciones para el artista {artist_name}")

# Ejecutar ejemplo de búsqueda por artista
ejemplo_busqueda_por_artista()