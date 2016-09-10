#coding: utf-8
import encode
import encode720
import thumbnail
from redis import Redis
from rq import Queue
import sys

src_ts = sys.argv[1]
q = Queue(connection=Redis())
q.enqueue(encode.encodejob, src_ts, timeout=36000)
q.enqueue(thumbnail.thumbnailjob, src_ts, timeout=600)
q.enqueue(encode720.encodejob, src_ts, timeout=36000)

