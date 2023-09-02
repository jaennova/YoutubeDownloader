from pytube import YouTube, Playlist
import re
import time
import threading

def download_video(video_url, output_path, video_format):
    """
    Descarga el video o el audio de un video de YouTube y lo guarda en la carpeta especificada.

    Args:
        video_url (str): URL del video de YouTube.
        output_path (str): Ruta de la carpeta de salida.
        video_format (str): Formato del video a descargar ('audio' o 'video').

    Returns:
        None
    """
    try:
        yt = YouTube(video_url)
        if video_format == 'audio':
            stream = yt.streams.get_audio_only()
        elif video_format == 'video':
            stream = yt.streams.get_highest_resolution()  # Cambiar esto según las preferencias
        else:
            print("Formato no válido. Selecciona 'audio' o 'video'.")
            return

        # Agregar una animación mientras se descarga
        animation_thread = threading.Thread(target=print_animation)
        animation_thread.start()

        stream.download(output_path)
        animation_thread.join()  # Esperar a que la animación termine
        print(f"{video_format.capitalize()} de '{yt.title}' descargado correctamente.")
    except Exception as e:
        print(f"Error al descargar el {video_format}: {e}")
        yt = YouTube(video_url)
        if video_format == 'audio':
            stream = yt.streams.get_audio_only()
        elif video_format == 'video':
            stream = yt.streams.get_highest_resolution()  # Cambiar esto según las preferencias
        else:
            print("Formato no válido. Selecciona 'audio' o 'video'.")
            return
        
        stream.download(output_path)
        print(f"{video_format.capitalize()} de '{yt.title}' descargado correctamente.")
    except Exception as e:
        print(f"Error al descargar el {video_format}: {e}")

def print_animation():
    animation_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"  # Caracteres de animación
    for char in animation_chars:
        print(f"\rDescargando {char}", end="")
        time.sleep(0.1)  # Cambiar el tiempo de espera según la velocidad deseada
    print("\rDescarga en progreso...   ")  # Limpiar la línea de animación

def get_valid_url(prompt):
    """
    Solicita y valida una URL ingresada por el usuario.

    Args:
        prompt (str): Mensaje de solicitud.

    Returns:
        str: URL válida.
    """
    while True:
        url = input(prompt)
        if re.match(r'^(https:\/\/www\.youtube\.com\/watch\?v=[\w-]+)|(https:\/\/youtu\.be\/[\w-]+)|(https:\/\/www\.youtube\.com\/playlist\?list=[\w-]+)$', url):
            return url
        print("URL no válida. Por favor, ingrese una URL válida de un video o una lista de reproducción de YouTube.")

def download_playlist(playlist_url, output_path):
    """
    Descarga el audio de todos los videos de una lista de reproducción de YouTube y los guarda en la carpeta especificada.

    Args:
        playlist_url (str): URL de la lista de reproducción de YouTube.
        output_path (str): Ruta de la carpeta de salida.

    Returns:
        None
    """
    try:
        playlist = Playlist(playlist_url)
        for video_url in playlist.video_urls:
            download_video(video_url, output_path, "audio")  # Cambia "audio" por "video" si deseas descargar videos
        print("Descarga de la lista de reproducción completa finalizada.")
    except Exception as e:
        print(f"Error al descargar la lista de reproducción: {e}")

def main():
    print("Bienvenido al descargador de contenido de YouTube.")
    print("Puede descargar el video o el audio según prefiera")
    
    while True:
        choice = input("¿Deseas descargar un video o una lista de reproducción? (video/lista/salir): ")

        if choice.lower() == "video":
            video_url = get_valid_url("Ingrese la URL del video de YouTube: ")
            output_path = input("Ingrese la carpeta en donde se guardará la descarga: ")
            video_format = input("¿Deseas descargar el 'audio' o el 'video'? ").lower()
            download_video(video_url, output_path, video_format)
        elif choice.lower() == "lista":
            playlist_url = get_valid_url("Ingrese la URL de la lista de reproducción de YouTube: ")
            output_path = input("Ingrese la carpeta en donde se descargarán los elementos de la lista de reproducción: ")
            download_playlist(playlist_url, output_path)
        elif choice.lower() == "salir":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija 'video', 'lista' o 'salir'.")

        another_download = input("¿Deseas realizar otra descarga? (si/no): ")
        if another_download.lower() != "si":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
