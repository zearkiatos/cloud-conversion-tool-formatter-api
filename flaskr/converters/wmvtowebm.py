from moviepy.editor import VideoFileClip

# Ruta del archivo de entrada (WMV)
input_file = "video.wmv"

# Ruta del archivo de salida (WebM)
output_file = "salida/video_output.webm"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Guardar el video en formato WebM
video.write_videofile(output_file, codec='libvpx', audio_codec='libvorbis')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")
