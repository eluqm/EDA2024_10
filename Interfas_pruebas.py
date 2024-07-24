import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from Logic import Logic
from playlist import Playlist 

class PlaylistApp:
    def __init__(self, root, logic):
        self.root = root
        self.logic = logic
        self.playlist = []
        self.is_searching = False 
        self.current_page = 0  # Índice de la página actual
        self.canciones = self.logic.retornarCanciones()
        self.num=0
        self.cancionTB=[]
        self.root.title("Playlist Manager")
        self.root.geometry("900x700")
        self.root.configure(bg="#333333")
        
        title_frame = tk.Frame(root, bg="#333333")
        title_frame.pack(pady=10, fill=tk.X)

        title_label = tk.Label(title_frame, text="Playlist Spotify", bg="#333333", fg="#ffffff", font=("Helvetica", 16))
        title_label.pack(side=tk.LEFT, padx=10)

        search_frame = tk.Frame(title_frame, bg="#333333")
        search_frame.pack(side=tk.LEFT, padx=10)

        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 12))
        self.search_entry.pack(side=tk.LEFT, padx=10)

        search_button = ttk.Button(search_frame, text="Search", command=self.search_song, style="TButton")
        search_button.pack(side=tk.LEFT)

        filter_button = ttk.Button(search_frame, text="Filter", command=self.filter_songs, style="TButton")
        filter_button.pack(side=tk.LEFT, padx=5)

        playlist_button = ttk.Button(search_frame, text="Play List", command=self.show_playlist, style="TButton")
        playlist_button.pack(side=tk.LEFT, padx=5)

        self.grid_frame = tk.Frame(root, bg="#444444")
        self.grid_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root, bg="#333333")
        self.button_frame.pack(pady=10, fill=tk.X)

        self.siguiente_button = ttk.Button(self.button_frame, text="Siguiente", command=self.next_page, style="TButton")
        self.siguiente_button.pack(pady=5, side=tk.RIGHT, padx=10)

        style = ttk.Style()
        style.configure("TButton", foreground="black", font=("Helvetica", 10), padding=10)
        style.map("TButton", background=[("active", "#666666")], foreground=[("active", "#000000")])

        self.login_music()
        self.playlist = Playlist()
        self.root.update_idletasks()
    
    def login_music(self):
        self.num=1
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        
        start_index = self.current_page * 15
        end_index = start_index + 15
        canciones_a_mostrar = self.canciones[start_index:end_index]

        for row, cancion in enumerate(canciones_a_mostrar):
            song_text = f"{cancion.get_track_name()} - {cancion.get_artist_name()}"
            tk.Label(self.grid_frame, text=song_text, bg="#444444", fg="#ffffff", font=("Helvetica", 12)).grid(row=row, column=0, padx=5, pady=5, sticky='nsew')

            add_button = ttk.Button(self.grid_frame, text="Añadir", command=lambda c=cancion: self.add_to_playlist(c), style="TButton")
            add_button.grid(row=row, column=1, padx=5, pady=5, sticky='nsew')

        
            view_button = ttk.Button(self.grid_frame, text="Ver", command=lambda c=cancion: self.show_song_details(c), style="TButton")
            view_button.grid(row=row, column=2, padx=5, pady=5, sticky='nsew')

        self.grid_frame.columnconfigure(0, weight=8)
        self.grid_frame.columnconfigure(1, weight=1)
        self.grid_frame.columnconfigure(2, weight=1)

        for i in range(len(canciones_a_mostrar)):
            self.grid_frame.rowconfigure(i, weight=1)
            
    def next_page(self):
        if self.num==1:
            total_canciones = len(self.canciones)
            if (self.current_page + 1) * 15 < total_canciones:
                self.current_page += 1
                self.login_music()  # Cargar la siguiente página de canciones
            else:
                messagebox.showinfo("Información", "No hay más páginas disponibles")
        elif self.num==2:
            total_canciones = len(self.cancionTB)
            if (self.current_page + 1) * 15 < total_canciones:
                self.current_page += 1
                self.login_music()  # Cargar la siguiente página de canciones
            else:
                messagebox.showinfo("Información", "No hay más páginas disponibles")
            
    def show_song_details(self, cancion):
        # Crear una ventana emergente
        details_window = tk.Toplevel(self.root)
        details_window.title("Song Details")
        details_window.geometry("300x250")
        details_window.configure(bg="#333333")

        # Mostrar detalles de la canción en la ventana emergente
        details = [
            f"Track Name: {cancion.get_track_name()}",
            f"Artist Name: {cancion.get_artist_name()}",
            f"Popularity: {cancion.get_popularity()}",
            f"Year: {cancion.get_year()}",
            f"Duration: {cancion.get_duration_ms()}"
        ]
        for idx, detail in enumerate(details):
            tk.Label(details_window, text=detail, bg="#333333", fg="#ffffff", font=("Helvetica", 12)).pack(pady=5)

        # Agregar botón para cerrar la ventana emergente
        close_button = ttk.Button(details_window, text="Close", command=details_window.destroy, style="TButton")
        close_button.pack(pady=10)
    
    def update_playlist_cola(self, cola):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        start_index = self.current_page * 15
        end_index = start_index + 15
        canciones_a_mostrar = cola.queue[start_index:end_index]  

        for row, cancion in enumerate(canciones_a_mostrar):
            song_text = f"{cancion.get_track_name()} - {cancion.get_artist_name()}"
            tk.Label(self.grid_frame, text=song_text, bg="#444444", fg="#ffffff", font=("Helvetica", 12)).grid(row=row, column=0, padx=5, pady=5, sticky='nsew')

            remove_button = ttk.Button(self.grid_frame, text="Eliminar", command=lambda c=cancion: self.remove_from_playlist(c), style="TButton")
            remove_button.grid(row=row, column=1, padx=5, pady=5, sticky='nsew')

            view_button = ttk.Button(self.grid_frame, text="Ver", command=lambda c=cancion: self.show_song_details(c), style="TButton")
            view_button.grid(row=row, column=2, padx=5, pady=5, sticky='nsew')

        self.grid_frame.columnconfigure(0, weight=8)
        self.grid_frame.columnconfigure(1, weight=1)
        self.grid_frame.columnconfigure(2, weight=1)

        for i in range(len(canciones_a_mostrar)):
            self.grid_frame.rowconfigure(i, weight=1)      
        
    def update_playlist_grid(self, cancionesB):
        self.num=2
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        
        start_index = self.current_page * 15
        end_index = start_index + 15
        canciones_a_mostrar = cancionesB[start_index:end_index]

        for row, cancion in enumerate(canciones_a_mostrar):
            song_text = f"{cancion.get_track_name()} - {cancion.get_artist_name()}"
            tk.Label(self.grid_frame, text=song_text, bg="#444444", fg="#ffffff", font=("Helvetica", 12)).grid(row=row, column=0, padx=5, pady=5, sticky='nsew')

            add_button = ttk.Button(self.grid_frame, text="Añadir", command=lambda c=cancion: self.add_to_playlist(c), style="TButton")
            add_button.grid(row=row, column=1, padx=5, pady=5, sticky='nsew')

        
            view_button = ttk.Button(self.grid_frame, text="Ver", command=lambda c=cancion: self.show_song_details(c), style="TButton")
            view_button.grid(row=row, column=2, padx=5, pady=5, sticky='nsew')

        self.grid_frame.columnconfigure(0, weight=8)
        self.grid_frame.columnconfigure(1, weight=1)
        self.grid_frame.columnconfigure(2, weight=1)

        for i in range(len(canciones_a_mostrar)):
            self.grid_frame.rowconfigure(i, weight=1)
            
    def search_song(self):
        search_term = self.search_entry.get().lower()  # Obtener el texto de búsqueda y convertir a minúsculas
        
        if search_term:  # Verificar que el término de búsqueda no esté vacío
            matching_songs = self.logic.search_in_trie(search_term)  # Buscar en el Trie
            self.cancionTB=matching_songs
            self.update_playlist_grid(matching_songs)  # Actualizar la interfaz con las canciones encontradas
        else:
            self.login_music()  # Si no hay término de búsqueda, mostrar todas las canciones


    def filter_songs(self):
        # Crear la ventana emergente para filtros
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Filter Options")
        filter_window.geometry("250x200")

        # Crear un marco para las opciones de filtrado
        options_frame = tk.Frame(filter_window)
        options_frame.pack(pady=10, padx=10, fill=tk.X)

        # Crear las opciones de filtrado
        self.filter_var = tk.StringVar()
        filters = ["Por Nombre", "Por Artista", "Por Año de Lanzamiento", "Por Popularidad", "Por Duración"]

        for option in filters:
            tk.Radiobutton(options_frame, text=option, variable=self.filter_var, value=option).pack(anchor=tk.W)

        # Crear el botón de actualizar
        update_button = ttk.Button(filter_window, text="Actualizar", command=self.update_filter)
        update_button.pack(pady=10)

    def update_filter(self):
        # Método que se ejecuta cuando se presiona el botón "Actualizar"
        selected_filter = self.filter_var.get()
        print(f"Filtro seleccionado: {selected_filter}")
        
        
    def show_playlist(self):
    # Guardar el estado actual
        self.previous_page = self.current_page
        self.previous_num = self.num
    
    # Actualizar la vista de la cola de reproducción
        self.update_playlist_cola(self.playlist)
    
    # Cambiar el botón "Siguiente" por un botón "Cerrar"
        self.siguiente_button.pack_forget()  # Ocultar el botón "Siguiente"
    
        close_button = ttk.Button(self.button_frame, text="Cerrar", command=self.close_playlist, style="TButton")
        close_button.pack(pady=5, side=tk.RIGHT, padx=10)
 
        
    def add_to_playlist(self, cancion):
        self.playlist.add_song(cancion)
        messagebox.showinfo("Canción Añadida", f"{cancion.get_track_name()} de {cancion.get_artist_name()} ha sido añadida a la cola")
    
    def close_playlist(self):
        self.current_page = self.previous_page
        self.num = self.previous_num
        self.login_music()  # Volver a cargar la vista principal de canciones

    # Restaurar el botón "Siguiente"
        self.siguiente_button.pack(pady=5, side=tk.RIGHT, padx=10)
    
        for widget in self.button_frame.winfo_children():
            if widget.cget("text") == "Cerrar":
                widget.pack_forget()  # Ocultar el botón
                break


    

root = tk.Tk()
logic = Logic('spotify_data.csv')
app = PlaylistApp(root, logic)
root.mainloop()
