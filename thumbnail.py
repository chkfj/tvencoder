#coding: utf-8

from settings import settings
import os

def thumbnailjob(ts):
    thumb_jpg = settings["encoded_dir"] + "/" + os.path.basename(ts).split(".")[0] + ".mp4.cover.jpg"
    thumb720_jpg = settings["encoded720_dir"] + "/" + os.path.basename(ts).split(".")[0] + ".mp4.cover.jpg"
    command = "ffmpeg -y -i %s -ss 120 -vframes 1 -f image2 -s 720x480 %s" % (ts, thumb_jpg)
    os.system(command)
    command = "cp -f %s %s" % (thumb_jpg, thumb720_jpg)
    os.system(command)

