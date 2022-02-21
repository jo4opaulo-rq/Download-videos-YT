from pytube import YouTube
import os


def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    yt.download(path)

video= input("Link do video: ")

downloadYouTube(video, './Downloads/')