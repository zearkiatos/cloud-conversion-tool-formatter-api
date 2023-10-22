from moviepy.editor import *
from config.config import Config


class Converter:

    def avitomp4(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mp4'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def avitompeg(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mpeg'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='mpeg1video')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def avitowebm(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        video = VideoFileClip(input_file)
        audio = video.audio
        video = video.set_audio(None)
        video.write_videofile(output_file_ini, codec='libvpx-vp9', preset='ultrafast', audio_codec='aac')
        final_video = VideoFileClip(output_file).set_audio(audio)
        final_video.write_videofile(output_file, codec='libvpx-vp9')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def avitowmv(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='wmv2')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def mp4toavi(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.avi'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='mpeg4', audio_codec='mp3')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def mp4tompeg(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mpeg'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mpeg'
        
        video = VideoFileClip(input_file)

        audio = video.audio
        video = video.set_audio(None)


        video.write_videofile(output_file_ini, codec='mpeg2video', preset='ultrafast', audio_codec='pcm_s16le')

        final_video = VideoFileClip(output_file_ini).set_audio(audio)
        final_video.write_videofile(output_file, codec='mpeg2video')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def mp4towebm(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        
        video = VideoFileClip(input_file)

        audio = video.audio
        video = video.set_audio(None)


        video.write_videofile(output_file_ini, codec='libvpx-vp9', preset='ultrafast', audio_codec='aac')

        final_video = VideoFileClip(output_file_ini).set_audio(audio)
        final_video.write_videofile(output_file, codec='libvpx-vp9')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def mp4towmv(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        
        video = VideoFileClip(input_file)


        audio = video.audio
        video = video.set_audio(None)


        video.write_videofile(output_file_ini, codec='wmv2', preset='ultrafast')


        final_video = VideoFileClip(output_file_ini).set_audio(audio)
        final_video.write_videofile(output_file, codec='wmv2')
        print(f"El video ha sido convertido y guardado como {output_file}")

    
    def mpegtoavi(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.avi'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='mpeg4', audio_codec='mp3')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def mpegtomp4(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mp4'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def mpegtowebm(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        
        video = VideoFileClip(input_file)

        audio = video.audio
        video = video.set_audio(None)


        video.write_videofile(output_file_ini, codec='libvpx-vp9', preset='ultrafast', audio_codec='aac')

        final_video = VideoFileClip(output_file_ini).set_audio(audio)
        final_video.write_videofile(output_file, codec='libvpx-vp9')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def mpegtowmv(self,id,input_file,output_file):
        config=Config()
        output_file_ini = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        
        video = VideoFileClip(input_file)


        audio = video.audio
        video = video.set_audio(None)


        video.write_videofile(output_file_ini, codec='wmv2', preset='ultrafast')


        final_video = VideoFileClip(output_file_ini).set_audio(audio)
        final_video.write_videofile(output_file, codec='wmv2')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def webmtoavi(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.avi'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='rawvideo')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def webmtomp4(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mp4'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac', preset='ultrafast')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def webmtompeg(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mpeg'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='mpeg1video')
        print(f"El video ha sido convertido y guardado como {output_file}")


    def webmtowmv(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.wmv'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='wmv2')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def wmvmtoavi(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.avi'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='rawvideo')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def wmvmtomp4(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mp4'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libx264', audio_codec='aac')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def wmvtompeg(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.mpeg'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='mpeg1video')
        print(f"El video ha sido convertido y guardado como {output_file}")

    def wmvtowebm(self,id,input_file,output_file):
        config=Config()
        output_file = config.PATH_STORAGE+'output/'+str(id)+output_file+'.webm'
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, codec='libvpx', audio_codec='libvorbis')
        print(f"El video ha sido convertido y guardado como {output_file}")