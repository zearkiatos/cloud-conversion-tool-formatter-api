
from moviepy.editor import *

# Ruta del archivo de entrada
input_file = "video.mpeg"

# Ruta del archivo de salida y formato deseado
output_file = "salida/video_output.avi"

# Cargar el video de entrada
video = VideoFileClip(input_file)

# Convertir el video al formato deseado
#mp4 a avi
video.write_videofile(output_file, codec='mpeg4', audio_codec='mp3')

print(f"El video ha sido convertido y guardado como {output_file}")