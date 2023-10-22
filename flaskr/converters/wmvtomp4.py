from moviepy.editor import VideoFileClip

# Ruta del archivo de entrada (WMV)
input_file = "video.wmv"

# Ruta del archivo de salida (MP4)
output_file = "salida/video_output.mp4"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Guardar el video en formato MP4
video.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")