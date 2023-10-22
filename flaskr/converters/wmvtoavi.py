from moviepy.editor import VideoFileClip

# Ruta del archivo de entrada (WMV)
input_file = "video.wmv"

# Ruta del archivo de salida (AVI)
output_file = "salida/video_output.avi"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Guardar el video en formato AVI
video.write_videofile(output_file, codec='rawvideo')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")
