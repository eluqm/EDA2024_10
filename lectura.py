from Cancion import Cancion
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
#Test de la lectura de la cancion 10000
archivo_csv = 'spotify_data.csv' 
canciones = leer_canciones_desde_csv(archivo_csv)

if canciones:
    primera_cancion = canciones[0]
    print(primera_cancion.get_artist_name())
    print(primera_cancion.get_track_name())
    print(primera_cancion.get_popularity())