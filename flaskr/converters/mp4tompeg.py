from moviepy.editor import *

input_file = "video.mp4"

output_file = "salida/video_output.mpeg"


video = VideoFileClip(input_file)

audio = video.audio
video = video.set_audio(None)


video.write_videofile(output_file, codec='mpeg2video', preset='ultrafast', audio_codec='pcm_s16le')

final_video = VideoFileClip(output_file).set_audio(audio)
final_output_file = "salida/final_video_output.mpeg"
final_video.write_videofile(final_output_file, codec='mpeg2video')

# Imprimir un mensaje cuando la conversión se haya completado
print(f"El video ha sido convertido y guardado como {final_output_file}")