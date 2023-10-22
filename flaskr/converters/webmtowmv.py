from moviepy.editor import *

input_file = "video.webm"


output_file = "salida/video_output.wmv"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Convertir el video al formato WMV con códec WMV2
video.write_videofile(output_file, codec='wmv2')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")
