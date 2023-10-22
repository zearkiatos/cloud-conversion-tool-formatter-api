# from moviepy.editor import *

# # Ruta del archivo de entrada (MP4)
# input_file = "video.mp4"

# # Ruta del archivo de salida (WebM)
# output_file = "video_output.webm"

# # Cargar el video de entrada
# video = VideoFileClip(input_file)

# # Extraer el audio del video
# audio = video.audio

# # Convertir el video al formato WebM con códec VP9 para video y AAC para audio
# video.write_videofile(output_file, codec='libvpx-vp9', audio_codec='mp3', preset='ultrafast', audio=audio)

# # Imprimir un mensaje cuando la conversión se haya completado
# print(f"El video ha sido convertido y guardado como {output_file}")

from moviepy.editor import *

input_file = "video.mp4"

output_file = "salida/video_output.webm"


video = VideoFileClip(input_file)

audio = video.audio
video = video.set_audio(None)


video.write_videofile(output_file, codec='libvpx-vp9', preset='ultrafast', audio_codec='aac')

final_video = VideoFileClip(output_file).set_audio(audio)
final_output_file = "salida/final_video_output.webm"
final_video.write_videofile(final_output_file, codec='libvpx-vp9')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {final_output_file}")