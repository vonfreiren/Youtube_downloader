# importing packages
from pytube import YouTube
import os
import subprocess
from moviepy.editor import *
import glob



def convert():
    list_urls = []
    url_1 = 'https://www.youtube.com/watch?v=nsNCK3EJpao'
    list_urls.append(url_1)

    # list_urls.append('https://www.youtube.com/watch?v=v7PJqCTX5ZE')
    # list_urls.append('https://www.youtube.com/watch?v=QrSebQAbytY')
    # list_urls.append('https://www.youtube.com/watch?v=GdMtN5Ifm-I')
    # list_urls.append('https://www.youtube.com/watch?v=D1OYDcXY79w')
    # list_urls.append('https://www.youtube.com/watch?v=9cWsoVKpNjw')
    # list_urls.append('https://www.youtube.com/watch?v=hEE7Vokwe48')

    for url in list_urls:

        yt = YouTube(url)
        video = yt.streams.get_audio_only()

        destination = '/Users/mariajosealvarez/Desktop/mp3'

        out_file = video.download(output_path=destination)
        clip = AudioFileClip(out_file)
        os.chdir(destination)
        clip.write_audiofile(out_file[:-4] + ".mp3")
        clip.close()

        print(yt.title + " has been downloaded.")

    remove_mp4()

def remove_mp4():
    dir_name = '/Users/mariajosealvarez/Desktop/mp3/**'
    files = glob.glob(dir_name, recursive=True)
    for item in files:
        if item.endswith('mp4'):
            print("Removed: "+item)
            os.remove(os.path.join(dir_name, item))


if __name__ == '__main__':
    convert()
