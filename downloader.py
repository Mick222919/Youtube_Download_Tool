import subprocess
import threading
import time
import sys
import os
import PySimpleGUI as sg
import ffmpeg

'''------------------------------------------------ download process ------------------------------------------------'''
def download_process():
    download_cmd = '.\youtube-dl --format avi -o "I:\Youtube downloader\download_place\%(title)s.%(ext)s" https://www.youtube.com/watch?v=hfgxAL3t2Tw'
    download_cmd2 = '.\youtube-dl --extract-audio --audio-format mp3 -o "I:\Youtube downloader\download_place\%(title)s.%(ext)s" https://www.youtube.com/watch?v=hfgxAL3t2Tw'
    download_cmd3 = '.\youtube-dl --recode-video avi -o "I:\Youtube downloader\download_place\%(title)s.%(ext)s" https://www.youtube.com/watch?v=hfgxAL3t2Tw'
    download_cmd4 = '.\youtube-dl -F https://www.youtube.com/watch?v=hfgxAL3t2Tw'
    with subprocess.Popen(download_cmd, shell=True, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True) as event1:
        for line in event1.stdout:
            print(line, end='')

''' audio format  "best", "aac","flac", "mp3", "m4a", "opus", "vorbis","wav" '''
''' video FORMAT  mp4,flv,ogg,webm,mkv,avi '''

if __name__ == '__main__':
    download_process()
