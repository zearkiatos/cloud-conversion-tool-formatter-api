from moviepy.editor import *

input_file = "video.webm"

output_file = "salida/video_output.avi"

video = VideoFileClip(input_file)

video.write_videofile(output_file, codec='rawvideo')

print(f"El video ha sido convertido y guardado como {output_file}")
