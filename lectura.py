from Cancion import Cancion
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
ejemplo_busqueda_por_titulo()