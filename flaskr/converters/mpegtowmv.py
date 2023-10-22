from moviepy.editor import *

input_file = "video.mpeg"


output_file = "salida/video_output.wmv"


video = VideoFileClip(input_file)


audio = video.audio
video = video.set_audio(None)


video.write_videofile(output_file, codec='wmv2', preset='ultrafast')


final_video = VideoFileClip(output_file).set_audio(audio)
final_output_file = "salida/final_video_output.wmv"
final_video.write_videofile(final_output_file, codec='wmv2')


print(f"El video ha sido convertido y guardado como {final_output_file}")
