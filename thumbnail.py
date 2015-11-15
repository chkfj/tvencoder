#coding: utf-8

import os

def thumbnailjob(ts):
    thumb_jpg = "/media/hdd/encoded/" + os.path.basename(ts).split(".")[0] + ".cover.jpg"
    command = "ffmpeg -y -i %s -ss 120 -vframes 1 -f image2 -s 720x480 %s" % (ts, thumb_jpg)
    os.system(command)

