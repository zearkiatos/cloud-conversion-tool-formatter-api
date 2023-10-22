from moviepy.editor import *


input_file = "video.avi"

# Ruta del archivo de salida (MPEG)
output_file = "salida/video_output.mpeg"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Convertir el video al formato MPEG con códec MPEG1
video.write_videofile(output_file, codec='mpeg1video')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")
