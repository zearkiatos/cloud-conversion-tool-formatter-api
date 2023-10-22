from moviepy.editor import *
from config.config import Config


class Converter:

    def avitomp4(self,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+output_file+'.mp4'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"El video ha sido convertido y guardado como {output_file}")
