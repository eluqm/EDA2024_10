import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import pandas as pd
from playlist import Playlist
from playlistapp_logic import PlaylistAppLogic

class PlaylistApp:
    def __init__(self, root, playlist_logic):
        self.root = root
        self.playlist_logic = playlist_logic

        self.root.title("Playlist Manager")
        self.root.geometry("600x500")
        self.root.configure(bg="#333333")

        # Frame para el título y la barra de búsqueda
        title_frame = tk.Frame(root, bg="#333333")
        title_frame.pack(pady=10)

        title_label = tk.Label(title_frame, text="Playlist Spotify", bg="#333333", fg="#ffffff", font=("Helvetica", 16))
        title_label.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(title_frame, font=("Helvetica", 12))
        self.search_entry.pack(side=tk.LEFT, padx=10)

        search_button = ttk.Button(title_frame, text="Search", command=self.search_song, style="TButton")
        search_button.pack(side=tk.LEFT)

        self.playlist_box = tk.Listbox(root, width=50, height=20, bg="#444444", fg="#ffffff", font=("Helvetica", 12))
        self.playlist_box.pack(pady=10)

        button_frame = tk.Frame(root, bg="#333333")
        button_frame.pack(pady=10)

        self.add_button = ttk.Button(button_frame, text="Add Song", command=self.add_song, style="TButton")
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.remove_button = ttk.Button(button_frame, text="Remove Song", command=self.remove_song, style="TButton")
        self.remove_button.grid(row=0, column=1, padx=5, pady=5)

        self.shuffle_button = ttk.Button(button_frame, text="Shuffle", command=self.shuffle, style="TButton")
        self.shuffle_button.grid(row=0, column=2, padx=5, pady=5)

        self.sort_by_popularity_button = ttk.Button(button_frame, text="Sort by Popularity", command=self.sort_by_popularity, style="TButton")
        self.sort_by_popularity_button.grid(row=1, column=0, padx=5, pady=5)

        self.sort_by_year_button = ttk.Button(button_frame, text="Sort by Year", command=self.sort_by_year, style="TButton")
        self.sort_by_year_button.grid(row=1, column=1, padx=5, pady=5)

        self.sort_by_duration_button = ttk.Button(button_frame, text="Sort by Duration", command=self.sort_by_duration, style="TButton")
        self.sort_by_duration_button.grid(row=1, column=2, padx=5, pady=5)

        self.update_playlist_box()

        # Estilos ttk
        style = ttk.Style()
        style.configure("TButton", foreground="black", font=("Helvetica", 10), padding=10)
        style.map("TButton", background=[("active", "#666666")], foreground=[("active", "#000000")])

    def update_playlist_box(self):
        self.playlist_box.delete(0, tk.END)
        for song in self.playlist_logic.get_playlist():
            self.playlist_box.insert(tk.END, song['track_name'])

    def add_song(self):
        song_name = simpledialog.askstring("Input", "Enter song name:")
        if song_name:
            self.playlist_logic.add_song(song_name)
            self.update_playlist_box()

    def remove_song(self):
        selected_song_index = self.playlist_box.curselection()
        if selected_song_index:
            song_name = self.playlist_box.get(selected_song_index[0])
            self.playlist_logic.remove_song(song_name)
            self.update_playlist_box()
        else:
            messagebox.showwarning("Warning", "Select a song to remove")

    def shuffle(self):
        self.playlist_logic.shuffle()
        self.update_playlist_box()

    def sort_by_popularity(self):
        self.playlist_logic.sort_playlist('popularity', 'asc')
        self.update_playlist_box()

    def sort_by_year(self):
        self.playlist_logic.sort_playlist('year', 'asc')
        self.update_playlist_box()

    def sort_by_duration(self):
        self.playlist_logic.sort_playlist('duration_ms', 'asc')
        self.update_playlist_box()

    def search_song(self):
        query = self.search_entry.get().lower()
        results = self.playlist_logic.search_song(query)
        self.playlist_box.delete(0, tk.END)
        if results:
            for result in results:
                self.playlist_box.insert(tk.END, result)
        else:
            messagebox.showinfo("Information", f"No songs found matching '{query}'")

# Definir la ruta del archivo CSV
csv_path = os.path.abspath('spotify_data.csv')

# Cargar el archivo CSV
df = pd.read_csv(csv_path, encoding='utf-8')

# Extraer las primeras 100 canciones
first_100_songs = df.head(100)

# Crear una cola de reproducción
playlist = Playlist()

# Insertar canciones en la cola de reproducción
for index, row in first_100_songs.iterrows():
    playlist.add_song(row)

# Iniciar la aplicación de Tkinter
root = tk.Tk()
logic = PlaylistAppLogic(playlist)
app = PlaylistApp(root, logic)

# Ajustar la ventana al tamaño de los elementos
root.geometry("")

root.mainloop()