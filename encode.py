# coding: utf-8

import json
import os
import sys

def encodejob(ts):
    dst_mp4 = "/media/hdd/encoded/" + os.path.basename(ts).split(".")[0] + ".mp4"
    encode_command = "ffmpeg -y -i %s -strict -2 -vcodec libx264 -r 30000/1001 -aspect 16:9 -s 1920x1080 -bufsize 20000k -minrate 2000k -pass 1 -movflags faststart -threads 2 %s" % (ts, dst_mp4)
    os.system(encode_command)
    

