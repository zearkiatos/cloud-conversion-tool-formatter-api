from moviepy.editor import *

input_file = "video.webm"

output_file = "salida/video_output.mpeg"

video = VideoFileClip(input_file)

video.write_videofile(output_file, codec='mpeg1video')

print(f"El video ha sido convertido y guardado como {output_file}")
