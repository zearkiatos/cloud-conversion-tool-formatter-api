from moviepy.editor import *


input_file = "video.avi"


output_file = "salida/video_output.wmv"


video = VideoFileClip(input_file)


video.write_videofile(output_file, codec='wmv2')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {output_file}")
