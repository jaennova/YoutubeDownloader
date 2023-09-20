# Descargador de Contenido de YouTube

<!-- ![YouTube Downloader](https://example.com/your_image.png) -->

## Resumen del Proyecto

Este es un programa en Python que te permite descargar contenido (audio o video) de YouTube. Puedes descargar videos individuales o incluso contenido de listas de reproducción.

## Instalación

1. Clona o descarga este repositorio en tu máquina.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala las dependencias ejecutando el siguiente comando:

```bash
pip install pytube
```

Puedes actualizar pip usando el siguiente comando:

```bash
python.exe -m pip install --upgrade pip
```
## Uso

Ejecuta el script youtube_downloader.py para comenzar a descargar contenido de YouTube.

```bash
python youtube_downloader.py
```
Sigue las instrucciones en pantalla para ingresar las URL, las rutas de salida y los formatos de descarga (audio o video).

## Ejemplos

1. Descargar audio de un video:
    - URL: https://www.youtube.com/watch?v=example_video_id
    - Formato: audio
    - Carpeta de salida: nombreDeLaCarpeta/audio

2. Descargar video:
- URL: https://www.youtube.com/watch?v=example_video_id
- Formato: video
- Carpeta de salida: nombreDeLaCarpeta/videos

3. Descargar lista de reproducción:

- URL: https://www.youtube.com/playlist?list=example_playlist_id
- Carpeta de salida: nombreDeLaCarpeta/playlist
