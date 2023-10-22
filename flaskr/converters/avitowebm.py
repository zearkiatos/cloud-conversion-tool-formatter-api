

from moviepy.editor import *

input_file = "video.avi"

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