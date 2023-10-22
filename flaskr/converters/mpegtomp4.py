from moviepy.editor import *

input_file = "video.mpeg"

output_file = "salida/video_output.mp4"


video = VideoFileClip(input_file)


video.write_videofile(output_file, codec='libx264', audio_codec='aac')


print(f"El video ha sido convertido y guardado como {output_file}")
